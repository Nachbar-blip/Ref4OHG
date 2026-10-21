# Ref4OHG: Kerncurriculum Niedersachsen + Level-Durchgang — Umsetzungsplan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Alle Trainer von Ref4OHG dem niedersächsischen Kerncurriculum zuordnen (Umzüge, Ersatzthemen, Benennung) und jeden Trainer je Klasse nach der Level-Rubrik durchgehen, mit zweitem Prüfdurchgang je Block.

**Architecture:** Die Klassenzuordnung lebt allein in `index.html` (Spalten `.col-7` … `.col-13`); Dateinamen bleiben (QR-Links, localStorage-Schlüssel `spirale-<datei>`). Aufgaben liegen je Trainer als JS-Array `AUFGABEN` (36 Stück, 6 Stufen × 6) in `trainer/<datei>.html`, rein textbasiert (kein Bild, kein SVG). Gates: `tests/level_check.py`, neu `tests/lehrplan_check.py`, `tests/katex_check.py`, Playwright-Suite. Arbeit in Wellen je Klasse, ein Commit je Block, nichts wird gepusht.

**Tech Stack:** Vanilla HTML/JS + KaTeX, Python 3 (pytest, playwright, pillow, sympy), node (wertet die AUFGABEN-Arrays aus), Wolfram-MCP oder sympy zum Nachrechnen.

**Design:** `docs/plans/2026-10-10-lehrplan-nds-und-level-durchgang-design.md` (Umfang „A, voll“ freigegeben).
**Lehrplanabgleich:** `docs/audit/lehrplanabgleich-nds-2026-10-10.md` — dort stehen die KC-Kürzel (S1 … S17, G1 … G16), die hier benutzt werden, mit Zeilennummern in den KC-Dateien unter `C:\DevProjects\schule\Verwaltung\Lehrplaene\KC_extern\`.

---

## Verbindliche Regeln für jede Aufgabe

| Stufe | AFB | Kriterium | Verboten |
|---|---|---|---|
| 1 | I | ein Rechenschritt, Objekt gegeben, schöne Zahlen | Kontext |
| 2 | I | Standardverfahren, zwei Schritte | Kontext, Parameter |
| 3 | I | Klassenarbeits-Standard, Zwischenergebnis nötig | Formel im Text |
| 4 | II | Verfahren wählen / Modell aus Text aufstellen / Umkehraufgabe | Rechenweg im Text, angesagte Rechenart |
| 5 | III | zwei Verfahren kombinieren / Parameter aus zwei Bedingungen / Fehler im Rechenweg finden | gelieferte Formel, trivialisierende Stelle |
| 6 | III | Fallunterscheidung / Aussage begründet prüfen / Kl. 11–13 Abiturformat | Muster aus Stufe 1–3 mit Kontext |

Weitere Regeln (jede stammt aus einem echten Fehler):

- Stufe ≠ Teilthema. MC nur, wenn die Auswahl selbst die Leistung ist; in Stufe 5 und 6 höchstens 3 MC je Stufe.
- Jede Aufgabe ist **aus sich heraus verständlich**: kein „vorige Aufgabe“, „siehe oben“, „dieselbe Figur“. Die Engine wählt je Stufe zufällig.
- MC-Optionen werden gemischt: nie „Antwort B“ oder „die dritte Aussage“, sondern den Inhalt nennen. Alle vier Optionen ungefähr gleich lang; jeder Distraktor ist **als Aussage falsch**, nicht nur schwach begründet.
- Tipps ab Stufe 4 nennen den Weg, nicht den Lösungswert und nicht die fertige Gleichung.
- Mathe steht in `\(…\)` oder `$$…$$`; Dezimalkomma als `{,}` nur dort. Im Klartext „3,60 €“. Kein `<` direkt vor einem Buchstaben (innerHTML frisst den Text).
- Typografie: „…“ statt `"…"`, ` – ` statt ` -- `, echte Umlaute, Fettdruck als `<b>…</b>`.
- Numerische Aufgaben haben `toleranz`; sie ist so eng, dass der typische Fehlweg nicht durchgeht.
- Niedersächsische Wörter: Stammfunktion bilden (nicht „aufleiten“), Formelsammlung (nicht „Tafelwerk“), Steigung (nicht „Anstieg“), Scheitelpunktform, p-q-Formel, Umfangs-/Mittelpunktswinkel kommen im KC gar nicht vor.
- Aufgabenformen und Zahlenmuster dürfen aus dem Materialindex adaptiert werden (`schule/CLAUDE.md`): umformuliert, ohne Quellenangabe, kein Rohtext, nichts aus dem Index ins Repo.

Aufgabenformat:

```js
{ id: 19, level: 4, typ: "numerisch", frage: "…", loesung: 12.5, toleranz: 0.1, tipp: "…", loesungsweg: "…" },
{ id: 22, level: 4, typ: "mc", frage: "…", optionen: ["…", "…", "…", "…"], korrekt: 2, tipp: "…", loesungsweg: "…" },
```

**Schreiben in Trainer-Dateien — nie per Bash-Heredoc** (frisst Backslashes, auch quotiert), nie mit einem Werkzeug, das CRLF in LF wandelt. Zwei Wege:

- Einzelne Felder ändern: Datenmodul mit `AENDERUNGEN = [(datei, id, optionen|None, {feld: neuer_wert}), …]` per Write-Tool anlegen (Texte als Python-Raw-Strings, **ein** Backslash), dann
  `python tests/aufgaben_patch.py . <datenmodul.py> --dry` und ohne `--dry`.
- Ganze Aufgaben oder ganze Trainer ersetzen: JSON-Datei per Write-Tool anlegen, dann
  `python tests/aufgaben_setzen.py trainer/<datei>.html <daten.json>` (Task 0b).

Datenmodule und JSON liegen im Scratchpad, **nie in `trainer/`** (sonst landen sie im Dubletten-Vergleich).

## Prüfschleife je Block (bindend)

```bash
# im Ordner Trainer-Public/Ref4OHG; Server einmal je Sitzung im Hintergrund starten
python -m http.server 8765 --bind 127.0.0.1
python tests/level_check.py --strict                          # Exit 0, keine Warnung
python tests/lehrplan_check.py --strict trainer/<datei>.html … # Exit 0 für die Dateien des Blocks
python tests/katex_check.py trainer/<datei>.html …             # jede Zeile "ok"
python -m pytest tests/test_level_check.py tests/test_lehrplan_check.py tests/test_index.py -q -o addopts=""
cd tests && python -m pytest test_trainer.py -k "<datei-ohne-.html>" -q && cd ..
python tests/bogen.py . <scratchpad>/sicht/<block> <specs.txt> --tipp --weg --zeilen 3
```

`specs.txt` enthält je Zeile `datei.html:id` für jede geänderte Aufgabe. Die erzeugten PNG **mit dem Read-Tool ansehen** (Sichtprüfung, `schule/CLAUDE.md`) — erzeugen allein zählt nicht. Die Playwright-Suite läuft am Ende jeder Welle einmal vollständig (rund 35 Minuten).

**Zweiter Prüfdurchgang je Block:** Ein frischer Agent bekommt nur die ausgewerteten Aufgaben (`python tests/zeige.py . datei.html:id … > vorlage.txt`), die Rubrik und die KC-Fundstelle — nicht die Begründungen des Schreibenden. Er rechnet jede Zahl selbst nach (sympy oder Wolfram), prüft Distraktoren auf Wahrheit, Stufenniveau, Dubletten, Tipps und Sprache und meldet FEHLER / MANGEL / HINWEIS mit Änderungsvorschlag im Wortlaut. Befunde werden an der Aufgabe behoben und geprüft, bevor committet wird.

---

### Task 0a: Lehrplan-Gate `tests/lehrplan_check.py`

> **Stand:** Der unten abgedruckte Test- und Gate-Code zeigt den Stand des ersten Commits (`d548f9b`). Nach dem Review vom 2026-10-10 wurde das Gate überarbeitet (tag-sichere Bereinigung, Teilwortsuche, flexionsfeste Muster als Liste von (Regex, Anzeigename), Notation wie `f'(`, `\int`, `\vec`, `e^`, Zusatzmuster je Datei, alle Begriffe je Aufgabe). **Maßgeblich sind die Dateien `tests/lehrplan_check.py` und `tests/test_lehrplan_check.py`**, nicht der Abdruck. Exit 0 heißt nur „kein Listenbegriff“, nicht „KC-konform“.

**Files:**
- Create: `tests/lehrplan_check.py`
- Test: `tests/test_lehrplan_check.py`

**Step 1: Tests schreiben** (`tests/test_lehrplan_check.py`)

```python
# -*- coding: utf-8 -*-
"""Tests fuer das Lehrplan-Gate Niedersachsen (tests/lehrplan_check.py)."""
import lehrplan_check as lp


def _a(**kw):
    a = {"id": 1, "level": 1, "typ": "numerisch", "frage": "Berechne 2 + 3.",
         "tipp": "Zähle zusammen.", "loesungsweg": "2 + 3 = 5"}
    a.update(kw)
    return a


def test_vektor_in_der_sek1_ist_fehler():
    fehler, _ = lp.pruefe(9, "9-x.html", [_a(frage="Bestimme den Vektor von A nach B.")])
    assert len(fehler) == 1 and "vektor" in fehler[0]


def test_vektor_in_der_qualifikationsphase_ist_erlaubt():
    assert lp.pruefe(12, "12-x.html", [_a(frage="Bestimme den Vektor von A nach B.")]) == ([], [])


def test_hypothesentest_ist_in_jeder_spalte_fehler():
    for klasse in (12, 13):
        fehler, _ = lp.pruefe(klasse, "x.html", [_a(loesungsweg="Der Hypothesentest lehnt ab.")])
        assert fehler, klasse


def test_produktregel_erst_in_der_qualifikationsphase():
    assert lp.pruefe(11, "11-x.html", [_a(tipp="Nutze die Produktregel.")])[0]
    assert lp.pruefe(12, "12-x.html", [_a(tipp="Nutze die Produktregel.")]) == ([], [])


def test_additionsverfahren_in_7_bis_10():
    assert lp.pruefe(8, "8-x.html", [_a(frage="Löse mit dem Additionsverfahren.")])[0]
    assert lp.pruefe(12, "12-x.html", [_a(loesungsweg="Additionsverfahren: I + II.")]) == ([], [])


def test_optionen_werden_mitgelesen():
    a = _a(typ="mc", optionen=["Polynomdivision", "Ausklammern", "p-q-Formel", "Raten"], korrekt=1)
    assert lp.pruefe(11, "11-x.html", [a])[0]


def test_wort_aus_anderem_bundesland_ist_warnung():
    fehler, warnungen = lp.pruefe(12, "12-x.html", [_a(frage="Leite auf: \\(f(x) = 2x\\). (Aufleiten)")])
    assert fehler == [] and len(warnungen) == 1 and "aufleit" in warnungen[0]


def test_wortanfang_zaehlt_wortinneres_nicht():
    """Der Begriff muss am Wortanfang stehen: 'Vektoren' schlaegt an, 'Kollektor' nicht."""
    assert lp.pruefe(9, "9-x.html", [_a(frage="Vektoren addieren.")])[0]
    assert lp.pruefe(9, "9-x.html", [_a(frage="Der Kollektor heizt.")]) == ([], [])


def test_klassen_aus_index_liest_alle_trainer():
    klassen = lp.klassen_aus_index()
    assert klassen["7-rat-zahlen-rechnen.html"] == 7
    assert klassen["13-eA-abstaende.html"] == 13
    assert len(klassen) >= 76
```

**Step 2: Fehlschlag ansehen**

Run: `python -m pytest tests/test_lehrplan_check.py -q -o addopts=""`
Expected: Fehler beim Import (`No module named 'lehrplan_check'`).

**Step 3: Gate schreiben** (`tests/lehrplan_check.py`)

```python
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
# Einfuehrungsphase: nur Summen-, Faktor-, Potenzregel (G3); Produkt-/Kettenregel in der QP (G4)
_VOR_QP = {"produktregel", "kettenregel", "stammfunktion"}
VERBOTEN = {
    7: _SEK1 | _NIE | _SEK1_VERFAHREN | _VOR_QP | {"logarithm", "sinus", "kosinus", "pythagoras"},
    8: _SEK1 | _NIE | _SEK1_VERFAHREN | _VOR_QP | {"logarithm", "sinus", "kosinus", "pythagoras"},
    9: _SEK1 | _NIE | _SEK1_VERFAHREN | _VOR_QP,
    10: _SEK1 | _NIE | _SEK1_VERFAHREN | _VOR_QP,
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
```

**Step 4: Tests grün**

Run: `python -m pytest tests/test_lehrplan_check.py -q -o addopts=""`
Expected: `9 passed`.

**Step 5: Ausgangsmessung festhalten**

Run: `python tests/lehrplan_check.py > <scratchpad>/lehrplan_baseline.txt; tail -1 <scratchpad>/lehrplan_baseline.txt`
Die Zahl in den Commit-Text schreiben. Treffer, die das KC trägt (z. B. „Stammfunktion“ in einem EP-Trainer als Ausblick), **nicht** vorschnell als Ausnahme eintragen: erst in der Welle der Klasse entscheiden, mit KC-Beleg im Kommentar.

**Step 6: Commit**

```bash
git add tests/lehrplan_check.py tests/test_lehrplan_check.py
git commit -m "Lehrplan-Gate Niedersachsen: verbotene Begriffe je Klassenspalte (Ausgang: N Fehler)"
```

### Task 0b: Werkzeug `tests/aufgaben_setzen.py`

Ersetzt ganze Aufgaben oder das ganze Array aus einer JSON-Datei. `tests/aufgaben_patch.py`, `tests/bogen.py` und `tests/zeige.py` liegen schon im Repo (aus der Sitzung vom 2026-10-10 übernommen, dort an 139 Aufgaben erprobt).

**Files:**
- Create: `tests/aufgaben_setzen.py`
- Test: `tests/test_aufgaben_setzen.py`

**Step 1: Tests schreiben**

```python
# -*- coding: utf-8 -*-
"""Tests fuer tests/aufgaben_setzen.py: ersetzt Aufgaben bytegenau und verlustfrei."""
import json
import shutil
from pathlib import Path

import aufgaben_setzen as aset
import level_check as lk

VORLAGE = Path(__file__).resolve().parent.parent / "trainer" / "7-rat-zahlen-rechnen.html"


def _kopie(tmp_path):
    ziel = tmp_path / VORLAGE.name
    shutil.copy(VORLAGE, ziel)
    return ziel


def test_einzelne_aufgabe_wird_ersetzt_rest_bleibt(tmp_path):
    ziel = _kopie(tmp_path)
    vorher = lk.lade_aufgaben(ziel)
    neu = {"id": 20, "level": 4, "typ": "numerisch",
           "frage": "Berechne \\(\\frac{1}{2} + 0{,}5\\).", "loesung": 1, "toleranz": 0.01,
           "tipp": "Wandle zuerst um.", "loesungsweg": "\\(0{,}5 + 0{,}5 = 1\\) – fertig, sagt „man“."}
    aset.setze(ziel, [neu])
    nachher = lk.lade_aufgaben(ziel)
    assert [a for a in nachher if a["id"] == 20] == [neu]
    assert [a for a in nachher if a["id"] != 20] == [a for a in vorher if a["id"] != 20]


def test_zeilenenden_bleiben(tmp_path):
    ziel = _kopie(tmp_path)
    crlf_vorher = ziel.read_bytes().count(b"\r\n")
    lf_vorher = ziel.read_bytes().count(b"\n")
    neu = dict(lk.lade_aufgaben(ziel)[0], frage="Neue Frage?")
    aset.setze(ziel, [neu])
    roh = ziel.read_bytes()
    # entweder durchgehend CRLF oder durchgehend LF - wie vorher
    assert (roh.count(b"\r\n") == roh.count(b"\n")) == (crlf_vorher == lf_vorher)


def test_mc_und_numerisch_tauschbar(tmp_path):
    ziel = _kopie(tmp_path)
    neu = {"id": 1, "level": 1, "typ": "mc", "frage": "Was ist \\(-3 + 5\\)?",
           "optionen": ["\\(2\\)", "\\(-2\\)", "\\(8\\)", "\\(-8\\)"], "korrekt": 0,
           "tipp": "Zahlenstrahl.", "loesungsweg": "\\(-3 + 5 = 2\\)"}
    aset.setze(ziel, [neu])
    assert lk.lade_aufgaben(ziel)[0] == neu


def test_unbekannte_id_ist_fehler(tmp_path):
    ziel = _kopie(tmp_path)
    try:
        aset.setze(ziel, [{"id": 99, "level": 1, "typ": "numerisch", "frage": "x", "loesung": 1,
                           "toleranz": 0, "tipp": "x", "loesungsweg": "x"}])
    except ValueError as e:
        assert "99" in str(e)
    else:
        raise AssertionError("ValueError erwartet")


def test_kommandozeile(tmp_path):
    ziel = _kopie(tmp_path)
    daten = tmp_path / "neu.json"
    a = dict(lk.lade_aufgaben(ziel)[5], frage="Über die Kommandozeile gesetzt?")
    daten.write_text(json.dumps([a], ensure_ascii=False), encoding="utf-8")
    assert aset.main([str(ziel), str(daten)]) == 0
    assert lk.lade_aufgaben(ziel)[5]["frage"] == "Über die Kommandozeile gesetzt?"
```

**Step 2:** `python -m pytest tests/test_aufgaben_setzen.py -q -o addopts=""` → Importfehler.

**Step 3: Implementieren.** Vorgaben:

- `setze(pfad: Path, aufgaben: list) -> None`: je Aufgabe den Objektblock über `id:\s*<n>\s*,` finden (genau ein Treffer, sonst `ValueError` mit der id), vom öffnenden `{` davor bis zum schließenden `}` (Klammern zählen, Strings überspringen: `"(?:[^"\\]|\\.)*"`), und durch einen neu erzeugten Block ersetzen. Nachfolgendes Komma und Kommentare zwischen den Aufgaben bleiben stehen.
- Blockformat wie in der Datei: je Feld eine Zeile, Einrückung des ersetzten Blocks übernehmen, Feldreihenfolge `id, level, typ, bereich, frage, optionen, korrekt, loesung, toleranz, einheit, tipp, loesungsweg` (nur vorhandene Felder; unbekannte Felder sind ein `ValueError`), `optionen` einzeilig.
- Strings: `\` → `\\`, `"` → `\"`, Steuerzeichen maskiert; Zahlen wie in JSON; Zeilenende des **ersetzten Blocks** übernehmen (manche Trainer mischen CRLF und LF), bei einzeiligem Block das der Datei.
- Pflichtfelder prüfen (`id, level, typ, frage, tipp, loesungsweg`; bei `mc` `optionen` mit 2 bis 4 Einträgen und `korrekt` kleiner als deren Anzahl; bei `numerisch` `loesung` und `toleranz`), sonst `ValueError`. Ebenfalls `ValueError`: Texte mit `</script`, `<script` oder `<!--`; Texte in Quelltext-Form (`\\(` mit zwei Backslashes statt der ausgewerteten Form); leere Liste; doppelte id.
- Selbstkontrolle vor dem Schreiben: neuer Inhalt in eine Hilfsdatei neben dem Ziel, mit `lade_aufgaben` auswerten; gleiche id-Folge, gesetzte Aufgaben wie übergeben, alle anderen wie vorher – sonst `ValueError` und das Ziel bleibt unverändert; bei Erfolg `os.replace`. Die Hilfsdatei wird in jedem Fall entfernt.
- `main(argv)`: `aufgaben_setzen.py <trainer.html> <daten.json>`; JSON ist eine Liste von Aufgaben; gibt je Aufgabe `ok <datei> #<id>` aus, Rückgabe 0; bei einem Fehler (auch fehlende Datei) `FEHLER …` und Rückgabe 1.
- Lesen und Schreiben als Bytes (`read_bytes().decode("utf-8")`, `write_bytes`).

Die abgedruckten Tests zeigen den Stand des ersten Commits; maßgeblich ist `tests/test_aufgaben_setzen.py` (Regressionstests aus dem Review vom 2026-10-10).

**Step 4:** Tests grün (`5 passed`). Zusätzlich an einer echten Datei im Arbeitsbaum probieren und mit `git diff --stat` prüfen, dass nur die erwarteten Zeilen betroffen sind; danach `git checkout -- trainer/<datei>`.

**Step 5: Commit**

```bash
git add tests/aufgaben_setzen.py tests/test_aufgaben_setzen.py tests/aufgaben_patch.py tests/bogen.py tests/zeige.py
git commit -m "Werkzeug: Aufgaben bytegenau setzen und patchen, Bildbogen fuer die Sichtpruefung"
```

### Task 1: Übersicht — Umzüge, Qualifikationsphase, Titel

**Files:**
- Modify: `index.html`
- Create: `tests/test_index.py`

**Step 1: Tests schreiben** (`tests/test_index.py`)

```python
# -*- coding: utf-8 -*-
"""Struktur-Tests fuer index.html: Klassenzuordnung nach dem KC Niedersachsen, Filter, Titel."""
import html
import re
from pathlib import Path

from lehrplan_check import klassen_aus_index

ROOT = Path(__file__).resolve().parent.parent
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")

ERWARTET = {
    "7-kreise-umfang-flaeche.html": 9, "8-aehnlichkeit-streckung.html": 9,
    "8-gebrochen-rationale-einfuehrung.html": 10,
    "10-ganzrationale-funktionen.html": 11, "10-ableitung-einfuehrung.html": 11,
    "12-ebenen.html": 13,
}
# Trainer, deren Titel an den drei Stellen noch auseinanderlaufen. Die Liste schrumpft je Welle
# und ist am Ende leer (Task 9).
NOCH_UNEINHEITLICH = set()   # in Step 3 fuellen


def test_umzuege_nach_kc():
    s = klassen_aus_index()
    for datei, klasse in ERWARTET.items():
        assert s[datei] == klasse, f"{datei}: Spalte {s.get(datei)}, erwartet {klasse}"


def test_jeder_trainer_genau_einmal_im_index():
    dateien = sorted(p.name for p in (ROOT / "trainer").glob("*.html"))
    verlinkt = sorted(re.findall(r'href="trainer/([^"]+\.html)"', INDEX))
    assert verlinkt == dateien


def test_ea_trainer_tragen_klasse_und_badge():
    for m in re.finditer(r'<a class="([^"]*)" href="trainer/([^"]+)"(.*?)</a>', INDEX, re.S):
        if klassen_aus_index()[m.group(2)] == 13:
            assert "ea-only" in m.group(1) and "ea-badge" in m.group(3), m.group(2)


def test_filter_klasse_12_zeigt_die_ea_spalte():
    css = re.search(r"<style>(.*?)</style>", INDEX, re.S).group(1)
    assert not re.search(r"body\.filter-klasse-12\s+\.col-13\s*\{\s*display:\s*none", css)
    assert not re.search(r"body\.max-klasse-12[^{]*\.col-13\s*\{\s*display:\s*none", css)


def test_filter_ea_blendet_den_kern_nicht_aus():
    css = re.search(r"<style>(.*?)</style>", INDEX, re.S).group(1)
    assert "body.filter-ea .theme-row:not(.ea-only)" not in css


def test_spaltenkoepfe_der_qualifikationsphase():
    sichtbar = html.unescape(re.sub(r"<script.*?</script>|<style.*?</style>", "", INDEX, flags=re.S))
    assert "Qualifikationsphase (12/13)" in sichtbar
    assert "zusätzlich eA" in sichtbar


def _titel(datei: str):
    roh = (ROOT / "trainer" / datei).read_text(encoding="utf-8")
    seite = html.unescape(re.search(r"<title>(.*?) - Ref4OHG</title>", roh).group(1))
    kopf = re.search(r"THEMA_CONFIG\s*=\s*\{\s*name:\s*'([^']*)'", roh).group(1)
    m = re.search(r'href="trainer/' + re.escape(datei) + r'".*?theme-name">(.*?)</span>', INDEX, re.S)
    return seite, kopf, html.unescape(m.group(1))


def test_titel_an_allen_drei_stellen_gleich():
    abweichend = {d for d in klassen_aus_index() if len(set(_titel(d))) > 1}
    assert abweichend == NOCH_UNEINHEITLICH, (
        f"neu uneinheitlich: {sorted(abweichend - NOCH_UNEINHEITLICH)}; "
        f"inzwischen einheitlich (aus der Liste streichen): {sorted(NOCH_UNEINHEITLICH - abweichend)}")
```

**Step 2:** `python -m pytest tests/test_index.py -q -o addopts=""` → mehrere Fehlschläge (Umzüge, Filter, Spaltenköpfe).

**Step 3: `index.html` ändern** (Edit-Tool; `index.html` ist LF — vorher `file index.html` prüfen)

1. Die sechs `<a class="theme-row" …>…</a>`-Blöcke aus `ERWARTET` in die Zielspalte verschieben, jeweils ans Ende des fachlich passenden Abschnitts (`section-title`): Kreise → Spalte 9 „C · Geometrie“; Ähnlichkeit → 9 „C · Geometrie“; `8-gebrochen-rationale-einfuehrung` → 10, neuer Abschnitt „E · Grenzprozesse“ (Farbe `analysis`); ganzrationale Funktionen → 11 „B · Elementare Funktionenlehre“; Ableitung-Einführung → 11 „C · Ableitungen“ an erster Stelle; `12-ebenen` → 13 in den Geometrie-Abschnitt, Klasse `theme-row ea-only`, `<span class="ea-badge">eA</span>` wie bei den Nachbarn, Titeltext „Ebenen (Koordinatenform)“.
2. Verbinder-Zeichen (`&#x251C;` mittlere Zeile, `&#x2514;` letzte Zeile eines Abschnitts) in den betroffenen Abschnitten richtigstellen.
3. Spaltenkopf Spalte 12: „Qualifikationsphase (12/13) — gemeinsamer Kern“; Spalte 13: „Qualifikationsphase — zusätzlich eA“. Filterknöpfe: „Klasse 12“ → „Q-Phase Kern“, „Klasse 13“ → „Q-Phase eA“; `gaea`-Leiste: „Alle“, „Nur gA“, „eA“.
4. CSS: Regel `body.filter-klasse-12 .col-13 { display: none; }` löschen; in den `max-klasse-12`-Regeln `.col-13` nicht mehr ausblenden; Regel `body.filter-ea .theme-row:not(.ea-only) { display: none; }` löschen.
5. `NOCH_UNEINHEITLICH` füllen: den Test einmal laufen lassen, die gemeldete Menge („neu uneinheitlich“) als Ausgangsliste in `tests/test_index.py` eintragen.

**Step 4:** Tests grün. Dann Sichtprüfung der Übersicht: Server starten, mit Playwright je ein Screenshot ohne Filter, mit „Klasse 9“, „Q-Phase Kern“, „Nur gA“, „eA“ (Viewport 1400 × 2200, `full_page=True`) — **ansehen**. Geprüft wird: die sechs Trainer stehen in der neuen Spalte, die eA-Spalte ist unter „Q-Phase Kern“ sichtbar, keine verwaisten Verbinder.

**Step 5:** `cd tests && python -m pytest test_trainer.py -k "kreise-umfang or ebenen or ableitung-einfuehrung" -q` → grün. `python tests/lehrplan_check.py | tail -1` — die Zahl ändert sich durch die Umzüge; neue Zahl notieren.

**Step 6: Commit**

```bash
git add index.html tests/test_index.py
git commit -m "Uebersicht nach KC Niedersachsen: 6 Umzuege, Qualifikationsphase als Kern und eA-Zusatz"
```

### Task 2: e-Funktion-Tausch (vorgezogen)

Der Inhalt von `12-e-funktion` (a·bˣ, KC 9/10, S14) zieht in die neue Datei `10-exponentialfunktionen.html`; `12-e-funktion` bekommt die e-Funktion (G7, G4). Beides in **einem** Commit, weil das Level-Gate sonst 36 wortgleiche Fragen in zwei Trainern meldet.

**Files:**
- Create: `trainer/10-exponentialfunktionen.html`
- Modify: `trainer/12-e-funktion.html`, `index.html`, `tests/conftest.py` (Liste `TRAINER_FILES`), `tests/test_index.py`
- Create: `docs/plans/2026-10-10-kl12-kriterien.md` (erster Eintrag)

**Steps:**

1. `cp trainer/12-e-funktion.html trainer/10-exponentialfunktionen.html`; darin `THEMA_KEY = '10-exponentialfunktionen'`, `<title>Exponentialfunktionen - Ref4OHG</title>`, `THEMA_CONFIG.name = 'Exponentialfunktionen'` (bytegenau per Skript, nicht per Heredoc).
2. `index.html`: neue Zeile in Spalte 10, Abschnitt „C · Potenzen & Funktionenlehre“ (wird in Welle 10 umbenannt), `href="trainer/10-exponentialfunktionen.html" data-key="spirale-10-exponentialfunktionen"`, Titel „Exponentialfunktionen“. `tests/conftest.py`: Datei in `TRAINER_FILES` einsortieren.
3. 36 neue Aufgaben für `12-e-funktion` schreiben (JSON im Scratchpad), Titel überall „e-Funktion“, Kommentar in Zeile 2 der Datei: `<!-- Inhalt seit 2026-10: e-Funktion (KC QP gA, Lernbereich "Die e-Funktion"); der fruehere Inhalt a·b^x steht in 10-exponentialfunktionen.html -->`. Stufenaufbau:
   - L1: \(e^0\), \(e^1\), \(\ln e\), \(\ln 1\); Ableitung von \(e^x\) und \(3e^x\)
   - L2: Ableitung von \(a \cdot e^{kx}\) und \(e^{2x+1}\) (Kettenregel, lineare innere Funktion); \(e^x = 5\) nach \(x\) auflösen
   - L3: Produktregel bei \(x \cdot e^x\), \((2x+1)e^x\); Tangentensteigung; \(3e^{2x} = 12\)
   - L4: Extremstelle von \(x \cdot e^{-x}\) ohne Nennung des Verfahrens; Modell aus Text (Wirkstoffabbau, \(k\) aus der Halbwertszeit); Umkehraufgabe (\(k\) aus \(f'(0)\))
   - L5: \(f(x) = (ax + b)e^x\) aus zwei Bedingungen; Fehler in einer Ableitung finden (innere Ableitung vergessen); \(2^x = e^{x \ln 2}\) und Ableitung von \(2^x\)
   - L6: Aussage prüfen („\(a \cdot e^{kx}\) hat nie eine Extremstelle“); Wendestelle und Wendetangente im Abiturformat; Fallunterscheidung nach dem Vorzeichen von \(k\)
   Nur Kettenregel mit **linearer** innerer Funktion (gA, G4). ln als Funktion ist fakultativ (G7) — ln nur als Werkzeug zum Lösen.
4. `python tests/aufgaben_setzen.py trainer/12-e-funktion.html <scratchpad>/12-e-funktion.json`
5. Kriterien-Datei anlegen (Format siehe „Kriterien-Datei“ unten), Prüfschleife, zweiter Prüfdurchgang für `12-e-funktion`, Sichtprüfung aller 36 Aufgaben.
6. Commit: `git commit -m "e-Funktion-Tausch: 12-e-funktion ist jetzt e-Funktion (QP gA), a·b^x zieht nach 10-exponentialfunktionen"`

---

## Wellen (Task 3 bis 9)

Jede Welle läuft in Blöcken von höchstens sechs Trainern; ein Commit je Block, die volle Playwright-Suite am Ende der Welle.

### Kriterien-Datei

Je Klasse `docs/plans/2026-10-10-klN-kriterien.md`. Je Trainer ein Abschnitt:

```markdown
## 9-pythagoras — Satz des Pythagoras
KC: 9/10 „Entdeckungen an rechtwinkligen Dreiecken und Ähnlichkeit“ (S11, SI Z. 2251).
Gelesen: alle 36 Aufgaben. Urteil Lehrplan: passt / Abweichungen: …

| id | Stufe | Kriterium laut Rubrik | Befund | Änderung |
|---|---|---|---|---|
| 19 | 4 | Verfahren wählen | Rechenart angesagt | Frage neu: … |
| 25 | 5 | zwei Verfahren | trägt | — |
```

Jede Aufgabe ab Stufe 4 bekommt eine Zeile, Stufe 1–3 nur bei Befund. „trägt“ ist ein zulässiges Ergebnis — nichts ändern, um etwas geändert zu haben.

### Verfahren „Durchgang“ (jeder Trainer)

1. Alle 36 Aufgaben ausgewertet lesen: `python tests/zeige.py . <datei>.html:1 … <datei>.html:36`.
2. Lehrplan: gegen die KC-Fundstelle aus dem Abgleich lesen (Kürzel dort nachschlagen, KC-Zeilen selbst öffnen). Der Abgleich hat 44 Trainer nur per Stichprobe gesehen — eigene Funde in die Kriterien-Datei.
3. Stufen: jede Aufgabe ab Stufe 4 gegen die Rubrik. Prüffragen: Verlangt Stufe 4 etwas anderes als Stufe 3? Stufe 5 etwas anderes als Stufe 4? Ist der Stoff für **diesen** Jahrgang in Niedersachsen zu früh oder zu spät (die Stufe-5/6-Blöcke stammen großteils aus Sachsen-Anhalt)?
4. Durchgehend, alle Stufen: Tipp ab Stufe 4 ohne fertige Gleichung; Distraktoren als Aussage falsch; Lösungsweg zeigt den Weg; Aufgabe aus sich heraus verständlich; Wörter aus anderen Bundesländern; sinngleiche Paare innerhalb des Trainers und zu den Nachbarn der Spalte.
5. Änderungen schreiben (Datenmodul oder JSON im Scratchpad), jede neue oder geänderte Zahl nachrechnen (sympy oder Wolfram), einsetzen.
6. Titel an allen drei Stellen angleichen, Datei aus `NOCH_UNEINHEITLICH` streichen.
7. Kriterien-Datei, Prüfschleife, zweiter Prüfdurchgang, Sichtprüfung, Commit.

### Verfahren „Ersatz“ (ganzer Trainer)

Wie „Durchgang“, aber alle 36 Aufgaben neu nach dem unten vorgegebenen Stufenaufbau; `<title>`, `THEMA_CONFIG.name`, Index-Text und Abschnitt anpassen; Kommentar in Zeile 2: `<!-- Dateiname historisch (QR-Links); Inhalt seit 2026-10: <Thema>, KC <Beleg> -->`. Vor dem Schreiben den KC-Lernbereich **im Wortlaut** lesen (Zeilen aus dem Abgleich) und den Stufenaufbau daran prüfen — das KC geht vor, die Liste hier ist ein Vorschlag. Brauchbare Altaufgaben, die KC-gedeckt sind, wandern in den passenden Nachbartrainer statt in den Papierkorb (in der Kriterien-Datei vermerken).

### Verfahren „Teil-Ersatz“

Nur die genannten Aufgaben neu (ids behalten ihre Stufe), der Rest „Durchgang“. Die Aufgaben-IDs aus dem Abgleich stammen aus einer Volltextsuche — vor dem Ersetzen an der ausgewerteten Aufgabe bestätigen.

### Verfahren „Umzug“

„Durchgang“, zusätzlich Stufe 1–3 auf das Vorwissen der Zielklasse prüfen und gegen die neuen Nachbarn abgrenzen (keine sinngleichen Aufgaben in zwei Trainern derselben Spalte).

---

### Task 3: Welle Klasse 7 (9 Trainer)

**Create:** `docs/plans/2026-10-10-kl7-kriterien.md`

- **Block 7A** (Durchgang): `7-rat-zahlen-rechnen`, `7-prozent-grundaufgaben`, `7-prozent-anwendungen-zins`, `7-zuordnungen-proportional`, `7-wahrscheinlichkeit`
- **Block 7B**: `7-terme-vereinfachen`, `7-gleichungen-linear`, `7-dreiecke-konstruktionen`, `7-koerper-volumen`

Besonderheiten:
- `7-koerper-volumen` — Teil-Ersatz: Zylinder (#12, 20, 22, 24, 25, 27, 28, 30, 33, 35) und Pyramide (#31, 32, 34, 36) sind 9/10 (S13). Ersatz: Prisma mit Dreiecks- und Trapezgrundfläche — Netz erkennen, Oberfläche, Volumen, Rückwärtsrechnen (S5). Titel „Körper — Netze & Prismen“.
- `7-dreiecke-konstruktionen` — Stufe 1–3 sind Dreiecksarten und Winkelsumme (5/6, S1). Ersatz durch Grundkonstruktionen und Kongruenz auf Stufe 1–3 (S7): welche Stücke legen ein Dreieck fest, Kongruenzsatz zuordnen, Konstruierbarkeit (Dreiecksungleichung). Thales gehört in `8-kreise-winkel` (Task 4).
- `7-wahrscheinlichkeit` #32 (Erwartungswert) ist fakultativ — bleibt, in der Kriterien-Datei vermerken.
- Lesart Kl. 7: L4 Rechenart selbst wählen; L5 zweischrittige Sachaufgabe ohne Weg oder Fehler in vorgelegter Rechnung; L6 Umkehraufgabe, „Stimmt die Behauptung?“, Sonderfall.

Commits: `Level-Durchgang Kl. 7 Block A: …`, `… Block B: …`; danach volle Suite.

### Task 4: Welle Klasse 8 (8 Trainer)

**Create:** `docs/plans/2026-10-10-kl8-kriterien.md`

- **Block 8A** (Durchgang): `8-terme-binomische-formeln`, `8-gleichungen-linear`, `8-lgs-zwei-variablen`, `8-lineare-funktionen-grund`, `8-lineare-funktionen-anwendungen`, `8-zufallsversuche-mehrstufig`
- **Block 8B** (Ersatz): `8-koerperberechnung`, `8-kreise-winkel`

Besonderheiten:
- `8-lgs-zwei-variablen` #13, #14, Option in #5: „Additionsverfahren“ ersetzen (KC nur Einsetzungs- und Gleichsetzungsverfahren, S9). Parameter-LGS sind KC-gedeckt (SI Z. 2143) und bleiben.
- `8-terme-binomische-formeln` #32: „… die in Klasse 9 gebraucht wird“ streichen.
- **Ersatz `8-koerperberechnung` → „Flächeninhalte & Prismen“** (S5, SI Z. 1974–1980), Abschnitt „C · Geometrie“:
  - L1: Flächeninhalt von Dreieck, Parallelogramm mit gegebener Grundseite und Höhe
  - L2: Trapez; Umfang; Volumen des Prismas aus Grundfläche und Höhe
  - L3: zusammengesetzte Figur zerlegen; Prisma mit Dreiecksgrundfläche (Grundfläche als Zwischenergebnis)
  - L4: fehlende Höhe aus dem Flächeninhalt; Formel selbst wählen (welche Höhe gehört zu welcher Seite); Term für einen Flächeninhalt aufstellen
  - L5: Fehler finden (Seite statt Höhe eingesetzt); Oberfläche eines Trapezprismas; Wirkung einer Verdopplung von Grundseite oder Höhe
  - L6: Behauptung prüfen („gleicher Umfang, also gleicher Flächeninhalt“); Trapezformel aus zwei Dreiecken begründen; Scherung
  Die Prisma-Altaufgaben (#1, 7, 9, 11, 15) dürfen bleiben, wenn sie in den Aufbau passen.
- **Ersatz `8-kreise-winkel` → „Thales & besondere Linien“** (S7, SI Z. 2059–2063). Die Thales-Aufgaben #19–22, #33, #36 bleiben (Stufe prüfen). Umkreis und Inkreis sind fakultativ — höchstens auf Stufe 6.
  - L1: Mittelsenkrechte, Winkelhalbierende, Seitenhalbierende, Höhe benennen; Winkel am Halbkreis
  - L2: Winkel im Thales-Dreieck mit der Winkelsumme; Eigenschaft der Punkte auf Mittelsenkrechte und Winkelhalbierender
  - L3: Ortslinien zuordnen (Kreis, Mittelsenkrechte, Winkelhalbierende, Parallele); Schritte einer Grundkonstruktion ordnen
  - L4: Ortslinien-Sachaufgabe („gleich weit von A und B und 3 cm von C“); Umkehrung des Thales-Satzes anwenden
  - L5: Fehler in einer Konstruktionsbeschreibung; Thales und gleichschenkliges Dreieck kombiniert
  - L6: Begründung des Thales-Satzes; Anzahl der Punkte bei zwei Ortslinien-Bedingungen (Fallunterscheidung)
  Kein Pythagoras (9/10), keine Umfangs- oder Mittelpunktswinkel (Gate).

### Task 5: Welle Klasse 9 (12 Trainer)

**Create:** `docs/plans/2026-10-10-kl9-kriterien.md`

- **Block 9A**: `9-reelle-zahlen-quadratwurzeln`, `9-binomische-formeln-vertieft` (Inhalt Potenzgesetze), `9-potenzen-wurzeln`, `9-quadratische-funktionen`, `9-quadratische-gleichungen`, `9-quadratische-anwendungen`
- **Block 9B**: `9-pythagoras`, `9-strahlensaetze`, `8-aehnlichkeit-streckung` (Umzug), `9-raumgeometrie`, `7-kreise-umfang-flaeche` (Umzug)
- **Block 9C** (Ersatz): `9-daten-zufall-boxplot`

Besonderheiten:
- `9-quadratische-funktionen`: „Scheitelform“ → „Scheitelpunktform“, „Normalform“ → „allgemeine Form“ (SI Z. 1241); die faktorisierte Form und der Wechsel der Formen (S12, SI Z. 2304) sind eine Lücke — auf Stufe 4–6 aufnehmen.
- `9-quadratische-gleichungen` #19, #23: „Mitternachtsformel“ → „Lösungsformel“ (Gate).
- `9-potenzen-wurzeln` #26, 28, 31 (Wurzel- und Umkehrfunktion): EP bzw. fakultativ — ersetzen durch Rechnen mit rationalen Exponenten und Logarithmieren als Umkehroperation (S14, SI Z. 2406).
- `8-aehnlichkeit-streckung`: Titel „Ähnlichkeit“; „zentrische Streckung“ als Begriff nicht im KC — als „Vergrößern/Verkleinern mit dem Faktor k“ fassen; gegen `9-strahlensaetze` abgrenzen (keine sinngleichen Aufgaben).
- `7-kreise-umfang-flaeche`: gegen `10-kreis-kugel` Stufe 1–3 abgrenzen; Bogenlänge und Kreisausschnitt (S13) dürfen hier stehen.
- `9-pythagoras`: Höhen- und Kathetensatz fehlen (Satzgruppe, S11) — je zwei Aufgaben auf Stufe 4–6.
- **Ersatz `9-daten-zufall-boxplot` → „Baumdiagramme & Vierfeldertafeln“** (S10, SI ab Z. 2199 im Wortlaut lesen), Abschnitt „D · Daten & Zufall“:
  - L1: fehlendes Feld und Randsumme einer Vierfeldertafel ergänzen
  - L2: Tafel mit relativen Häufigkeiten vervollständigen; Pfadwahrscheinlichkeit im Baum
  - L3: Baum in Tafel überführen und zurück; Anteil „unter den …“ aus der Tafel
  - L4: Tafel aus einem Text aufstellen; umgekehrtes Baumdiagramm
  - L5: Fehler finden (Bedingung und Ereignis vertauscht); Testaufgabe in natürlichen Häufigkeiten (positiv getestet — wie viele sind krank?)
  - L6: Behauptung prüfen; Abhängigkeit über den Vergleich von Anteilen beurteilen; fehlende Angabe als Parameter
  Schreibweise der bedingten Wahrscheinlichkeit nur, wenn das KC sie in 9/10 nennt — sonst in Worten.

### Task 6: Welle Klasse 10 (12 Trainer)

**Create:** `docs/plans/2026-10-10-kl10-kriterien.md`

- **Block 10A** Trigonometrie: `10-trig-rechtwinkliges-dreieck`, `10-trig-anwendungen`, `10-kreis-kugel`, `10-potenzfunktionen` (Ersatz)
- **Block 10B** periodische Zusammenhänge: `10-trig-einheitskreis`, `10-sinusfunktion`, `10-sin-cos-parameter`, `10-cos-tan-funktion` (Teil-Ersatz)
- **Block 10C** Wachstum und Grenzprozesse: `10-wachstum-linear-exponentiell`, `10-exponentialfunktionen` (seit Task 2), `10-potenzen-ganzzahlig` (Ersatz), `8-gebrochen-rationale-einfuehrung` (Ersatz, Umzug)

Besonderheiten:
- Abschnitte in Spalte 10 neu ordnen: „A · Trigonometrie“, „B · Periodische Zusammenhänge“, „C · Wachstum“, „D · Kreis & Kugel“, „E · Grenzprozesse“.
- `10-trig-anwendungen` #20, #34: „Anstieg“ → „Steigung“.
- `10-cos-tan-funktion` — Teil-Ersatz #13–24 (Tangensfunktion, nicht im KC, S15): Kosinusfunktion — Werte, Kosinus als verschobener Sinus, Grad und Bogenmaß, Symmetrie, Nullstellen. Titel „Kosinusfunktion“.
- `10-exponentialfunktionen`: Durchgang als Klasse-10-Trainer (kam aus Spalte 12): Parametervariation und Funktionsgleichung aus zwei Punkten (S14, SI Z. 2415–2421) sind der Kern; gegen `10-wachstum-linear-exponentiell` abgrenzen.
- **Ersatz `10-potenzfunktionen` → „Sinussatz & Kosinussatz“** (S11, SI Z. 2260), Abschnitt A:
  - L1: Welcher Satz passt (SSS, SWS, WSW)? Einsetzen mit fertiger Skizzenbeschreibung
  - L2: Seite mit dem Sinussatz; Seite mit dem Kosinussatz (SWS)
  - L3: Winkel mit dem Kosinussatz (SSS); Winkel mit dem Sinussatz, Rest über die Winkelsumme
  - L4: Satz selbst wählen; Vermessungsaufgabe aus Text; Umkehraufgabe
  - L5: zwei Schritte (erst Kosinus-, dann Sinussatz); Fehler finden (zweite Lösung beim Sinussatz übersehen)
  - L6: Aussage prüfen (Kosinussatz enthält den Pythagoras); Anzahl der Dreiecke bei SSW (Fallunterscheidung)
- **Ersatz `10-potenzen-ganzzahlig` → „Begrenztes Wachstum & iterative Modelle“** (S14, SI Z. 2410–2413), Abschnitt C:
  - L1: einen Schritt einer rekursiven Vorschrift rechnen (linear, exponentiell); Grenze G ablesen
  - L2: zwei bis drei Schritte; Zuwachs als Anteil des Rests \(G - B\)
  - L3: Tabelle fortsetzen; Wachstumsart aus einer Tabelle erkennen; iterativ gegen explizit
  - L4: Modell aus Text aufstellen (Abkühlung, Medikament mit täglicher Dosis); Grenze bestimmen
  - L5: Anteil und Grenze aus zwei Messwerten; Fehler finden (Zuwachs zum Bestand statt zum Rest proportional); Überlagerung von linearem und exponentiellem Anteil
  - L6: Behauptung prüfen („die Grenze wird nach endlicher Zeit erreicht“); Startwert über oder unter G (Fallunterscheidung); Modellvergleich
  Ohne e-Funktion und ohne Ableitung (Gate). Die Altaufgaben zu negativen Exponenten, die reines Rechnen sind (S14), gehen nach `9-binomische-formeln-vertieft`, soweit dort nicht schon sinngleich vorhanden.
- **Ersatz `8-gebrochen-rationale-einfuehrung` → „Grenzprozesse & Zahlbereiche“** (S16, SI Z. 2509–2517; laut SI Z. 1494 Klasse 10), Abschnitt E:
  - L1: rational oder irrational; \(\frac{1}{x}\) für große \(x\) auswerten; Intervallschachtelung lesen
  - L2: ein Heron-Schritt; periodische Dezimalzahl als Bruch
  - L3: zwei Heron-Schritte; \(0{,}\overline{9} = 1\) über Brüche; Grenzverhalten von \(\frac{1}{x}\) und \(a \cdot b^x\) mit \(b < 1\) benennen
  - L4: Wertetabelle eines Näherungsverfahrens deuten; Einfluss des Startwerts; passendes Verfahren wählen
  - L5: Fehler in einer Argumentation finden („\(0{,}\overline{9}\) ist kleiner als 1“); zwei Grenzprozesse vergleichen (ab wann kleiner als 0,001)
  - L6: Behauptung prüfen („Heron liefert nach endlich vielen Schritten \(\sqrt{2}\) exakt“); Irrationalitätsbegründung; Annäherung an \(\pi\) über Vielecke
  Altaufgaben #11 und #14 sind laut Abgleich anschlussfähig.

### Task 7: Welle Klasse 11, Einführungsphase (14 Trainer)

**Create:** `docs/plans/2026-10-10-kl11-kriterien.md`

- **Block 11A** Statistik und Funktionenlehre: `11-statistik-lagemasse`, `11-statistik-streumasse`, `11-funktionsbegriff`, `11-funktionen-potenzfunktionen`, `11-funktionen-ganzrational`, `10-ganzrationale-funktionen` (Umzug)
- **Block 11B** Ableitung: `10-ableitung-einfuehrung` (Umzug), `11-grenzwerte` (Ersatz), `11-ableitungsregeln` (Teil-Ersatz), `11-tangenten-normalen`
- **Block 11C** Anwendungen: `11-monotonie-kruemmung`, `11-extrempunkte-wendepunkte`, `11-extremwertaufgaben`, `11-kurvendiskussion`

Besonderheiten:
- Stufe 6 hat ab hier Abiturformat (hilfsmittelfreier Teil): begründen, beurteilen, Zusammenhang herstellen.
- `11-statistik-lagemasse`: „Modus“ → „Modalwert“, „Mittelwert“ → „arithmetisches Mittel“ (G1).
- `10-ganzrationale-funktionen` #34 enthält \(f'\) — in Spalte 11 jetzt zulässig; gegen `11-funktionen-ganzrational` abgrenzen (ein Trainer Grundlagen: Grad, Globalverhalten, Symmetrie; der andere Nullstellen und Faktorisieren).
- `11-funktionsbegriff` #14, 17, 20, 27 (Verkettung) und #15, #18 („Anstieg“): Verkettung bleibt propädeutisch, „Anstieg“ → „Steigung“.
- `11-funktionen-potenzfunktionen` #29: offene Entscheidung des Autors (dritte Wurzel für negative x) — **nicht ändern, beim Autor nachfragen**, bevor der Block committet wird.
- `11-ableitungsregeln` — Teil-Ersatz #19, 25, 28, 29, 30, 34, 35, 36 (Produktregel, \(e^x\), ln; QP): Summen- und Faktorregel mit \(\sin\), \(\cos\), \(\sqrt{x}\), \(x^{-n}\); Sachprobleme; Parameter aus Steigungsbedingungen (G3).
- `11-tangenten-normalen` #23 (\(e^x\)) ersetzen; #20, #26 „Anstiegswinkel“ → „Steigungswinkel“.
- `11-kurvendiskussion` #11 und Lösungsweg #21: Polynomdivision ersetzen (Nullstellen über Ausklammern, Substitution oder gegebene Faktorisierung, G2).
- **Ersatz `11-grenzwerte` → „Ableitungsfunktion“** (G3, GO Z. 1730–1761). Die Trainer sind textbasiert: Graphen werden über Wertetabellen, Vorzeichentabellen oder eine Beschreibung in Worten gegeben.
  - L1: Vorzeichen von \(f'\) aus dem beschriebenen Verlauf von \(f\); Ableitungen von \(\sin\), \(\cos\), \(\sqrt{x}\) nennen
  - L2: \(\frac{1}{x}\) und \(\sqrt{x}\) als Potenz ableiten; \(a \sin x + b \cos x\)
  - L3: Differenzenquotient von \(x^2\) an einer Stelle vereinfachen (h-Methode); Aussage „wo \(f\) steigt, ist \(f' > 0\)“ anwenden
  - L4: aus einer Vorzeichentabelle von \(f'\) auf Extremstellen von \(f\) schließen; Stelle mit vorgegebener Steigung bei \(\sqrt{x}\) oder \(\frac{1}{x}\)
  - L5: Fehler in einer h-Methoden-Rechnung finden; \(f\) aus zwei Bedingungen an \(f'\); Eigenschaften von \(f\) aus beschriebenem \(f'\)-Graphen
  - L6: Aussage prüfen („\(f'(x_0) = 0\), also Extremstelle“); Fallunterscheidung; Abiturformat
  Die Altaufgaben #7–10 (Globalverhalten) gehen nach `10-ganzrationale-funktionen`, soweit dort nicht sinngleich vorhanden.

### Task 8: Welle Qualifikationsphase Kern (13 Trainer)

**Fortschreiben:** `docs/plans/2026-10-10-kl12-kriterien.md`

- **Block 12A** Analysis: `12-steckbriefaufgaben`, `12-stammfunktionen`, `12-bestimmtes-integral`, `12-flaechenberechnung`, `12-e-funktion` (seit Task 2: nur Gegenlesen), `12-wachstum-begrenzt`
- **Block 12B** Geometrie: `12-vektoren-grundlagen`, `12-geraden-raum`, `12-skalarprodukt`
- **Block 12C** Stochastik: `12-stoch-grundlagen` (Teil-Ersatz), `12-stoch-bedingte-wahrscheinlichkeit`, `12-stoch-binomialverteilung`, `12-stoch-sigma-umgebungen`

Besonderheiten:
- `12-stammfunktionen` #1, 2, 3, 6, 8, 18, 25: „Aufleiten“ → „Stammfunktion bilden“. Stammfunktionen mit der Kettenregel nur bei linearer innerer Funktion (G6, GO Z. 1851).
- `12-bestimmtes-integral`: „Bestand aus Änderungsrate rekonstruieren“ und „Integral als Grenzwert von Produktsummen“ (G6, GO Z. 1835–1836) sind eine Lücke — auf Stufe 4–6 aufnehmen. Integralfunktion (#25, #31) ist für gA fakultativ: bleibt, vermerken.
- `12-vektoren-grundlagen` #35: Kreuzprodukt im Tipp ersetzen (Gate).
- `12-geraden-raum` #27, #35 (Abstand paralleler Geraden, Punkt–Gerade: eA): ersetzen durch **Ebenen in Parameterform** (G8, GO Z. 1927) — aufstellen aus drei Punkten, Punktprobe, Spurpunkte. Titel „Geraden & Ebenen in Parameterform“.
- `12-stoch-binomialverteilung` #27: „Tafelwerk“ → „Formelsammlung“.
- `12-stoch-sigma-umgebungen`: bleibt in der Kernspalte (Design 1d). Zuschnitt auf gA: Prognoseintervalle „grafisch oder tabellarisch“ und die Frage, ob ein Wert mit einer Stichprobe **verträglich** ist (G9, GO Z. 1990–1992). Aufgaben, die σ-Umgebungen für Anteile rechnen (eA, GO Z. 2283), auf Stufe 6 beschränken oder nach `13-eA-normalverteilung`/`13-eA-beurteilende-statistik` geben.
- `12-stoch-grundlagen` — Teil-Ersatz Stufe 3–6 (24 Aufgaben) → **Zufallsgrößen** (G9, GO Z. 1974–1978); Stufe 1–2 so anpassen, dass sie darauf hinführen (Wahrscheinlichkeitsverteilung ablesen, vervollständigen). Titel „Zufallsgrößen & Erwartungswert“.
  - L3: Erwartungswert aus einer Verteilung; Varianz und Standardabweichung
  - L4: Verteilung aus einem Spieltext aufstellen; ist das Spiel fair?; Einsatz für ein faires Spiel
  - L5: fehlende Wahrscheinlichkeit und Auszahlung aus Erwartungswert und Summe 1; Fehler finden (Varianz mit Standardabweichung verwechselt)
  - L6: Aussage prüfen („ein faires Spiel gewinnt man in der Hälfte der Fälle“); zwei Spiele mit gleichem Erwartungswert und verschiedener Streuung beurteilen; Abiturformat

### Task 9: Welle Qualifikationsphase eA (9 Trainer)

**Create:** `docs/plans/2026-10-10-kl13-kriterien.md`

- **Block 13A** Analysis: `13-eA-integralrechnung-vertieft` (Teil-Ersatz), `13-eA-funktionenscharen`, `13-eA-wachstumsmodelle`
- **Block 13B** Geometrie: `12-ebenen` (Umzug), `13-eA-ebenen-lagebeziehungen`, `13-eA-abstaende`, `13-eA-tangenten-kreise`
- **Block 13C** Stochastik: `13-eA-normalverteilung`, `13-eA-beurteilende-statistik` (Teil-Ersatz)

Besonderheiten:
- Koordinaten einheitlich \(x_1, x_2, x_3\) in allen Geometrie-Trainern der Spalten 12 und 13 (`13-eA-ebenen-lagebeziehungen` nutzt x, y, z).
- `12-ebenen`: Titel „Ebenen (Koordinatenform, eA)“; #13–18 Kreuzprodukt ersetzen (Normalenvektor über das Gleichungssystem aus zwei Skalarprodukten); #33 Ebenenschar ersetzen; gegen `13-eA-ebenen-lagebeziehungen` und `13-eA-abstaende` abgrenzen.
- `13-eA-ebenen-lagebeziehungen` #22, Tipp #15: Kreuzprodukt ersetzen.
- `13-eA-abstaende`: Kopfzeile mit „(eA)“; Kugel (#27, #34) fakultativ — bleibt.
- `13-eA-tangenten-kreise`: bleibt als fakultativer Trainer (Design 1d). Im Index-Titel „(fakultativ)“ ergänzen.
- `13-eA-wachstumsmodelle`: „DGL“ im Titel ausschreiben („Differentialgleichungen“, G11).
- `13-eA-integralrechnung-vertieft` — Teil-Ersatz #25, 26, 27, 29, 30, 36 (nichtlineare Substitution) und #31, 32, 35 (partielle Integration) → **Rotationsvolumen** (GO Z. 2048), **uneigentliche Integrale als Grenzwerte** (GO Z. 2050), **Integralfunktion** und ihre Abgrenzung zur Stammfunktion (GO Z. 2033). Titel überall „Integralrechnung (vertieft, eA)“.
- `13-eA-normalverteilung` #28–30 (Stetigkeitskorrektur): im KC nicht genannt — ersetzen durch „diskret gegen stetig“ und Histogramm-Deutung (GO Z. 2274–2278).
- `13-eA-beurteilende-statistik` — Teil-Ersatz der Hypothesentest-Aufgaben (#19–26, 28, 29, 31–33, 35, 36; Gate) → **Konfidenzintervalle** (G14, GO Z. 2283–2284): Intervall für \(p\) aus \(h\) und \(n\) über σ-Umgebungen, Einfluss von \(n\) und Sicherheitswahrscheinlichkeit, Prognose- gegen Konfidenzintervall, „mit der Stichprobe verträglich“. Stufe 6: Aussage prüfen („\(p\) liegt mit 95 % Wahrscheinlichkeit im Intervall“), Stichprobenumfang für eine geforderte Breite, Abiturformat. Keine Wörter Hypothese, Signifikanz, Ablehnungsbereich.

### Task 10: Abschluss

1. `python tests/level_check.py --strict` → Exit 0 ohne Warnung; `python tests/lehrplan_check.py --strict` → Exit 0; `python tests/katex_check.py` über alle 77 Trainer; `cd tests && python -m pytest -q` → grün.
2. `tests/test_index.py`: `NOCH_UNEINHEITLICH` ist leer; Test `test_alle_77_trainer` ergänzen (`len(klassen_aus_index()) == 77`).
3. Nachmessung in `docs/audit/lehrplanabgleich-nds-2026-10-10.md` als neuer Abschnitt „Abschluss (Datum)“: je Befund des Abgleichs erledigt / bewusst nicht (mit Verweis auf Design 1d); Kennzahl „Tipps ab Stufe 4 mit fertiger Gleichung“ neu zählen (Ausgang 425 von 1368).
4. `docs/plans/2026-09-19-level-progression-plan-ENTWURF.md`: Status „abgelöst durch 2026-10-10-Plan“; der dort als offen geführte Schritt 5 ist überholt.
5. Dem Autor melden, nicht selbst erledigen: `Ref4OHG_QR.docx` braucht einen Eintrag für `10-exponentialfunktionen`; offene Entscheidungen aus Design 1d (`13-eA-tangenten-kreise`, `11-funktionen-potenzfunktionen` #29).
6. Commit: `git commit -m "KC Niedersachsen und Level-Durchgang abgeschlossen: Nachmessung, Plan-Status"`. **Kein Push** ohne ausdrückliche Freigabe des Autors.
