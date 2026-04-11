"""Shared fixtures and trainer list for Playwright tests."""

import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://nachbar-blip.github.io/Ref4OHG"

TRAINER_FILES = [
    "7-dreiecke-konstruktionen.html",
    "7-gleichungen-linear.html",
    "7-koerper-volumen.html",
    "7-kreise-umfang-flaeche.html",
    "7-prozent-anwendungen-zins.html",
    "7-prozent-grundaufgaben.html",
    "7-rat-zahlen-rechnen.html",
    "7-terme-vereinfachen.html",
    "7-wahrscheinlichkeit.html",
    "7-zuordnungen-proportional.html",
    "8-aehnlichkeit-streckung.html",
    "8-gebrochen-rationale-einfuehrung.html",
    "8-gleichungen-linear.html",
    "8-koerperberechnung.html",
    "8-kreise-winkel.html",
    "8-lgs-zwei-variablen.html",
    "8-lineare-funktionen-anwendungen.html",
    "8-lineare-funktionen-grund.html",
    "8-terme-binomische-formeln.html",
    "8-zufallsversuche-mehrstufig.html",
    "9-binomische-formeln-vertieft.html",
    "9-daten-zufall-boxplot.html",
    "9-potenzen-wurzeln.html",
    "9-pythagoras.html",
    "9-quadratische-anwendungen.html",
    "9-quadratische-funktionen.html",
    "9-quadratische-gleichungen.html",
    "9-raumgeometrie.html",
    "9-reelle-zahlen-quadratwurzeln.html",
    "9-strahlensaetze.html",
    "10-ableitung-einfuehrung.html",
    "10-cos-tan-funktion.html",
    "10-ganzrationale-funktionen.html",
    "10-kreis-kugel.html",
    "10-potenzen-ganzzahlig.html",
    "10-potenzfunktionen.html",
    "10-sin-cos-parameter.html",
    "10-sinusfunktion.html",
    "10-trig-anwendungen.html",
    "10-trig-einheitskreis.html",
    "10-trig-rechtwinkliges-dreieck.html",
    "10-wachstum-linear-exponentiell.html",
    "11-ableitungsregeln.html",
    "11-extrempunkte-wendepunkte.html",
    "11-extremwertaufgaben.html",
    "11-funktionen-ganzrational.html",
    "11-funktionen-potenzfunktionen.html",
    "11-funktionsbegriff.html",
    "11-grenzwerte.html",
    "11-kurvendiskussion.html",
    "11-monotonie-kruemmung.html",
    "11-statistik-lagemasse.html",
    "11-statistik-streumasse.html",
    "11-tangenten-normalen.html",
    "12-bestimmtes-integral.html",
    "12-e-funktion.html",
    "12-ebenen.html",
    "12-flaechenberechnung.html",
    "12-geraden-raum.html",
    "12-skalarprodukt.html",
    "12-stammfunktionen.html",
    "12-steckbriefaufgaben.html",
    "12-stoch-bedingte-wahrscheinlichkeit.html",
    "12-stoch-binomialverteilung.html",
    "12-stoch-grundlagen.html",
    "12-stoch-sigma-umgebungen.html",
    "12-vektoren-grundlagen.html",
    "12-wachstum-begrenzt.html",
    "13-eA-abstaende.html",
    "13-eA-beurteilende-statistik.html",
    "13-eA-ebenen-lagebeziehungen.html",
    "13-eA-funktionenscharen.html",
    "13-eA-integralrechnung-vertieft.html",
    "13-eA-normalverteilung.html",
    "13-eA-tangenten-kreise.html",
    "13-eA-wachstumsmodelle.html",
]


@pytest.fixture(scope="session")
def browser():
    """Shared browser instance across all tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Fresh browser context + page per test (isoliert localStorage)."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def pytest_generate_tests(metafunc):
    """Parametrisiert alle Tests mit der Trainer-Liste."""
    if "trainer_file" in metafunc.fixturenames:
        metafunc.parametrize(
            "trainer_file",
            TRAINER_FILES,
            ids=[f.replace(".html", "") for f in TRAINER_FILES],
        )
