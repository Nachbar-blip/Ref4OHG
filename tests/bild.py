# -*- coding: utf-8 -*-
"""Screenshot eines Trainers oder des Index fuer die Sichtpruefung.

    python tests/bild.py trainer/7-vierecke.html            -> tests/reports/bild-7-vierecke.png
    python tests/bild.py trainer/7-vierecke.html --level 5  -> tests/reports/bild-7-vierecke-L5.png
    python tests/bild.py index.html                         -> tests/reports/bild-index.png
    python tests/bild.py trainer/7-vierecke.html --aufgabe 33 -> genau Aufgabe 33
    python tests/bild.py trainer/7-vierecke.html --aufgabe 33 --loesungsweg -> mit Loesungsweg

Braucht einen lokalen Server im Projektordner: python -m http.server 8765
(KaTeX kommt per CDN, die Trainer laden spirale-engine.js relativ).
Vorbild: Mathe/Trainer-Lokal/Lehrer/KA-Generator/blattbild.py - das PNG wird angesehen, nicht gemessen.
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = os.environ.get("REF4OHG_BASE_URL", "http://127.0.0.1:8765")


def _katex_abwarten(seite, ms=4000):
    """Wartet, bis KaTeX gesetzt hat - sonst zeigt das Bild rohes LaTeX."""
    try:
        seite.wait_for_function(
            "() => !window.katex || document.querySelectorAll('.katex').length > 0",
            timeout=ms)
    except Exception:
        seite.wait_for_timeout(800)


def _loesungsweg_aufdecken(seite):
    """Antwortet bewusst falsch, damit das Feedback mit dem Loesungsweg erscheint.
    Mehrere Fehler der Wellen Kl. 10-12 steckten im Loesungsweg (abgebrochener String,
    '<' vor Buchstabe, Optionsverweis) und waren im Bild der Aufgabenseite unsichtbar."""
    if seite.query_selector("#antwortInput"):
        # ein Wert, der praktisch nie stimmt und jede Toleranz verfehlt
        seite.fill("#antwortInput", "-987654321")
        seite.click("#btnPruefen")
    else:
        knoepfe = seite.query_selector_all(".mc-option")
        if not knoepfe:
            raise SystemExit("weder Eingabefeld noch MC-Optionen gefunden")
        # irgendeine Option; falsch oder richtig - der Loesungsweg erscheint in beiden Faellen
        knoepfe[0].click()
    seite.wait_for_selector("#feedback", state="visible", timeout=5000)


def bild(rel, level=None, aufgabe=None, loesungsweg=False):
    """Schreibt tests/reports/bild-<name>[-L<level>|-A<id>].png und gibt den Pfad zurueck.

    Mit `aufgabe` wird genau diese Aufgaben-id gezeigt. Die Engine waehlt sonst zufaellig
    aus der Stufe, sodass eine bestimmte Aufgabe nur durch wiederholtes Laden zu sehen war;
    die Agenten der Wellen Kl. 10/11 haben sich mit Kopien in trainer/ beholfen, die im
    Dubletten-Vergleich falsche Warnungen ausgeloest haben. Der Weg hier fasst die Engine
    nicht an: alle uebrigen Aufgaben der Stufe gelten als beantwortet, dann bleibt eine uebrig.
    """
    from playwright.sync_api import sync_playwright
    marke = f"-A{aufgabe}" if aufgabe else (f"-L{level}" if level else "")
    if loesungsweg:
        marke += "-weg"
    name = f"bild-{Path(rel).stem}{marke}.png"
    ziel = ROOT / "tests" / "reports" / name
    ziel.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        seite = browser.new_page(viewport={"width": 1240, "height": 900})
        seite.goto(f"{BASE}/{rel}", wait_until="networkidle")
        if aufgabe is not None:
            key = seite.evaluate("typeof THEMA_KEY !== 'undefined' ? THEMA_KEY : null")
            if not key:
                raise SystemExit(f"{rel}: kein THEMA_KEY - ist das ein Trainer?")
            treffer = seite.evaluate("id => AUFGABEN.find(a => a.id === id) || null", aufgabe)
            if not treffer:
                raise SystemExit(f"{rel}: keine Aufgabe mit id {aufgabe}")
            lvl = treffer["level"]
            andere = seite.evaluate(
                "([l, id]) => AUFGABEN.filter(a => a.level === l && a.id !== id).map(a => a.id)",
                [lvl, aufgabe])
            seite.evaluate(
                "([k, l, ids]) => localStorage.setItem('spirale-ref4ohg-' + k,"
                " JSON.stringify({level: l, answered: ids}))",
                [key, lvl, andere])
            seite.reload(wait_until="networkidle")
        elif level:
            # Die Engine liest 'spirale-ref4ohg-<THEMA_KEY>' und ergaenzt fehlende Felder
            # aus DEFAULT_STATE - level allein reicht, damit initApp() nach dem
            # Reload direkt eine Aufgabe dieses Levels rendert (kein Startbildschirm).
            key = seite.evaluate("typeof THEMA_KEY !== 'undefined' ? THEMA_KEY : null")
            if not key:
                raise SystemExit(f"{rel}: kein THEMA_KEY - ist das ein Trainer?")
            seite.evaluate(
                "([k, l]) => localStorage.setItem('spirale-ref4ohg-' + k, JSON.stringify({level: l}))",
                [key, level])
            seite.reload(wait_until="networkidle")
        _katex_abwarten(seite)
        if loesungsweg:
            _loesungsweg_aufdecken(seite)
            _katex_abwarten(seite)
            seite.wait_for_timeout(400)
        seite.screenshot(path=str(ziel), full_page=True)
        browser.close()
    return ziel


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    lvl = int(args[args.index("--level") + 1]) if "--level" in args else None
    auf = int(args[args.index("--aufgabe") + 1]) if "--aufgabe" in args else None
    print(bild(args[0], lvl, auf, "--loesungsweg" in args))
