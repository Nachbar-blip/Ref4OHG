# -*- coding: utf-8 -*-
"""Tests fuer das Lehrplan-Gate Niedersachsen (tests/lehrplan_check.py)."""
import lehrplan_check as lp


def _a(**kw):
    a = {"id": 1, "level": 1, "typ": "numerisch", "frage": "Berechne 2 + 3.",
         "tipp": "Zähle zusammen.", "loesungsweg": "2 + 3 = 5"}
    a.update(kw)
    return a


def test_vektor_in_der_sek1_ist_fehler():
    fehler, _ = lp.pruefe(9, "9-x.html", [_a(frage="Bestimme den Vektor von A nach B.")])
    assert len(fehler) == 1 and "vektor" in fehler[0]


def test_vektor_in_der_qualifikationsphase_ist_erlaubt():
    assert lp.pruefe(12, "12-x.html", [_a(frage="Bestimme den Vektor von A nach B.")]) == ([], [])


def test_hypothesentest_ist_in_jeder_spalte_fehler():
    for klasse in (12, 13):
        fehler, _ = lp.pruefe(klasse, "x.html", [_a(loesungsweg="Der Hypothesentest lehnt ab.")])
        assert fehler, klasse


def test_produktregel_erst_in_der_qualifikationsphase():
    assert lp.pruefe(11, "11-x.html", [_a(tipp="Nutze die Produktregel.")])[0]
    assert lp.pruefe(12, "12-x.html", [_a(tipp="Nutze die Produktregel.")]) == ([], [])


def test_additionsverfahren_in_7_bis_10():
    assert lp.pruefe(8, "8-x.html", [_a(frage="Löse mit dem Additionsverfahren.")])[0]
    assert lp.pruefe(12, "12-x.html", [_a(loesungsweg="Additionsverfahren: I + II.")]) == ([], [])


def test_optionen_werden_mitgelesen():
    a = _a(typ="mc", optionen=["Polynomdivision", "Ausklammern", "p-q-Formel", "Raten"], korrekt=1)
    assert lp.pruefe(11, "11-x.html", [a])[0]


def test_wort_aus_anderem_bundesland_ist_warnung():
    fehler, warnungen = lp.pruefe(12, "12-x.html", [_a(frage="Leite auf: \\(f(x) = 2x\\). (Aufleiten)")])
    assert fehler == [] and len(warnungen) == 1 and "aufleit" in warnungen[0]


def test_wortanfang_zaehlt_wortinneres_nicht():
    """Der Begriff muss am Wortanfang stehen: 'Vektoren' schlaegt an, 'Kollektor' nicht."""
    assert lp.pruefe(9, "9-x.html", [_a(frage="Vektoren addieren.")])[0]
    assert lp.pruefe(9, "9-x.html", [_a(frage="Der Kollektor heizt.")]) == ([], [])


def test_klassen_aus_index_liest_alle_trainer():
    klassen = lp.klassen_aus_index()
    assert klassen["7-rat-zahlen-rechnen.html"] == 7
    assert klassen["13-eA-abstaende.html"] == 13
    assert len(klassen) >= 76
