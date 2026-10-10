# -*- coding: utf-8 -*-
"""Lehrplan-Gate Niedersachsen: meldet Begriffe und Schreibweisen, die das Kerncurriculum in der
Klassenspalte nicht kennt (Sek I Gymnasium; gymnasiale Oberstufe 2018). Die Klassenzuordnung
wird aus index.html gelesen. Belege: docs/audit/lehrplanabgleich-nds-2026-10-10.md.

Das Gate ist eine Begriffsliste, kein Lehrplanabgleich: Exit 0 heisst nur "keiner der gelisteten
Begriffe kommt vor", NICHT "KC-konform". Inhalte, die ohne ihr Stichwort auskommen (Zylinder in
Klasse 7, nichtlineare Substitution, Verkettung), sieht es nicht - das bleibt Sache des Durchgangs.

Aufruf:  python tests/lehrplan_check.py [--strict] [trainer/x.html ...]
         --strict: Exit 1, sobald ein Fehler oder eine Warnung gemeldet wird.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from level_check import lade_aufgaben, ROOT, TRAINER_DIR  # noqa: E402

INDEX = ROOT / "index.html"
FELDER = ("frage", "loesungsweg", "tipp")

# Nur echte Tags verschwinden. level_check.normalisiere() loescht alles zwischen '<' und '>' und
# frass damit bei Ungleichungen ganze Saetze samt verbotener Woerter (Review 2026-10-10:
# 13-eA-beurteilende-statistik #19, 'Nullhypothese' im Tipp). <br> ist ein Zeilenumbruch und wird
# Leerraum; <b>, <sub> ... stehen auch mitten im Wort und fallen ersatzlos weg. Hinter dem
# Tag-Namen duerfen nur Attribute (name="wert") stehen - sonst waere '\(a<b\), ... \(a>b\)' ein Tag.
_ATTRIBUTE = r"""(?:\s+[a-zA-Z-]+\s*=\s*(?:"[^"<>]*"|'[^'<>]*'))*\s*/?>"""
_UMBRUCH = re.compile(r"<br" + _ATTRIBUTE, re.I)
_TAG = re.compile(r"</?(?:b|i|u|em|strong|sub|sup|span)" + _ATTRIBUTE, re.I)


def bereinige(text) -> str:
    """Sichtbarer Text eines Feldes: ohne Tags und weiche Trennstriche, Leerraum einfach.
    Gross/klein bleibt stehen (die Wortmuster suchen ohnehin ohne Ruecksicht darauf), damit die
    Notationsmuster f'( von A'( unterscheiden koennen."""
    t = str(text or "").replace("­", "").replace("&shy;", "").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", _TAG.sub("", _UMBRUCH.sub(" ", t))).strip()


def _regeln(*paare) -> list:
    """[(Regex, Anzeigename)]. Gesucht wird als Teilwort und ohne Ruecksicht auf gross/klein;
    wo die Schreibung zaehlt (Notation), steht (?-i:...) im Muster."""
    return [(re.compile(muster, re.I), name) for muster, name in paare]


_B = r"[\s\-–]*"          # Fuge im zusammengesetzten Wort: nichts, Leerraum, Binde- oder Halbgeviertstrich
_KEIN_BUCHSTABE = r"(?![A-Za-z])"
_VEKTOR = r"(?:\\vec\{[^{}]*\}(?:_\{?\w+\}?)?|\\overrightarrow\{[^{}]*\}|\\end\{pmatrix\})"

# Im KC fuer das Gymnasium an keiner Stelle (Volltextsuche beider KC-Dateien)
_NIE = _regeln(
    (rf"polynom{_B}division", "polynomdivision"),
    (rf"hypothesen{_B}test", "hypothesentest"),
    (rf"null{_B}hypothese", "nullhypothese"),
    (rf"alternativ{_B}hypothese", "alternativhypothese"),
    (rf"signifikanz{_B}niveau", "signifikanzniveau"),
    (r"ablehnungsbereich", "ablehnungsbereich"),
    (r"newton", "newton-verfahren"),
    (r"partiell\w*\s+(?:zu\s+)?integr", "partielle integration"),
    (rf"vektor{_B}produkt|kreuz{_B}produkt", "kreuzprodukt"),
    # \times nur zwischen zwei Vektoren - '2 \times 2' und '3 \times 4 = 12' bleiben still
    (rf"{_VEKTOR}\s*\\times\s*\\(?:vec|overrightarrow|begin\{{pmatrix\}})", r"\times zwischen vektoren"),
    (rf"gebrochen{_B}rational", "gebrochen-rational"),
    (r"mitternachtsformel", "mitternachtsformel"),
    (r"stetigkeitskorrektur", "stetigkeitskorrektur"),
)
# Ableitung und Integral erst in der Sek II (SI Z. 1488); Vektoren erst in der QP (G8).
# 7/8: nur Einsetzungs- und Gleichsetzungsverfahren (S9); 9/10: nur Sinus- und Kosinusfunktion (S15).
# "Produktregel" fehlt hier mit Absicht: in 7-10 heisst so die Pfadregel bzw. das Wurzelgesetz
# (Ausgangsmessung 2026-10-10: alle 8 Treffer dort waren Fehlalarm).
_SEK1 = _regeln(
    (r"vektor", "vektor"),
    (r"ableitung", "ableitung"),
    (r"integral", "integral"),
    (r"skalarprodukt", "skalarprodukt"),
    (r"determinante", "determinante"),
    (r"kettenregel", "kettenregel"),
    (r"stammfunktion", "stammfunktion"),
    # 'Additions- und Subtraktionsaufgaben' ist Bruchrechnung: nur mit '...verfahren' dahinter
    (r"additions-?\s*verfahren|additions-\s*(?:oder|und)\s+\w*verfahren", "additionsverfahren"),
    (rf"tangens{_B}funktion", "tangensfunktion"),
    (r"peripheriewinkel|umfangswinkel", "peripheriewinkel"),
    # ohne 'Mittelpunktswinkel': so heisst auch der Winkel des Kreisausschnitts (10-kreis-kugel #13)
    (r"zentriwinkel", "zentriwinkel"),
    (r"sehnentangentenwinkel", "sehnentangentenwinkel"),
    (r"sehnenviereck", "sehnenviereck"),
    # f'(2), g''(x) - aber nicht der Bildpunkt A'(4|2): Funktionsnamen sind klein und stehen allein
    (r"(?-i:(?<![A-Za-z\\])[a-z]'{1,2}\s*\()", "f'( (ableitungsstrich)"),
    (rf"\\int{_KEIN_BUCHSTABE}", r"\int"),
    (rf"\\vec{_KEIN_BUCHSTABE}|\\overrightarrow", r"\vec"),
)
_KLASSE_7_8 = _regeln(
    (r"logarithm", "logarithmus"),
    (r"sinus", "sinus/kosinus"),          # trifft auch Kosinus und Cosinus
    (r"pythagoras", "pythagoras"),
    (rf"\\(?:sin|cos|tan){_KEIN_BUCHSTABE}", r"\sin/\cos/\tan"),
    (rf"\\(?:log|ln|lg){_KEIN_BUCHSTABE}", r"\log/\ln"),
)
# Einfuehrungsphase: nur Summen-, Faktor-, Potenzregel (G3); Produkt-/Kettenregel, e-Funktion und
# ln erst in der QP (G4). Der Ableitungsstrich ist hier erlaubt.
_EINFUEHRUNGSPHASE = _regeln(
    (rf"produkt{_B}regel", "produktregel"),
    (r"kettenregel", "kettenregel"),
    (r"stammfunktion", "stammfunktion"),
    (r"vektor", "vektor"),
    (r"integral", "integral"),
    (r"skalarprodukt", "skalarprodukt"),
    (rf"\\int{_KEIN_BUCHSTABE}", r"\int"),
    (rf"\\vec{_KEIN_BUCHSTABE}|\\overrightarrow", r"\vec"),
    # e^x, e^{-x}; nicht nach Buchstabe oder Backslash (anderes Wort, anderer Befehl)
    (r"(?-i:(?<![A-Za-z\\])e\^)", "e^ (e-funktion)"),
    (rf"\\ln{_KEIN_BUCHSTABE}", r"\ln"),
)
VERBOTEN = {
    7: _NIE + _SEK1 + _KLASSE_7_8,
    8: _NIE + _SEK1 + _KLASSE_7_8,
    9: _NIE + _SEK1,
    10: _NIE + _SEK1,
    11: _NIE + _EINFUEHRUNGSPHASE,
    12: _NIE,
    13: _NIE,
}
# Zusatzmuster je Datei: was nur in diesem Trainer lehrplanfremd ist.
DATEI_ZUSATZ = {
    # Tangens als Funktion ist nicht KC (S15: nur Sinus- und Kosinusfunktion); in den
    # Dreieckstrainern derselben Spalte ist \tan erlaubt.
    "10-cos-tan-funktion.html": _regeln((rf"\\tan{_KEIN_BUCHSTABE}", r"\tan")),
}
# Ausnahmen je Datei als Menge von Anzeigenamen, jeweils mit Beleg.
# Nur ergaenzen, wenn das KC den Begriff dort traegt.
AUSNAHMEN = {}

# Woerter aus anderen Bundeslaendern: Warnung, kein Fehler
_WARN = _regeln(
    # 'leite ... auf' nur als Verbform (nicht 'Leiter') und mit 'auf' am Satz- oder Teilsatzende
    # ('auf beiden Seiten' zaehlt nicht)
    (r"aufleit|aufgeleitet|\bleite(?:t|n|st)?\s(?:[^.]{0,40}\s)?auf(?=\s*(?:[.:;,!?)]|$))", "aufleiten"),
    (r"tafelwerk", "tafelwerk"),
    (r"anstiegswinkel", "anstiegswinkel"),
    # nur das Wort selbst ('Anstieg', 'Anstiegs'): 'Anstiegswinkel der Tangente' hat seine eigene Regel
    (r"anstieg(?:e?s)?\s+(?:der|einer|des|eines)\s+(?:gerade|tangente|sekante|funktion|graph)",
     "anstieg (steigung)"),
    (r"scheitelform", "scheitelform"),
)
# 'Normalform' der quadratischen Funktion (Audit Z. 297). Ab der QP heisst so die Normalenform von
# Gerade und Ebene (Hesse-Normalform, 13-eA-abstaende) - dort keine Warnung.
_WARN_BIS_EP = _regeln((r"normalform", "normalform"))
WARNUNGEN = {k: _WARN + (_WARN_BIS_EP if k <= 11 else []) for k in VERBOTEN}


def klassen_aus_index() -> dict:
    """{dateiname: klasse} aus den .col-N-Bloecken von index.html."""
    html = INDEX.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r'<div class="col col-(\d+)">(.*?)(?=<div class="col col-|\Z)', html, re.S):
        for h in re.findall(r'href="trainer/([^"]+\.html)"', m.group(2)):
            out[h] = int(m.group(1))
    return out


def _begriffe(regeln: list, texte: list) -> str:
    """Anzeigenamen aller Regeln, die in einem der Texte anschlagen: \"'a', 'b'\" oder \"\"."""
    return ", ".join(f"'{name}'" for rx, name in regeln if any(rx.search(t) for t in texte))


def pruefe(klasse: int, name: str, aufgaben: list):
    """Liefert (fehler, warnungen) als Listen von Strings - je Aufgabe hoechstens eine Zeile,
    die alle getroffenen Begriffe nennt. Jedes Feld und jede Option wird fuer sich durchsucht."""
    if klasse not in VERBOTEN:
        return [f"{name}: Spalte {klasse} kennt das Gate nicht (nur 7 bis 13)"], []
    ausnahmen = AUSNAHMEN.get(name, set())
    hart = [r for r in VERBOTEN[klasse] + DATEI_ZUSATZ.get(name, []) if r[1] not in ausnahmen]
    fehler, warnungen = [], []
    for a in aufgaben:
        texte = [bereinige(a.get(k)) for k in FELDER] + [bereinige(o) for o in (a.get("optionen") or [])]
        f, w = _begriffe(hart, texte), _begriffe(WARNUNGEN[klasse], texte)
        if f:
            fehler.append(f"{name} #{a['id']} L{a['level']}: {f} (Spalte {klasse}: nicht im KC Niedersachsen)")
        if w:
            warnungen.append(f"{name} #{a['id']} L{a['level']}: {w} (Wort aus einem anderen Bundesland)")
    return fehler, warnungen


def main(argv):
    unbekannt = [x for x in argv if x != "--strict" and not x.endswith(".html")]
    if unbekannt:
        print(f"Unbekanntes Argument: {' '.join(unbekannt)}")
        print("Aufruf: python tests/lehrplan_check.py [--strict] [trainer/x.html ...]")
        return 2
    strict = "--strict" in argv
    dateien = [Path(x) for x in argv if x.endswith(".html")] or sorted(TRAINER_DIR.glob("*.html"))
    dateien = [d if d.is_absolute() else ROOT / d for d in dateien]
    klassen = klassen_aus_index()
    fehler, warnungen = [], []
    for d in dateien:
        if d.name not in klassen:
            fehler.append(f"{d.name}: nicht in index.html eingeordnet")
            continue
        f, w = pruefe(klassen[d.name], d.name, lade_aufgaben(d))
        fehler += f
        warnungen += w
    for b in fehler:
        print(f"FEHLER  {b}")
    for b in warnungen:
        print(f"warn    {b}")
    print(f"== Lehrplan-Gate: {len(fehler)} Fehler, {len(warnungen)} Warnungen in {len(dateien)} Trainern")
    return 1 if ((fehler or warnungen) and strict) else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
