# -*- coding: utf-8 -*-
"""Sichtpruefung vieler Aufgaben in wenigen Bildern: ein Browser, je Aufgabe ein Ausschnitt
   (Karte, wahlweise mit Tipp und Loesungsweg), zu Boegen mit zwei Spalten zusammengesetzt.
   python bogen.py <root> <praefix> <specs.txt> [--tipp] [--weg] [--zeilen N] [--breite PX]"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

root = Path(sys.argv[1])
praefix = sys.argv[2]
specs = Path(sys.argv[3]).read_text(encoding="utf-8").split()
args = sys.argv[4:]
mit_tipp, mit_weg = "--tipp" in args, "--weg" in args
zeilen = int(args[args.index("--zeilen") + 1]) if "--zeilen" in args else 5
breite = int(args[args.index("--breite") + 1]) if "--breite" in args else 700
sys.path.insert(0, str(root / "tests"))
import bild as b  # noqa: E402

teile = []
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    seite = browser.new_page(viewport={"width": breite, "height": 900})
    for spec in specs:
        name, nr = spec.split(":")
        nr = int(nr)
        seite.goto(f"{b.BASE}/trainer/{name}", wait_until="networkidle")
        lvl = seite.evaluate("id => AUFGABEN.find(a => a.id === id).level", nr)
        andere = seite.evaluate(
            "([l, id]) => AUFGABEN.filter(a => a.level === l && a.id !== id).map(a => a.id)", [lvl, nr])
        seite.evaluate(
            "([l, ids]) => localStorage.setItem('spirale-ref4ohg-' + THEMA_KEY,"
            " JSON.stringify({level: l, answered: ids}))", [lvl, andere])
        seite.reload(wait_until="networkidle")
        b._katex_abwarten(seite)
        if mit_tipp:
            knopf = seite.query_selector(".btn-tipp")
            if knopf:
                knopf.click()
                seite.wait_for_timeout(250)
        if mit_weg:
            b._loesungsweg_aufdecken(seite)
            b._katex_abwarten(seite)
            seite.wait_for_timeout(350)
        # Ausschnitt: von der Karte bis zum unteren Rand von Feedback/Tipp
        box = seite.evaluate("""() => {
            const els = ['.aufgabe-karte', '#feedback', '.feedback', '.tipp-box']
                .flatMap(s => [...document.querySelectorAll(s)])
                .filter(e => e.offsetParent !== null && e.getBoundingClientRect().height > 0);
            const r = els.map(e => e.getBoundingClientRect());
            return {top: Math.min(...r.map(x => x.top)) + window.scrollY,
                    bottom: Math.max(...r.map(x => x.bottom)) + window.scrollY};
        }""")
        pfad = Path(f"{praefix}-tmp.png")
        seite.screenshot(path=str(pfad), full_page=True)
        img = Image.open(pfad).convert("RGB")
        if "--kopf" in args:
            box["top"] = 0
        img = img.crop((0, max(0, int(box["top"]) - 6), img.width, min(img.height, int(box["bottom"]) + 6)))
        kopf = Image.new("RGB", (img.width, 22), "black")
        ImageDraw.Draw(kopf).text((6, 4), f"{name} #{nr}  L{lvl}", fill="white")
        teil = Image.new("RGB", (img.width, img.height + 22), "white")
        teil.paste(kopf, (0, 0))
        teil.paste(img, (0, 22))
        teile.append(teil)
    browser.close()

# zwei Spalten, Spalten werden nacheinander gefuellt und sind etwa gleich hoch
je_bogen = zeilen * 2
for n in range(0, len(teile), je_bogen):
    gruppe = teile[n:n + je_bogen]
    links, rechts = gruppe[:(len(gruppe) + 1) // 2], gruppe[(len(gruppe) + 1) // 2:]
    h = max(sum(t.height for t in links), sum(t.height for t in rechts) if rechts else 0)
    bogen = Image.new("RGB", (breite * 2, h), "white")
    for spalte, x in ((links, 0), (rechts, breite)):
        y = 0
        for t in spalte:
            bogen.paste(t, (x, y))
            y += t.height
    ziel = Path(f"{praefix}-{n // je_bogen + 1:02d}.png")
    bogen.save(ziel)
    print(ziel.name, bogen.size, len(gruppe))
