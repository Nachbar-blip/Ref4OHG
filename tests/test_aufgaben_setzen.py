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
