# -*- coding: utf-8 -*-
"""Ersetzt MC-Optionen (und wahlweise frage/loesungsweg/tipp) einzelner Aufgaben.
   python mc_patch.py <root> <datenmodul.py> [--dry]

Das Datenmodul definiert AENDERUNGEN = [(datei, id, optionen, extras), ...]:
  optionen: Liste mit 4 Eintraegen in Quelltext-Reihenfolge, None = unveraendert (oder None
            fuer "Optionen gar nicht anfassen")
  extras:   dict feld -> neuer Gesamtwert (frage, loesungsweg, tipp)
Alle Texte in AUSGEWERTETER Form (ein Backslash). Layout und Zeilenenden bleiben unberuehrt,
ersetzt wird nur der Inhalt der String-Literale."""
import importlib.util
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
root = Path(sys.argv[1])
dry = "--dry" in sys.argv
spec = importlib.util.spec_from_file_location("daten", sys.argv[2])
daten = importlib.util.module_from_spec(spec)
spec.loader.exec_module(daten)

JS_STRING = r'"((?:[^"\\]|\\.)*)"'


def dekodiere(s):
    def ein(m):
        if m.group(1) not in '\\"':
            raise ValueError(f"unerwartete Escape-Folge \\{m.group(1)} in {s[:60]!r}")
        return m.group(1)
    return re.sub(r"\\(.)", ein, s)


def kodiere(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def sichtbar(s):
    return len(re.sub(r"\\[a-zA-Z]+|[\\{}$()]", "", str(s)))


fehler = 0
noch_lang = 0
for datei, nr, optionen, extras in daten.AENDERUNGEN:
    p = root / "trainer" / datei
    roh = p.read_bytes().decode("utf-8")
    ids = list(re.finditer(rf"\bid:\s*{nr}\s*,", roh))
    if len(ids) != 1:
        print(f"FEHLER {datei} #{nr}: id {len(ids)}-mal gefunden"); fehler += 1; continue
    start = ids[0].end()
    naechste = re.search(r"\bid:\s*\d+\s*,", roh[start:])
    ende = start + naechste.start() if naechste else len(roh)
    ersetzungen = []          # (von, bis, neuer kodierter Inhalt)
    bericht = ""
    if optionen is not None:
        kopf = re.compile(r"\boptionen:\s*\[").search(roh, start, ende)
        if not kopf:
            print(f"FEHLER {datei} #{nr}: optionen nicht gefunden"); fehler += 1; continue
        zu = roh.index("]", kopf.end())
        # ']' kann in einem String stehen (Intervalle) -> bis zum ersten ']' ausserhalb von Strings
        pos, strings = kopf.end(), []
        while True:
            m = re.compile(r"\s*,?\s*" + JS_STRING).match(roh, pos)
            if not m:
                break
            strings.append(m)
            pos = m.end()
        if len(strings) != 4 or len(optionen) != 4 or not re.match(r"\s*\]", roh[pos:pos + 40]):
            print(f"FEHLER {datei} #{nr}: {len(strings)} Optionen gelesen"); fehler += 1; continue
        km = re.compile(r"\bkorrekt:\s*(\d)").search(roh, start, ende)
        korrekt = int(km.group(1))
        neu = []
        for m, o in zip(strings, optionen):
            alt = dekodiere(m.group(1))
            if o is None:
                neu.append(alt)
            else:
                neu.append(o)
                ersetzungen.append((m.start(1), m.end(1), kodiere(o)))
        if len(set(neu)) != 4:
            print(f"FEHLER {datei} #{nr}: doppelte Option"); fehler += 1; continue
        l = [sichtbar(o) for o in neu]
        andere = max(x for i, x in enumerate(l) if i != korrekt)
        lang = l[korrekt] > andere * 1.3
        noch_lang += lang
        marke = "LANG" if lang else ("knapp" if l[korrekt] > andere * 1.15 else "ok   ")
        bericht = f"{marke} {l} richtig={l[korrekt]} max.andere={andere}"
    for feld, wert in (extras or {}).items():
        m = re.compile(rf"\b{feld}:\s*{JS_STRING}").search(roh, start, ende)
        if not m:
            print(f"FEHLER {datei} #{nr}: Feld {feld} nicht gefunden"); fehler += 1; continue
        ersetzungen.append((m.start(1), m.end(1), kodiere(wert)))
        bericht += f" +{feld}"
    for von, bis, inhalt in sorted(ersetzungen, reverse=True):
        roh = roh[:von] + inhalt + roh[bis:]
    if not dry:
        p.write_bytes(roh.encode("utf-8"))
    print(f"{datei} #{nr}: {bericht}")
print(f"{'PROBELAUF - ' if dry else ''}{len(daten.AENDERUNGEN)} Aufgaben, {fehler} Fehler, "
      f"{noch_lang} weiterhin zu lang")
sys.exit(1 if fehler else 0)
