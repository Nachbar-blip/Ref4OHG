# -*- coding: utf-8 -*-
"""Tests fuer das Level-Gate (tests/level_check.py).

Befund 2026-09-30 (Review Kl. 10 Block C): In 10-stoch-mehrstufig stand die MC-Option
"0{,}5" ausserhalb einer Mathe-Umgebung und wurde im Browser woertlich angezeigt.
Kein Gate sah das: level_check kannte nur fehlende Backslaesche, katex_check rendert
gar nicht, was ausserhalb von \\(...\\) steht. Nur die Sichtpruefung fand es.
"""
import level_check as lk


def _aufgabe(**kw):
    a = {"id": 1, "level": 1, "typ": "numerisch", "frage": "Berechne 2 + 3.",
         "loesung": 5, "toleranz": 0.1, "tipp": "Zaehle zusammen.", "loesungsweg": "2 + 3 = 5"}
    a.update(kw)
    return a


def test_mathe_markup_ausserhalb_der_umgebung_ist_hart():
    """0{,}5 im Klartext rendert woertlich — harter Fehler."""
    hart = lk.mathe_markup_ausserhalb(_aufgabe(frage="Die Wahrscheinlichkeit ist 0{,}5."))
    assert hart == ["frage"]


def test_markup_innerhalb_der_umgebung_ist_erlaubt():
    """Dasselbe Markup innerhalb von \\(...\\) und $$...$$ ist korrekt."""
    assert lk.mathe_markup_ausserhalb(_aufgabe(frage="Es gilt \\(p = 0{,}5\\).")) == []
    assert lk.mathe_markup_ausserhalb(_aufgabe(loesungsweg="$$p = 0{,}5$$ also die Haelfte.")) == []


def test_befehl_ausserhalb_der_umgebung_ist_hart():
    """Auch ein KaTeX-Befehl ausserhalb der Umgebung rendert woertlich."""
    assert lk.mathe_markup_ausserhalb(_aufgabe(tipp="Nimm \\sqrt{2} als Faktor.")) == ["tipp"]


def test_mc_optionen_werden_mitgeprueft():
    """Der Befund lag in einer MC-Option, nicht im Aufgabentext."""
    a = _aufgabe(typ="mc", optionen=["0", "0{,}5", "1", "je nach Experiment"], korrekt=2)
    assert lk.mathe_markup_ausserhalb(a) == ["optionen[1]"]


def test_normaler_text_bleibt_still():
    """Dezimalkomma als echtes Komma und Prozentzeichen loesen nichts aus."""
    a = _aufgabe(frage="Die Quote betraegt 0,5 bzw. 50 %.", loesungsweg="Haelfte von 1 ist 0,5.")
    assert lk.mathe_markup_ausserhalb(a) == []


def test_null_auswertung_greift_in_allen_ableitungs_trainern():
    """Befund 2026-09-30 (Welle Kl. 11): Die Auswertung bei x = 0 laesst bei Produkt- und
    Kettenregel je einen Summanden wegfallen und trivialisiert die Regel. Der Check hing an
    'ableitungsregeln|kettenregel' — ausgerechnet 11-ableitung-ketten-produkt, der Trainer mit
    14 solchen Aufgaben, fiel durchs Raster."""
    for name in ("11-ableitung-ketten-produkt.html", "11-ableitungsregeln.html",
                 "11-e-funktion-ableitung.html"):
        assert lk.KETTEN_TRAINER.search(name), name


def test_null_auswertung_greift_nicht_bei_fremden_trainern():
    """Kein Fehlalarm, wo 'Produkt' etwas anderes meint."""
    assert not lk.KETTEN_TRAINER.search("12-skalarprodukt.html")


def test_kleinerzeichen_vor_buchstabe_ist_hart():
    """Befund 2026-09-30 (Review Kl. 11 Block A2): Die Engine setzt frage/optionen/tipp/
    loesungsweg per innerHTML. Ein '<' unmittelbar vor einem Buchstaben startet fuer den
    HTML-Parser ein Tag und frisst den Text bis zum naechsten '>' - im Bild fehlte dadurch
    die halbe Fallunterscheidung. Weder level_check noch katex_check sahen das."""
    assert lk.html_frisst_text(_aufgabe(loesungsweg="Fuer \\(a<e\\) gibt es keinen.")) == ["loesungsweg"]
    assert lk.html_frisst_text(_aufgabe(frage="Es gilt \\(1<x<5\\).")) == ["frage"]


def test_kleinerzeichen_mit_abstand_ist_erlaubt():
    """'< ' und '<0' starten kein Tag - der HTML-Parser liest sie als Text."""
    assert lk.html_frisst_text(_aufgabe(frage="Es gilt \\(2 < x < 7\\).")) == []
    assert lk.html_frisst_text(_aufgabe(loesungsweg="Hier ist \\(f'(x)<0\\).")) == []


def test_erlaubte_auszeichnung_bleibt_still():
    """<b>…</b> ist ausdruecklich erlaubt (Fettdruck-Regel aus CLAUDE.md)."""
    assert lk.html_frisst_text(_aufgabe(frage="Das ist <b>wichtig</b>.")) == []


def test_tipp_mit_bruch_ab_stufe4():
    """Befund 2026-09-30 (Review Kl. 12 Block A): Tipps wie '= 1/5' nahmen die Antwort vorweg,
    rutschten aber durch, weil das Gate nur dezimal und erst ab Betrag 10 prueft."""
    assert lk.tipp_verraet_loesung(r"\(\sqrt{2} = 2^{1/2}\).", 0.5, 4)
    assert not lk.tipp_verraet_loesung(r"\(\sqrt{2} = 2^{1/2}\).", 0.5, 2)


def test_tipp_mit_kleiner_ganzer_zahl_nur_als_ergebnis():
    """Kleine ganze Zahlen zaehlen nur hinter '=' oder '⇒'. Als Index (E_2), Exponent (r^2)
    oder Nenner (1/3) stehen sie staendig zufaellig im Text - ein Gate, das jede 2 meldet,
    erzieht dazu, Warnungen zu ignorieren."""
    assert lk.tipp_verraet_loesung(r"\(y=0 \Rightarrow s=0\). Dann \(t=2\).", 2, 4)
    assert not lk.tipp_verraet_loesung(r"Schnittgerade von \(E_1\) und \(E_2\) bestimmen.", 2, 6)
    assert not lk.tipp_verraet_loesung(r"Was muss mit \(r^2\) passieren?", 2, 6)
    assert not lk.tipp_verraet_loesung(r"\(S = \frac{1}{3}(A+B+C)\).", 1, 4)


def test_tipp_grosse_zahl_weiterhin_auf_jeder_stufe():
    """Die bisherige Regel (ab Betrag 10) gilt unveraendert auch unterhalb Stufe 4."""
    assert lk.tipp_verraet_loesung("30000 cm³ sind 30 l.", 30, 1)


def test_optionsbuchstabe_im_loesungsweg_ist_hart():
    """Befund 2026-09-30 (Welle Kl. 11): Die Engine mischt die MC-Optionen. Ein Loesungsweg,
    der sie mit 'Option A' anspricht, zeigt im Bild auf eine andere Option - zwei Renderings
    derselben Aufgabe lieferten verschiedene Reihenfolgen. Im Quelltext ist das nicht zu sehen."""
    a = _aufgabe(typ="mc", optionen=["4", "5", "6", "7"], korrekt=1,
                 loesungsweg="Option B ist richtig, weil 2+3 = 5 ist.")
    assert lk.optionsbuchstabe(a) == ["loesungsweg"]


def test_optionsposition_im_loesungsweg_ist_hart():
    """Befund 2026-09-30 (Welle Kl. 12): Statt des Buchstabens wurde die Position genannt
    ("die dritte Antwort"). Die Engine mischt, also zeigt auch das ins Leere."""
    a = _aufgabe(typ="mc", optionen=["4", "5", "6", "7"], korrekt=1,
                 loesungsweg="Die dritte Antwort entsteht, wenn man falsch kuerzt.")
    assert lk.optionsbuchstabe(a) == ["loesungsweg"]


def test_zeile_eines_gleichungssystems_ist_keine_option():
    """'die dritte Zeile' meint eine Gleichungszeile, keine Antwortmoeglichkeit."""
    a = _aufgabe(typ="mc", optionen=["ja", "nein", "nur fuer k=1", "nur fuer k=0"], korrekt=0,
                 loesungsweg="Fuer jedes andere k bleibt die dritte Zeile unerfuellt.")
    assert lk.optionsbuchstabe(a) == []


def test_mathe_mit_buchstaben_schlaegt_nicht_an():
    """P(A|B) und aehnliche Terme sind keine Options-Verweise."""
    a = _aufgabe(typ="mc", optionen=["0,2", "0,3", "0,4", "0,5"], korrekt=0,
                 loesungsweg="Es gilt \\(P(A \\cap B) = P(A) \\cdot P(B)\\).")
    assert lk.optionsbuchstabe(a) == []


def test_ohne_mc_keine_pruefung():
    """Numerische Aufgaben haben keine Optionen, die gemischt werden koennten."""
    assert lk.optionsbuchstabe(_aufgabe(loesungsweg="Variante A des Verfahrens.")) == []


def test_gate_meldet_den_befund_als_harten_fehler():
    """Der Check haengt im Gate und landet in der Fehlerliste, nicht in den Warnungen."""
    from pathlib import Path
    aufgaben = [_aufgabe(id=i, level=(i - 1) // 6 + 1) for i in range(1, 37)]
    aufgaben[3]["frage"] = "Die Summe ist 0{,}5."
    hart, warn = lk.pruefe_trainer(Path("x.html"), aufgaben)
    assert any("Mathe-Markup ausserhalb" in f and "#4" in f for f in hart)
