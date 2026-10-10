# -*- coding: utf-8 -*-
"""Lehrplan-Gate Niedersachsen: meldet Begriffe, die das Kerncurriculum in der Klassenspalte
nicht kennt (Sek I Gymnasium; gymnasiale Oberstufe 2018). Die Klassenzuordnung wird aus
index.html gelesen. Belege: docs/audit/lehrplanabgleich-nds-2026-10-10.md.

Aufruf:  python tests/lehrplan_check.py [--strict] [trainer/x.html ...]
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from level_check import lade_aufgaben, normalisiere, ROOT, TRAINER_DIR  # noqa: E402

INDEX = ROOT / "index.html"

# Ableitung und Integral erst in der Sek II (SI Z. 1488); Vektoren erst in der QP (G8)
_SEK1 = {"vektor", "ableitung", "integral", "skalarprodukt", "determinante"}
# Im KC fuer das Gymnasium an keiner Stelle (Volltextsuche beider KC-Dateien)
_NIE = {"polynomdivision", "hypothesentest", "signifikanzniveau", "nullhypothese",
        "newton-verfahren", "newtonverfahren", "partielle integration", "partiell integr",
        "vektorprodukt", "kreuzprodukt", "gebrochen-rational", "gebrochenrational",
        "mitternachtsformel"}
# 7/8: nur Einsetzungs- und Gleichsetzungsverfahren (S9); 9/10: nur Sinus- und Kosinusfunktion (S15)
_SEK1_VERFAHREN = {"additionsverfahren", "tangensfunktion", "peripheriewinkel", "zentriwinkel",
                   "sehnentangentenwinkel"}
# Einfuehrungsphase: nur Summen-, Faktor-, Potenzregel (G3); Produkt-/Kettenregel in der QP (G4).
# Nur fuer Spalte 11: in 7-10 heisst "Produktregel" die Pfadregel bzw. das Wurzelgesetz
# (Ausgangsmessung 2026-10-10: alle 8 Treffer dort waren Fehlalarm).
_VOR_QP = {"produktregel", "kettenregel", "stammfunktion"}
VERBOTEN = {
    7: _SEK1 | _NIE | _SEK1_VERFAHREN | {"logarithm", "sinus", "kosinus", "pythagoras"},
    8: _SEK1 | _NIE | _SEK1_VERFAHREN | {"logarithm", "sinus", "kosinus", "pythagoras"},
    9: _SEK1 | _NIE | _SEK1_VERFAHREN,
    10: _SEK1 | _NIE | _SEK1_VERFAHREN,
    11: (_NIE | _VOR_QP | {"vektor", "integral", "skalarprodukt"}),
    12: _NIE,
    13: _NIE,
}
# Ausnahmen je Datei, jeweils mit Beleg. Nur ergaenzen, wenn das KC den Begriff dort traegt.
AUSNAHMEN = {}
# Woerter aus anderen Bundeslaendern: Warnung, kein Fehler
WARNWOERTER = {"aufleit", "tafelwerk", "anstiegswinkel"}
FELDER = ("frage", "loesungsweg", "tipp")


def klassen_aus_index() -> dict:
    """{dateiname: klasse} aus den .col-N-Bloecken von index.html."""
    html = INDEX.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r'<div class="col col-(\d+)">(.*?)(?=<div class="col col-|\Z)', html, re.S):
        for h in re.findall(r'href="trainer/([^"]+\.html)"', m.group(2)):
            out[h] = int(m.group(1))
    return out


def _muster(woerter) -> re.Pattern:
    # Wortanfang muss stimmen, Endung frei: "vektor" trifft "Vektoren", nicht "Kollektor".
    return re.compile(r"(?<![a-zäöüß])(" + "|".join(map(re.escape, sorted(woerter))) + ")")


def pruefe(klasse: int, name: str, aufgaben: list):
    """Liefert (fehler, warnungen) als Listen von Strings."""
    verboten = VERBOTEN.get(klasse, set()) - AUSNAHMEN.get(name, set())
    hart, weich = _muster(verboten) if verboten else None, _muster(WARNWOERTER)
    fehler, warnungen = [], []
    for a in aufgaben:
        text = normalisiere(" ".join(str(a.get(k) or "") for k in FELDER)
                            + " " + " ".join(str(o) for o in (a.get("optionen") or [])))
        m = hart.search(text) if hart else None
        if m:
            fehler.append(f"{name} #{a['id']} L{a['level']}: '{m.group(1)}' "
                          f"(Spalte {klasse}: nicht im KC Niedersachsen)")
        w = weich.search(text)
        if w:
            warnungen.append(f"{name} #{a['id']} L{a['level']}: '{w.group(1)}' "
                             f"(Wort aus einem anderen Bundesland)")
    return fehler, warnungen


def main(argv):
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
    sys.exit(main(sys.argv[1:]))
