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
NOCH_UNEINHEITLICH = {   # Ist-Stand 2026-10-10: 39 von 76
    "10-kreis-kugel.html", "10-potenzen-ganzzahlig.html", "10-potenzfunktionen.html",
    "10-wachstum-linear-exponentiell.html",
    "11-funktionen-ganzrational.html", "11-funktionen-potenzfunktionen.html",
    "11-funktionsbegriff.html", "11-grenzwerte.html", "11-monotonie-kruemmung.html",
    "11-statistik-lagemasse.html", "11-statistik-streumasse.html",
    "12-ebenen.html", "12-skalarprodukt.html", "12-stoch-grundlagen.html",
    "12-stoch-sigma-umgebungen.html", "12-vektoren-grundlagen.html",
    "13-eA-abstaende.html", "13-eA-beurteilende-statistik.html",
    "13-eA-ebenen-lagebeziehungen.html", "13-eA-funktionenscharen.html",
    "13-eA-integralrechnung-vertieft.html", "13-eA-normalverteilung.html",
    "13-eA-tangenten-kreise.html", "13-eA-wachstumsmodelle.html",
}


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


def _knoepfe(gruppe: str):
    """[(data-filter, Beschriftung)] einer Filterleiste, in Reihenfolge."""
    leiste = re.search(r'<div class="filter-bar" data-filter-group="' + gruppe + r'">(.*?)</div>',
                       INDEX, re.S).group(1)
    return re.findall(r'<button class="filter-btn[^"]*" data-filter="([^"]+)">(.*?)</button>', leiste)


def test_genau_ein_qphase_knopf():
    knoepfe = _knoepfe("klasse")
    assert [k for k in knoepfe if "Q-Phase" in k[1]] == [("12", "Q-Phase")]
    assert "13" not in [wert for wert, _ in knoepfe]


def test_ga_ea_leiste_kennt_nur_alle_und_nur_ga():
    # eA ist Kern plus Zusatz, also dasselbe wie "Alle": kein eigener Knopf, kein eigener Filter.
    assert _knoepfe("gaea") == [("alle", "Alle"), ("ga", "Nur gA")]
    assert "filter-ea" not in INDEX


def test_nur_ga_blendet_die_ea_spalte_aus():
    css = re.search(r"<style>(.*?)</style>", INDEX, re.S).group(1)
    assert re.search(r"body\.filter-ga\s+\.col-13\s*\{\s*display:\s*none", css)


def _abschnitte():
    """{(spalte, abschnittstitel): [(dateiname, verbinder)]} in Reihenfolge des Quelltexts."""
    out = {}
    for sp in re.finditer(r'<div class="col col-(\d+)">(.*?)(?=<div class="col col-|<!-- /grid -->)',
                          INDEX, re.S):
        for ab in re.finditer(r'<div class="section-title[^"]*">(.*?)</div>\s*<div class="theme-list">'
                              r'(.*?)(?=<div class="section-card">|\Z)', sp.group(2), re.S):
            out[(int(sp.group(1)), html.unescape(ab.group(1)))] = re.findall(
                r'href="trainer/([^"]+)".*?<span class="connector">(.*?)</span>', ab.group(2), re.S)
    return out


def test_reihenfolge_fachlich():
    funktionen = [d for d, _ in _abschnitte()[(11, "B · Elementare Funktionenlehre")]]
    assert (funktionen.index("10-ganzrationale-funktionen.html")
            < funktionen.index("11-funktionen-ganzrational.html")), funktionen
    geometrie = [d for d, _ in _abschnitte()[(13, "B · Analytische Geometrie eA")]]
    assert geometrie[0] == "12-ebenen.html", geometrie
    # Spalte 9: Aehnlichkeit vor ihrer Anwendung (Strahlensaetze), der Kreis vor den Koerpern
    geo9 = [d for d, _ in _abschnitte()[(9, "C · Geometrie")]]
    assert geo9.index("8-aehnlichkeit-streckung.html") < geo9.index("9-strahlensaetze.html"), geo9
    assert geo9.index("7-kreise-umfang-flaeche.html") < geo9.index("9-raumgeometrie.html"), geo9


def test_nur_die_letzte_zeile_eines_abschnitts_schliesst_ab():
    abschnitte = _abschnitte()
    assert sum(len(z) for z in abschnitte.values()) == len(klassen_aus_index())
    for schluessel, zeilen in abschnitte.items():
        verbinder = [v for _, v in zeilen]
        assert verbinder == ["&#x251C;"] * (len(zeilen) - 1) + ["&#x2514;"], (schluessel, zeilen)


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
