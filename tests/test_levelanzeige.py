"""Level-Anzeige und Level-Meldungen sind gestylt (seit 2026-10-18).

spirale-engine.js und spirale.css sind dieselben wie in DiffEngine und Ref4OHG. Die erreichten
Segmente sind deckend hellgruen: das halbdurchsichtige Gruen verschwand auf dem gruenen Verlauf
der Mathepfade (gleiche Datei in allen drei Sammlungen).
"""

import json

from helpers import load_trainer

TRAINER = "9-quadratische-funktionen.html"
KEY = TRAINER[:-5]


def _auf_level(page, level, streak=0):
    page.evaluate("([k, v]) => localStorage.setItem(k, v)", [f"spirale-ref4ohg-{KEY}", json.dumps({
        "level": level, "streak": streak, "wrongStreak": 0, "answered": [],
        "totalCorrect": 0, "totalAttempts": 0})])
    page.reload(wait_until="networkidle")
    page.wait_for_selector("#app .aufgabe-karte", timeout=10000)


def test_erreichte_segmente_sind_eingefaerbt(page):
    load_trainer(page, TRAINER)
    _auf_level(page, 4)
    farben = page.evaluate("""() => [...document.querySelectorAll('.level-segment')]
        .map(s => getComputedStyle(s).backgroundColor)""")
    leer = farben[5]
    assert all(f != leer for f in farben[:3]), farben
    assert farben[3] != farben[2], "aktives Segment hebt sich ab"
    assert farben[0].startswith("rgb("), f"erreichtes Segment deckend, nicht {farben[0]}"


def test_levelaufstieg_blinkt_am_segment_und_meldung_ist_gestylt(page):
    load_trainer(page, TRAINER)
    _auf_level(page, 3, streak=1)
    aufgabe = page.evaluate("window.spiraleAktuelleAufgabe()")
    if aufgabe["typ"] == "mc":
        page.query_selector_all(".mc-option")[aufgabe["korrekt"]].click()
    else:
        page.fill("#antwortInput", str(aufgabe["loesung"]).replace(".", ","))
        page.click("#btnPruefen")
    page.wait_for_selector(".level-change.level-up", timeout=5000)
    assert page.evaluate("getComputedStyle(document.querySelector('.level-change')).fontWeight") == "600"
    assert page.query_selector(".level-segment.flash-up"), "Aufblinken am Segment"
