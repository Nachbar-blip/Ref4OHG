# -*- coding: utf-8 -*-
"""Zeigt einzelne Aufgaben ausgewertet (wie die Engine sie sieht).
   python zeige.py <ref4ohg-root> datei.html:35 datei2.html:1 ..."""
import sys
from pathlib import Path

root = Path(sys.argv[1])
sys.path.insert(0, str(root / "tests"))
import level_check as lk  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
cache = {}
for spec in sys.argv[2:]:
    name, nr = spec.split(":")
    if name not in cache:
        cache[name] = lk.lade_aufgaben(root / "trainer" / name)
    a = next(x for x in cache[name] if x["id"] == int(nr))
    print(f"===== {name} #{a['id']} L{a['level']} {a['typ']}")
    print("FRAGE:", a.get("frage"))
    if a["typ"] == "mc":
        for i, o in enumerate(a["optionen"]):
            print(f"   [{i}]{'*' if i == a['korrekt'] else ' '} {o}")
    else:
        print("LOESUNG:", a.get("loesung"), "tol", a.get("toleranz"), "einheit", a.get("einheit"))
    print("TIPP:", a.get("tipp"))
    print("WEG:", a.get("loesungsweg"))
    print()
