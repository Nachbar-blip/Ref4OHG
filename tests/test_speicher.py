"""Eigener Speicher-Key der Sammlung (seit 2026-10-18).

Alle Sammlungen liegen unter nachbar-blip.github.io und teilen sich einen localStorage. Die
Engine speicherte unter "spirale-<THEMA_KEY>"; 23 Trainer heissen in DiffEngine und Ref4OHG
gleich und teilten sich so Level und beantwortete Aufgaben-IDs (die in der anderen Sammlung
andere Aufgaben bezeichnen). Ref4OHG speichert jetzt unter "spirale-ref4ohg-<THEMA_KEY>"
(data-sammlung am Engine-<script>) und uebernimmt einen vorhandenen alten Stand einmalig.
"""

import json
from pathlib import Path

from helpers import BASE_URL, load_trainer

ROOT = Path(__file__).resolve().parent.parent
TRAINER = "9-quadratische-funktionen.html"   # gibt es auch in der DiffEngine
KEY = TRAINER[:-5]
NEU, ALT = f"spirale-ref4ohg-{KEY}", f"spirale-{KEY}"


def _stand(level, versuche=3):
    return json.dumps({"level": level, "streak": 0, "wrongStreak": 0, "answered": [],
                       "totalCorrect": 1, "totalAttempts": versuche})


def _ls(page, key):
    raw = page.evaluate("k => localStorage.getItem(k)", key)
    return json.loads(raw) if raw else None


def _setze(page, werte):
    page.evaluate("w => { for (const [k, v] of Object.entries(w)) localStorage.setItem(k, v); }", werte)


def _neu_laden(page):
    page.reload(wait_until="networkidle")
    page.wait_for_selector("#app .aufgabe-karte", timeout=10000)


def _antworte_falsch(page):
    if page.query_selector("#antwortInput"):
        page.fill("#antwortInput", "-987654321")
        page.click("#btnPruefen")
    else:
        page.query_selector_all(".mc-option")[0].click()
    page.wait_for_selector("#feedback[style*='block']", timeout=5000)


def test_jeder_trainer_meldet_die_sammlung_an_der_engine():
    for datei in sorted((ROOT / "trainer").glob("*.html")):
        html = datei.read_text(encoding="utf-8")
        assert '<script src="../spirale-engine.js" data-sammlung="ref4ohg"></script>' in html, datei.name


def test_speichert_unter_eigenem_key_und_laesst_den_alten_stehen(page):
    load_trainer(page, TRAINER)
    _antworte_falsch(page)
    assert _ls(page, NEU)["totalAttempts"] == 1
    assert _ls(page, ALT) is None


def test_alter_stand_wird_einmal_uebernommen(page):
    load_trainer(page, TRAINER)
    _setze(page, {ALT: _stand(5)})
    _neu_laden(page)
    assert page.inner_text(".level-label").startswith("Level 5")
    assert _ls(page, NEU)["level"] == 5, "Umzug sofort gespeichert, nicht erst nach der ersten Antwort"
    # Was die andere Sammlung danach unter dem alten Key schreibt, wirkt hier nicht mehr
    _setze(page, {ALT: _stand(1)})
    _neu_laden(page)
    assert page.inner_text(".level-label").startswith("Level 5")
    assert _ls(page, ALT)["level"] == 1


def test_eigener_key_geht_vor(page):
    load_trainer(page, TRAINER)
    _setze(page, {ALT: _stand(1), NEU: _stand(4)})
    _neu_laden(page)
    assert page.inner_text(".level-label").startswith("Level 4")


def test_zuruecksetzen_beruehrt_den_alten_key_nicht(page):
    load_trainer(page, TRAINER)
    _setze(page, {ALT: _stand(5), NEU: _stand(4)})
    _neu_laden(page)
    page.once("dialog", lambda d: d.accept())
    page.click("#btnReset")
    assert _ls(page, NEU)["totalAttempts"] == 0
    assert _ls(page, ALT)["level"] == 5
    _neu_laden(page)
    assert page.inner_text(".level-label").startswith("Level 3"), "kein erneuter Umzug nach dem Zuruecksetzen"


def _zeile(page, key):
    return page.evaluate("""k => { const r = document.querySelector('.theme-row[data-key="spirale-' + k + '"]');
        return r.querySelector('.level-badge').textContent; }""", key)


def test_uebersicht_liest_eigenen_key_und_sonst_den_alten(page):
    page.goto(f"{BASE_URL}/index.html", wait_until="networkidle")
    andere = "9-pythagoras"
    _setze(page, {NEU: _stand(4), ALT: _stand(1), f"spirale-{andere}": _stand(2)})
    page.reload(wait_until="networkidle")
    assert _zeile(page, KEY) == "Lvl 4"
    assert _zeile(page, andere) == "Lvl 2", "noch nicht umgezogener Trainer zeigt seinen alten Stand"
