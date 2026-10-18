# -*- coding: utf-8 -*-
"""Tests fuer tests/aufgaben_setzen.py: ersetzt Aufgaben bytegenau und verlustfrei."""
import json
import re
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


def test_bereich_bleibt_erhalten(tmp_path):
    """Das Feld 'bereich' (9-quadratische-anwendungen) wird nicht verworfen; es steht nach 'typ'."""
    ziel = _kopie(tmp_path)
    neu = dict(lk.lade_aufgaben(ziel)[0], bereich="Analysis", frage="Mit Bereich?")
    aset.setze(ziel, [neu])
    assert lk.lade_aufgaben(ziel)[0] == neu
    assert list(lk.lade_aufgaben(ziel)[0])[:4] == ["id", "level", "typ", "bereich"]


def test_mc_mit_zwei_optionen_wird_gesetzt(tmp_path):
    ziel = _kopie(tmp_path)
    neu = {"id": 2, "level": 1, "typ": "mc", "frage": "Welche Zuordnung liegt vor?",
           "optionen": ["proportional", "antiproportional"], "korrekt": 1,
           "tipp": "Verdopple eine Größe.", "loesungsweg": "Das Produkt bleibt gleich."}
    aset.setze(ziel, [neu])
    assert lk.lade_aufgaben(ziel)[1] == neu


def _muss_scheitern(ziel, aufgaben):
    """ValueError erwartet; die Datei bleibt Byte fuer Byte, wie sie war."""
    vorher = ziel.read_bytes()
    try:
        aset.setze(ziel, aufgaben)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError erwartet")
    assert ziel.read_bytes() == vorher


def test_fehlendes_pflichtfeld_laesst_datei_unveraendert(tmp_path):
    ziel = _kopie(tmp_path)
    gut = lk.lade_aufgaben(ziel)
    for feld in ("tipp", "loesungsweg", "toleranz"):
        _muss_scheitern(ziel, [{k: v for k, v in gut[0].items() if k != feld}])
    _muss_scheitern(ziel, [{k: v for k, v in gut[1].items() if k != "korrekt"}])


def test_korrekt_ausserhalb_laesst_datei_unveraendert(tmp_path):
    ziel = _kopie(tmp_path)
    mc = lk.lade_aufgaben(ziel)[1]
    _muss_scheitern(ziel, [dict(mc, korrekt=4)])
    _muss_scheitern(ziel, [dict(mc, korrekt=-1)])
    _muss_scheitern(ziel, [dict(mc, optionen=mc["optionen"][:2], korrekt=2)])
    _muss_scheitern(ziel, [dict(mc, optionen=mc["optionen"][:1], korrekt=0)])
    _muss_scheitern(ziel, [dict(mc, optionen=mc["optionen"] + ["fünfte"], korrekt=0)])


def test_unbekanntes_feld_laesst_datei_unveraendert(tmp_path):
    ziel = _kopie(tmp_path)
    _muss_scheitern(ziel, [dict(lk.lade_aufgaben(ziel)[0], hinweis="gibt es nicht")])


def test_doppelte_id_laesst_datei_unveraendert(tmp_path):
    ziel = _kopie(tmp_path)
    a = lk.lade_aufgaben(ziel)[0]
    _muss_scheitern(ziel, [dict(a, frage="eins"), dict(a, frage="zwei")])


def test_fehler_in_spaeterer_aufgabe_schreibt_auch_die_erste_nicht(tmp_path):
    ziel = _kopie(tmp_path)
    gut = lk.lade_aufgaben(ziel)
    _muss_scheitern(ziel, [dict(gut[0], frage="gültig"), dict(gut[1], id=77)])


# ---------- Regressionstests nach dem Review vom 2026-10-10 ----------

TRAINER = VORLAGE.parent


def _kopie_von(tmp_path, name):
    ziel = tmp_path / name
    shutil.copy(TRAINER / name, ziel)
    return ziel


def _numerisch(nr, level=4, **kw):
    a = {"id": nr, "level": level, "typ": "numerisch", "frage": f"Frage {nr}?", "loesung": 1,
         "toleranz": 0.01, "tipp": "Tipp.", "loesungsweg": "Weg."}
    a.update(kw)
    return a


def _spanne(roh: bytes, nr: int):
    """Unabhaengig vom Werkzeug: vom '{' vor 'id: nr,' bis zur letzten '}' vor dem naechsten
    Block (bei der letzten Aufgabe: vor '];')."""
    m = re.search(rb"\{\s*id:\s*%d\s*," % nr, roh)
    nach = re.search(rb"\{\s*id:\s*\d+\s*,", roh[m.end():])
    grenze = m.end() + nach.start() if nach else roh.index(b"];", m.end())
    return m.start(), roh.rindex(b"}", m.start(), grenze) + 1


def _neuer_block(vorher: bytes, nachher: bytes, nr: int) -> bytes:
    """Prueft, dass alles vor und hinter dem Block von nr Byte fuer Byte steht, und gibt den
    neuen Block zurueck."""
    a, e = _spanne(vorher, nr)
    rest = len(vorher) - e
    assert nachher[:a] == vorher[:a], "Bytes vor dem Block veraendert"
    assert nachher[len(nachher) - rest:] == vorher[e:], "Bytes hinter dem Block veraendert"
    return nachher[a:len(nachher) - rest]


def test_bytes_vor_und_hinter_dem_block_bleiben(tmp_path):
    ziel = _kopie(tmp_path)
    vorher = ziel.read_bytes()
    aset.setze(ziel, [_numerisch(20)])
    block = _neuer_block(vorher, ziel.read_bytes(), 20)
    assert block.startswith(b"{\r\n        id: 20,\r\n") and block.endswith(b"\r\n      }")
    assert block.count(b"\n") == block.count(b"\r\n") == 9


def test_gefaehrliche_texte_bleiben_text(tmp_path):
    """Klammern, Array-Ende, Kommentarzeichen, Anfuehrungszeichen und 'id: 5,' im Text duerfen
    weder die Aufgabe noch ihre Nachbarn beschaedigen."""
    texte = ["Menge \\(\\{1; 2\\}\\), } allein, { allein, }, und {",
             "Ende ]; mitten im Text, [ und ] und }];",
             "Kommentar // im Text und /* auch */ sowie http://x.de",
             "Zitat \"gerade\" und \\\" und Backslash am Ende \\",
             "Die Liste beginnt mit id: 5, dann 6.",
             "Apostroph ' und Backtick ` und ${x}",
             "Zeile1\nZeile2\tTab"]
    ziel = _kopie(tmp_path)
    urzustand = lk.lade_aufgaben(ziel)
    for i, s in enumerate(texte):
        vorher = ziel.read_bytes()
        neu = {"id": 20, "level": 4, "typ": "mc", "frage": s + f" F{i}", "optionen": [s, s + "2", "x", "y"],
               "korrekt": 0, "tipp": s, "loesungsweg": s}
        aset.setze(ziel, [neu])
        _neuer_block(vorher, ziel.read_bytes(), 20)
        nachher = lk.lade_aufgaben(ziel)
        assert nachher[19] == neu, s
        assert nachher[:19] + nachher[20:] == urzustand[:19] + urzustand[20:], s
    # die Nachbarn lassen sich danach weiter setzen
    aset.setze(ziel, [_numerisch(19), _numerisch(21)])
    assert [a["frage"] for a in lk.lade_aufgaben(ziel)[18:21:2]] == ["Frage 19?", "Frage 21?"]


def test_letzte_aufgabe_vor_dem_array_ende(tmp_path):
    ziel = _kopie(tmp_path)
    vorher = ziel.read_bytes()
    assert b"}];" in vorher
    neu = _numerisch(36, level=6)
    aset.setze(ziel, [neu])
    nachher = ziel.read_bytes()
    _neuer_block(vorher, nachher, 36)
    assert nachher.count(b"}];") == vorher.count(b"}];")
    assert lk.lade_aufgaben(ziel)[35] == neu and len(lk.lade_aufgaben(ziel)) == 36


def test_klammer_hinter_dem_vorgaenger_in_derselben_zeile(tmp_path):
    """Echte Form '},    {' (8-aehnlichkeit-streckung #26): der Vorgaenger bleibt unberuehrt."""
    ziel = _kopie_von(tmp_path, "8-aehnlichkeit-streckung.html")
    vorher = ziel.read_bytes()
    assert re.search(rb"\},[ \t]+\{\r\n\s*id: 26,", vorher)
    neu = _numerisch(26, level=5)
    aset.setze(ziel, [neu])
    block = _neuer_block(vorher, ziel.read_bytes(), 26)
    assert block.count(b"\n") == block.count(b"\r\n")
    nachher = lk.lade_aufgaben(ziel)
    assert nachher[25] == neu and len(nachher) == 36


def test_mischdatei_block_behaelt_sein_zeilenende(tmp_path):
    """Datei fast ueberall CRLF, Block #25 mit LF. Der neue Block uebernimmt das Zeilenende des
    ersetzten Blocks, nicht den Dateimodus.

    Die Mischung wird hier hergestellt: Frueher stand sie zufaellig so in der Arbeitskopie von
    10-ganzrationale-funktionen; nach frischem Auschecken (core.autocrlf) ist die Datei ganz CRLF."""
    ziel = _kopie_von(tmp_path, "10-ganzrationale-funktionen.html")
    roh = ziel.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    a, e = _spanne(roh, 25)
    ziel.write_bytes(roh[:a] + roh[a:e].replace(b"\r\n", b"\n") + roh[e:])
    vorher = ziel.read_bytes()
    a, e = _spanne(vorher, 25)
    assert b"\n" in vorher[a:e] and b"\r\n" not in vorher[a:e]
    alt = lk.lade_aufgaben(ziel)
    aset.setze(ziel, [dict(alt[24], frage="Neue Frage 25?"), dict(alt[23], frage="Neue Frage 24?")])
    nachher = ziel.read_bytes()
    a2, e2 = _spanne(nachher, 25)
    assert b"\r\n" not in nachher[a2:e2] and nachher[a2:e2].count(b"\n") >= 8
    a3, e3 = _spanne(nachher, 24)
    assert nachher[a3:e3].count(b"\n") == nachher[a3:e3].count(b"\r\n") >= 8
    assert nachher[e2:] == vorher[e:]
    assert [x["frage"] for x in lk.lade_aufgaben(ziel)[23:25]] == ["Neue Frage 24?", "Neue Frage 25?"]


def test_reine_lf_datei_bleibt_lf(tmp_path):
    ziel = _kopie(tmp_path)
    ziel.write_bytes(ziel.read_bytes().replace(b"\r\n", b"\n"))
    vorher = ziel.read_bytes()
    aset.setze(ziel, [_numerisch(20)])
    assert b"\r" not in ziel.read_bytes()
    assert b"\n        id: 20,\n" in _neuer_block(vorher, ziel.read_bytes(), 20)
    assert lk.lade_aufgaben(ziel)[19]["frage"] == "Frage 20?"


def test_kommentar_mit_klammer_im_block_wird_abgewiesen(tmp_path):
    """Reviewer-Fall C6a: '}' in einem Kommentar beendet den Block fuer das Werkzeug zu frueh.
    Die Selbstkontrolle merkt es, bevor geschrieben wird."""
    ziel = _kopie(tmp_path)
    ziel.write_bytes(ziel.read_bytes().replace(b"id: 20,", b'id: 20, // Kommentar mit } und "', 1))
    assert len(lk.lade_aufgaben(ziel)) == 36
    _muss_scheitern(ziel, [_numerisch(20)])
    assert list(tmp_path.iterdir()) == [ziel]


def test_script_ende_im_text_wird_abgewiesen(tmp_path):
    """Reviewer-Fall B5: '</script>' in einem Text beendet im Browser den Skriptblock."""
    ziel = _kopie(tmp_path)
    for s in ("Tag </script> im Text", "Tag </SCRIPT > im Text", "<!-- <script> a --> b"):
        _muss_scheitern(ziel, [_numerisch(20, frage=s)])
        _muss_scheitern(ziel, [_numerisch(20, tipp=s)])
        mc = lk.lade_aufgaben(ziel)[1]
        _muss_scheitern(ziel, [dict(mc, optionen=["a", s, "c", "d"])])
    assert list(tmp_path.iterdir()) == [ziel]


def test_fremdes_objekt_mit_id_wird_nicht_ersetzt(tmp_path):
    """Reviewer-Faelle B3/B4 und C10b: 'id: 99,' gibt es nur in einem Text bzw. in einem Objekt
    ausserhalb des Arrays - das ist keine Aufgabe #99."""
    ziel = _kopie(tmp_path)
    aset.setze(ziel, [_numerisch(20, frage="Objekt { id: 99, wert: 3 } gegeben. Ende")])
    _muss_scheitern(ziel, [_numerisch(99)])
    ziel = _kopie(tmp_path)
    ziel.write_bytes(ziel.read_bytes().replace(
        b"const AUFGABEN = [", b'const STUFEN = [{ id: 77, name: "Profi" }];\r\n    const AUFGABEN = [', 1))
    _muss_scheitern(ziel, [_numerisch(77)])
    assert list(tmp_path.iterdir()) == [ziel]


def test_zahl_die_javascript_nicht_haelt_wird_abgewiesen(tmp_path):
    """Die Selbstkontrolle vergleicht, was der Browser liest: 2**53 + 1 kaeme anders zurueck."""
    ziel = _kopie(tmp_path)
    _muss_scheitern(ziel, [_numerisch(20, loesung=2 ** 53 + 1)])


def test_erfolg_hinterlaesst_keine_hilfsdatei(tmp_path):
    ziel = _kopie(tmp_path)
    aset.setze(ziel, [_numerisch(20)])
    assert list(tmp_path.iterdir()) == [ziel]


def test_quelltext_form_wird_abgewiesen(tmp_path):
    """Doppelte Backslashes vor der Klammer heissen: jemand hat die Quelltext-Form uebergeben."""
    ziel = _kopie(tmp_path)
    vorher = ziel.read_bytes()
    for feld, wert in (("frage", "Berechne \\\\(2 + 3\\\\)."), ("tipp", "Nutze \\\\(a\\\\)."),
                       ("loesungsweg", "Also \\\\(5\\\\).")):
        try:
            aset.setze(ziel, [_numerisch(20, **{feld: wert})])
        except ValueError as e:
            assert "ausgewertete Form" in str(e), e
        else:
            raise AssertionError("ValueError erwartet")
    mc = lk.lade_aufgaben(ziel)[1]
    _muss_scheitern(ziel, [dict(mc, optionen=["\\\\(1\\\\)", "b", "c", "d"])])
    assert ziel.read_bytes() == vorher
    # ein LaTeX-Zeilenumbruch '\\' vor etwas anderem als einer Klammer bleibt erlaubt
    gut = _numerisch(20, loesungsweg="$$\\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}$$ und \\(x\\)")
    aset.setze(ziel, [gut])
    assert lk.lade_aufgaben(ziel)[19] == gut


def test_leere_liste_und_fehlende_datei(tmp_path, capsys):
    ziel = _kopie(tmp_path)
    _muss_scheitern(ziel, [])
    daten = tmp_path / "leer.json"
    daten.write_text("[]", encoding="utf-8")
    assert aset.main([str(ziel), str(daten)]) == 1
    assert "FEHLER" in capsys.readouterr().out
    daten.write_text(json.dumps([_numerisch(20)]), encoding="utf-8")
    assert aset.main([str(tmp_path / "gibt-es-nicht.html"), str(daten)]) == 1
    assert "FEHLER" in capsys.readouterr().out
    assert aset.main([str(ziel), str(tmp_path / "gibt-es-nicht.json")]) == 1
    assert "FEHLER" in capsys.readouterr().out


def test_kommandozeile(tmp_path):
    ziel = _kopie(tmp_path)
    daten = tmp_path / "neu.json"
    a = dict(lk.lade_aufgaben(ziel)[5], frage="Über die Kommandozeile gesetzt?")
    daten.write_text(json.dumps([a], ensure_ascii=False), encoding="utf-8")
    assert aset.main([str(ziel), str(daten)]) == 0
    assert lk.lade_aufgaben(ziel)[5]["frage"] == "Über die Kommandozeile gesetzt?"
