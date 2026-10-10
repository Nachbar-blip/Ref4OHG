# -*- coding: utf-8 -*-
"""Tests fuer das Lehrplan-Gate Niedersachsen (tests/lehrplan_check.py)."""
import lehrplan_check as lp


def _a(**kw):
    a = {"id": 1, "level": 1, "typ": "numerisch", "frage": "Berechne 2 + 3.",
         "tipp": "Zähle zusammen.", "loesungsweg": "2 + 3 = 5"}
    a.update(kw)
    return a


def _fehler(klasse, text, feld="frage", datei="x.html"):
    return lp.pruefe(klasse, datei, [_a(**{feld: text})])[0]


def _warnung(klasse, text, feld="frage"):
    return lp.pruefe(klasse, "x.html", [_a(**{feld: text})])[1]


def test_vektor_in_der_sek1_ist_fehler():
    fehler, _ = lp.pruefe(9, "9-x.html", [_a(frage="Bestimme den Vektor von A nach B.")])
    assert len(fehler) == 1 and "vektor" in fehler[0]


def test_vektor_in_der_qualifikationsphase_ist_erlaubt():
    assert lp.pruefe(12, "12-x.html", [_a(frage="Bestimme den Vektor von A nach B.")]) == ([], [])


def test_hypothesentest_ist_in_jeder_spalte_fehler():
    for klasse in range(7, 14):
        fehler, _ = lp.pruefe(klasse, "x.html", [_a(loesungsweg="Der Hypothesentest lehnt ab.")])
        assert fehler, klasse


def test_produktregel_erst_in_der_qualifikationsphase():
    assert lp.pruefe(11, "11-x.html", [_a(tipp="Nutze die Produktregel.")])[0]
    assert lp.pruefe(12, "12-x.html", [_a(tipp="Nutze die Produktregel.")]) == ([], [])


def test_produktregel_ist_in_der_sek1_kein_fehler():
    """In 7-10 heisst so die Pfadregel bzw. das Wurzelgesetz - verboten nur in Spalte 11."""
    for klasse in (7, 8, 9, 10):
        assert lp.pruefe(klasse, "x.html", [_a(tipp="Nutze die Produktregel.")]) == ([], []), klasse
    assert lp.pruefe(11, "11-x.html", [_a(tipp="Nutze die Produktregel.")])[0]


def test_kettenregel_und_stammfunktion_bleiben_in_der_sek1_verboten():
    for klasse in (7, 8, 9, 10, 11):
        assert _fehler(klasse, "Nutze die Kettenregel."), klasse
        assert _fehler(klasse, "Bilde eine Stammfunktion."), klasse
    assert _fehler(12, "Nutze die Kettenregel und bilde eine Stammfunktion.") == []


def test_additionsverfahren_in_7_bis_10():
    assert lp.pruefe(8, "8-x.html", [_a(frage="Löse mit dem Additionsverfahren.")])[0]
    assert lp.pruefe(12, "12-x.html", [_a(loesungsweg="Additionsverfahren: I + II.")]) == ([], [])


def test_optionen_werden_mitgelesen():
    a = _a(typ="mc", optionen=["Polynomdivision", "Ausklammern", "p-q-Formel", "Raten"], korrekt=1)
    assert lp.pruefe(11, "11-x.html", [a])[0]


def test_wort_aus_anderem_bundesland_ist_warnung():
    fehler, warnungen = lp.pruefe(12, "12-x.html", [_a(frage="Leite auf: \\(f(x) = 2x\\). (Aufleiten)")])
    assert fehler == [] and len(warnungen) == 1 and "aufleit" in warnungen[0]


def test_teilwort_schlaegt_an():
    """Der Begriff zaehlt auch im Wortinneren: Richtungsvektor, Ortsvektor, Flaechenintegral."""
    for text in ("Der Richtungsvektor ist gesucht.", "Der Ortsvektor von P.", "Die Stützvektoren.",
                 "Berechne das Flächenintegral.", "Vektoren addieren.", "VEKTOR"):
        assert _fehler(9, text), text
    for text in ("Der Kollektor heizt.", "Der Sektor hat 60°.", "Integriere die Gruppe ins Team."):
        assert lp.pruefe(9, "9-x.html", [_a(frage=text)]) == ([], []), text


def test_ungleichung_frisst_keinen_text():
    """Befund Review 2026-10-10: normalisiere() aus level_check loescht alles zwischen '<' und
    '>'. In 13-eA-beurteilende-statistik #19 verschwand so der Tipp mit 'Nullhypothese'
    zwischen dem '<' im Loesungsweg und dem '>' in einer Option. Hier nachgebaut."""
    a = _a(id=19, level=4, typ="mc", korrekt=0,
           frage="Ein Hersteller behauptet, mindestens 80 % seien fehlerfrei. Wie lauten \\(H_0\\) und \\(H_1\\)?",
           optionen=["\\(H_0\\colon p \\ge 0{,}80\\) und \\(H_1\\colon p < 0{,}80\\)",
                     "\\(H_0\\colon p \\le 0{,}80\\) und \\(H_1\\colon p > 0{,}80\\)",
                     "\\(H_0\\colon p = 0{,}80\\) und \\(H_1\\colon p = 0{,}70\\)",
                     "\\(H_0\\colon p < 0{,}80\\) und \\(H_1\\colon p \\ge 0{,}80\\)"],
           tipp="Die Nullhypothese enthält die Behauptung des Herstellers.",
           loesungsweg="\\(H_0\\colon p \\ge 0{,}80\\) gegen \\(H_1\\colon p < 0{,}80\\). Linksseitig.")
    fehler, _ = lp.pruefe(13, "13-x.html", [a])
    assert len(fehler) == 1 and "nullhypothese" in fehler[0]
    assert _fehler(9, "Für \\(x < 2\\) nimm den Vektor, für \\(x > 5\\) nicht.")
    assert _fehler(9, "Wenn \\(a<b\\), bilde das Integral; sonst \\(a>b\\).")


def test_echte_tags_trennen_oder_verschwinden():
    """<br> ist ein Zeilenumbruch (Leerraum), <b>…</b> steht mitten im Wort."""
    for text in ("Ergebnis<br>Vektor \\(v\\)", "Lösung:<br/>Ableitung", "Summe</b>Integral",
                 "<b>Vektor</b>", "Vek<b>tor</b>", "<span class=\"x\">Vektor</span>"):
        assert _fehler(9, text), text
    assert _fehler(12, "partiell<br>integrieren")


def test_weiche_trennstriche_verstecken_nichts():
    assert _fehler(9, "Vek­tor (weiches Trennzeichen)")
    assert _fehler(9, "Vek&shy;tor")
    assert _fehler(9, "&nbsp;Vektor")


def test_felder_werden_nicht_zusammengezogen():
    """Ein Muster darf nicht ueber die Feldgrenze greifen."""
    a = _a(frage="Hier wird partiell", loesungsweg="integriert wird hier nichts.", tipp="x")
    assert lp.pruefe(12, "12-x.html", [a]) == ([], [])
    b = _a(typ="mc", optionen=["gebrochen", "rational", "ganz", "reell"], korrekt=0)
    assert lp.pruefe(12, "12-x.html", [b]) == ([], [])


def test_alle_begriffe_einer_aufgabe_werden_genannt():
    fehler, _ = lp.pruefe(9, "9-x.html", [_a(frage="Vektor und Integral", tipp="Nimm die Ableitung.")])
    assert len(fehler) == 1
    for begriff in ("'vektor'", "'integral'", "'ableitung'"):
        assert begriff in fehler[0], begriff


def test_flexionsfeste_muster():
    ueberall = ("Polynom-Division", "Polynom division", "Hypothesen-Test", "Test der Null-Hypothese",
                "Die Alternativhypothese", "Signifikanz-Niveau", "im Ablehnungsbereich",
                "Newton'sches Näherungsverfahren", "Verfahren von Newton",
                "mit partieller Integration", "der partiellen Integration", "partiell zu integrieren",
                "Kreuz-Produkt", "Vektorprodukts", "gebrochen rationale Funktion", "gebrochen–rational",
                "gebrochenrationale", "mit Stetigkeitskorrektur", "Mitternachtsformel")
    for text in ueberall:
        for klasse in (8, 11, 13):
            assert _fehler(klasse, text), (klasse, text)
    sek1 = ("Additions- oder Einsetzungsverfahren", "Additions-Verfahren", "Die Tangens-Funktion",
            "Der Umfangswinkel über der Sehne", "Peripheriewinkel", "Zentriwinkel", "Sehnenviereck",
            "Sehnentangentenwinkel")
    for text in sek1:
        assert _fehler(8, text), text
        assert _fehler(12, text) == [], text
    for text in ("Produkt-Regel", "Produkt- und Kettenregel", "Skalarprodukt", "Teilintegrale"):
        assert _fehler(11, text), text


def test_erlaubte_bedeutungen_bleiben_still():
    """Enger gefasste Muster: Woerter, die im Bestand in erlaubter Bedeutung vorkommen."""
    # Mittelpunktswinkel eines Kreisausschnitts (10-kreis-kugel #13) ist nicht der Zentriwinkelsatz
    assert _fehler(10, "Kreisbogen mit Mittelpunktswinkel \\(\\alpha\\) und Radius \\(r\\)") == []
    # 'Additions- und ...' ohne Verfahren ist Bruchrechnung, nicht das LGS-Verfahren
    assert _fehler(7, "Additions- und Subtraktionsaufgaben mit rationalen Zahlen") == []
    assert _fehler(8, "Addiere 3 und 5.") == []


def test_notation_ableitungsstrich_integral_vektorpfeil():
    for text in ("Bestimme \\(f'(2)\\).", "\\(g''(x) = 2\\)", "\\(\\int_0^1 x\\,dx\\)",
                 "\\(\\vec{a} + \\vec{b}\\)", "\\(\\overrightarrow{AB}\\)"):
        assert _fehler(9, text), text
    # Bildpunkt A'(4|2) und Strecke a' sind keine Ableitung
    assert _fehler(9, "Der Bildpunkt ist \\(A'(4 \\mid 2)\\), die Seite \\(a' = 6\\).") == []
    assert _fehler(11, "\\(\\int_0^1 x\\,dx\\) und \\(\\vec{a}\\)")
    assert _fehler(11, "Bestimme \\(f'(2)\\).") == []
    assert _fehler(12, "\\(f'(2)\\), \\(\\int_0^1 x\\,dx\\), \\(\\vec{a}\\)") == []


def test_e_funktion_und_ln_in_der_einfuehrungsphase():
    for text in ("\\(f(x) = e^x\\)", "\\(2 \\cdot e^{-x}\\)", "\\(x = \\ln(3)\\)"):
        assert _fehler(11, text), text
        assert _fehler(12, text) == [], text
    # 'e^' nach einem Buchstaben ist ein anderes Wort oder ein anderer Befehl
    assert _fehler(11, "\\(\\mathrm{Länge}^2\\) und \\(be^2\\)") == []


def test_trigonometrie_und_logarithmus_in_7_und_8():
    for text in ("Sinus", "Cosinus", "Kosinus", "\\(\\sin(30°)\\)", "\\(\\cos\\alpha\\)", "\\(\\tan\\alpha\\)",
                 "Logarithmus", "\\(\\log_2 8\\)", "Satz des Pythagoras"):
        assert _fehler(8, text), text
        assert _fehler(10, text) == [], text


def test_kreuzprodukt_als_notation():
    for text in ("\\(\\vec{u} \\times \\vec{v}\\)", "\\(\\vec{n}_1 \\times \\vec{n}_2\\)",
                 "\\(\\overrightarrow{AB} \\times \\overrightarrow{AC}\\)",
                 "\\(\\begin{pmatrix}1\\\\0\\\\0\\end{pmatrix} \\times \\begin{pmatrix}0\\\\1\\\\0\\end{pmatrix}\\)"):
        assert _fehler(12, text), text
    assert _fehler(12, "Eine \\(2 \\times 2\\)-Tabelle und \\(3 \\times 4 = 12\\)") == []


def test_dateibezogenes_zusatzmuster():
    """Tangens als Funktion ist in 10-cos-tan-funktion nicht KC, im Dreieck schon."""
    text = "\\(f(x) = \\tan(x)\\) hat die Periode \\(\\pi\\)."
    assert _fehler(10, text, datei="10-cos-tan-funktion.html")
    assert _fehler(10, text, datei="10-trig-rechtwinkliges-dreieck.html") == []
    assert _fehler(10, "\\(\\tanh(x)\\)", datei="10-cos-tan-funktion.html") == []


def test_warnwoerter_flexionsfest():
    for text in ("Leite auf.", "Leite die Funktion auf.", "Leite jeden Summanden einzeln auf: \\(x\\).",
                 "wird dabei aufgeleitet", "Die Aufleitung", "Tafelwerk", "Anstiegswinkel",
                 "Der Anstieg der Geraden", "den Anstieg einer Tangente", "in Scheitelform"):
        assert _warnung(12, text), text
    for text in ("Leite die Formel her und löse sie auf beiden Seiten nach x auf.",
                 "Leite ab. Schreibe das Ergebnis auf.", "Der Anstieg der Temperatur",
                 "Ein Anstieg von \\(15°\\)", "Setze in die Hesse-Normalform ein.",
                 "Die Leiter liegt in 4 m Höhe an der Wand auf."):
        assert _warnung(12, text) == [], text
    assert _warnung(12, "Wir leiten die Funktion auf.")
    # 'Anstiegswinkel der Tangente' ist ein Begriff, nicht zwei
    assert "anstieg (" not in _warnung(11, "Berechne den Anstiegswinkel der Tangente.")[0]
    assert _warnung(11, "wegen des Anstiegs der Tangente")


def test_normalform_nur_bis_zur_einfuehrungsphase():
    """Gemeint ist die 'Normalform' der quadratischen Funktion; in der QP heisst so die
    Normalenform der Geraden und Ebenen (Hesse-Normalform, 13-eA-abstaende)."""
    assert _warnung(9, "In der Normalform \\(f(x) = ax^2 + bx + c\\)")
    assert _warnung(13, "Gerade in Normalform: \\(2x - y + c = 0\\)") == []


def test_ausnahme_je_datei(monkeypatch):
    monkeypatch.setitem(lp.AUSNAHMEN, "11-x.html", {"stammfunktion"})
    assert _fehler(11, "Bilde eine Stammfunktion.", datei="11-x.html") == []
    assert _fehler(11, "Bilde eine Stammfunktion.", datei="11-y.html")
    assert _fehler(11, "Stammfunktion per Kettenregel", datei="11-x.html")


def test_spalte_ausserhalb_7_bis_13_ist_fehler():
    for klasse in (6, 14, None):
        fehler, _ = lp.pruefe(klasse, "x.html", [_a()])
        assert len(fehler) == 1 and "Spalte" in fehler[0], klasse


def test_unbekanntes_argument_bricht_ab(capsys):
    assert lp.main(["--strikt"]) == 2
    assert lp.main(["trainer"]) == 2
    assert "--strikt" in capsys.readouterr().out


def test_klassen_aus_index_liest_alle_trainer():
    klassen = lp.klassen_aus_index()
    assert klassen["7-rat-zahlen-rechnen.html"] == 7
    assert klassen["13-eA-abstaende.html"] == 13
    assert len(klassen) == 77
