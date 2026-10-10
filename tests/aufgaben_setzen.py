# -*- coding: utf-8 -*-
"""Ersetzt ganze Aufgaben im AUFGABEN-Array eines Trainers.
   python tests/aufgaben_setzen.py <trainer.html> <daten.json>

Die JSON-Datei ist eine Liste von Aufgaben in AUSGEWERTETER Form (ein Backslash), so wie
level_check.lade_aufgaben() sie liefert. Je Aufgabe wird der Objektblock mit derselben id gegen
einen neu erzeugten getauscht; alles andere bleibt Byte fuer Byte stehen (Kommas, Kommentare
zwischen den Stufen, Zeilenenden). Wer alle 36 Aufgaben uebergibt, ersetzt das ganze Array.

Geschrieben wird erst nach einer Selbstkontrolle: Der neue Inhalt landet in einer Hilfsdatei
neben dem Ziel, wird wie im Browser ausgewertet (level_check.lade_aufgaben) und muss dieselbe
id-Folge, die gesetzten Aufgaben wie uebergeben und alle anderen wie vorher liefern. Sonst
ValueError, und die Zieldatei bleibt, wie sie war."""
import json
import math
import os
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from level_check import lade_aufgaben  # noqa: E402

# Reihenfolge der Felder im erzeugten Block; geschrieben werden nur die vorhandenen.
FELDER = ("id", "level", "typ", "bereich", "frage", "optionen", "korrekt", "loesung", "toleranz",
          "einheit", "tipp", "loesungsweg")
PFLICHT = ("id", "level", "typ", "frage", "tipp", "loesungsweg")
PFLICHT_JE_TYP = {"mc": ("optionen", "korrekt"), "numerisch": ("loesung", "toleranz")}
# String-Literal oder Klammer. Ein einzelnes '"' bleibt nur uebrig, wenn ein String nicht endet.
_TOKEN = re.compile(r'"(?:[^"\\]|\\.)*"|[{}"]')
# Im Browser beendet '</script' den Skriptblock mitten im String; '<!--' samt '<script' haelt ihn
# ueber sein Ende hinaus offen. Die Auswertung mit node sieht beides nicht.
_SKRIPT = re.compile(r"</?script|<!--", re.I)
# Zwei Backslashes vor der Klammer: Quelltext-Form ('\\\\(') statt ausgewerteter Form ('\\(').
_QUELLTEXT_FORM = re.compile(r"(?<!\\)\\\\[()]")


def kodiere(s: str) -> str:
    """JS-String-Literal samt Anfuehrungszeichen: Backslash -> \\\\, '"' -> \\", Rest woertlich.
    Steuerzeichen (Zeilenumbruch, Tab) wuerden das Literal zerreissen und werden maskiert."""
    return json.dumps(s, ensure_ascii=False).replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def _wert(v) -> str:
    if isinstance(v, str):
        return kodiere(v)
    if isinstance(v, list):
        return "[" + ", ".join(kodiere(o) for o in v) + "]"
    return json.dumps(v)


def _ganzzahl(v) -> bool:
    return isinstance(v, int) and not isinstance(v, bool)


def _zahl(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def pruefe(a) -> None:
    """ValueError, wenn die Aufgabe nicht geschrieben werden darf."""
    if not isinstance(a, dict):
        raise ValueError(f"Aufgabe ist kein Objekt: {str(a)[:60]!r}")
    k = f"Aufgabe #{a.get('id')}"
    je_typ = PFLICHT_JE_TYP.get(a.get("typ")) if isinstance(a.get("typ"), str) else None
    fehlt = [f for f in PFLICHT + (je_typ or ()) if f not in a]
    if fehlt:
        raise ValueError(f"{k}: Pflichtfeld fehlt: {', '.join(fehlt)}")
    if je_typ is None:
        raise ValueError(f"{k}: typ ungueltig ({a['typ']!r}), erlaubt: mc, numerisch")
    unbekannt = [f for f in a if f not in FELDER]
    if unbekannt:
        raise ValueError(f"{k}: unbekanntes Feld: {', '.join(map(str, unbekannt))}")
    for f in ("id", "level"):
        if not _ganzzahl(a[f]):
            raise ValueError(f"{k}: {f} ist keine ganze Zahl ({a[f]!r})")
    for f in ("bereich", "frage", "einheit", "tipp", "loesungsweg"):
        if f in a and not isinstance(a[f], str):
            raise ValueError(f"{k}: {f} ist kein Text ({a[f]!r})")
    anzahl = 4
    if "optionen" in a:
        opt = a["optionen"]
        # 2 bis 4 wie level_check: zwei Optionen sind z. B. bei proportional/antiproportional richtig.
        if not isinstance(opt, list) or not 2 <= len(opt) <= 4 or not all(isinstance(o, str) for o in opt):
            raise ValueError(f"{k}: optionen braucht 2 bis 4 Texte")
        anzahl = len(opt)
    if "korrekt" in a and not (_ganzzahl(a["korrekt"]) and 0 <= a["korrekt"] < anzahl):
        raise ValueError(f"{k}: korrekt muss 0 bis {anzahl - 1} sein ({a['korrekt']!r})")
    for f in ("loesung", "toleranz"):
        if f in a and not _zahl(a[f]):
            raise ValueError(f"{k}: {f} ist keine Zahl ({a[f]!r})")
    texte = [(f, a[f]) for f in ("bereich", "frage", "einheit", "tipp", "loesungsweg") if f in a]
    texte += [(f"optionen[{i}]", o) for i, o in enumerate(a.get("optionen") or [])]
    for f, text in texte:
        if _SKRIPT.search(text):
            raise ValueError(f"{k}: {f} enthaelt '</script', '<script' oder '<!--' "
                             f"(zerreisst im Browser den Skriptblock der Seite)")
        if _QUELLTEXT_FORM.search(text):
            raise ValueError(f"{k}: {f}: Backslashes doppelt - ausgewertete Form uebergeben "
                             f"(ein Backslash vor der Klammer, wie lade_aufgaben sie liefert)")


def _finde(roh: str, nr: int):
    """(anfang, ende, einzug_felder, einzug_klammer) des Objektblocks mit dieser id.
    anfang zeigt auf '{', ende hinter '}' - Komma und Kommentare danach gehoeren nicht dazu."""
    treffer = list(re.finditer(rf"\bid:\s*{nr}\s*,", roh))
    if len(treffer) != 1:
        raise ValueError(f"id {nr}: {len(treffer)}-mal gefunden (erwartet: genau einmal)")
    m = treffer[0]
    auf = roh.rfind("{", 0, m.start())
    if auf < 0 or roh[auf + 1:m.start()].strip():
        raise ValueError(f"id {nr}: kein '{{' unmittelbar vor der id")
    tiefe, zu = 0, -1
    for t in _TOKEN.finditer(roh, auf):
        if t.group() == "{":
            tiefe += 1
        elif t.group() == "}":
            tiefe -= 1
            if tiefe == 0:
                zu = t.start()
                break
        elif t.group() == '"':
            zeile = roh.count("\n", 0, t.start()) + 1
            raise ValueError(f"id {nr}: String-Literal endet nicht (Zeile {zeile})")
    if zu < 0:
        raise ValueError(f"id {nr}: schliessendes '}}' nicht gefunden")

    def einzug_vor(pos: int, ersatz: str) -> str:
        """Leerraum vom Zeilenanfang bis pos; steht dort schon Code, gilt der Ersatz."""
        vor = roh[roh.rfind("\n", 0, pos) + 1:pos]
        return ersatz if vor.strip() else vor

    kopf = re.match(r"[ \t]*", roh[roh.rfind("\n", 0, auf) + 1:auf]).group()
    return auf, zu + 1, einzug_vor(m.start(), kopf + "  "), einzug_vor(zu, kopf)


def _block(a: dict, einzug: str, einzug_zu: str, eol: str) -> str:
    zeilen = [f"{einzug}{f}: {_wert(a[f])}" for f in FELDER if f in a]
    return "{" + eol + ("," + eol).join(zeilen) + eol + einzug_zu + "}"


def _auswerten(pfad: Path, was: str) -> list:
    try:
        return lade_aufgaben(pfad)
    except RuntimeError as e:
        raise ValueError(f"{was} nicht auswertbar: {e}") from None


def _schreibe_geprueft(pfad: Path, inhalt: bytes, vorher: list, aufgaben: list) -> None:
    """Selbstkontrolle: Inhalt in eine Hilfsdatei neben dem Ziel, auswerten, vergleichen, erst
    dann das Ziel ersetzen. Die Hilfsdatei endet nicht auf .html (level_check liest trainer/*.html)
    und wird in jedem Fall wieder entfernt."""
    gesetzt = {a["id"]: a for a in aufgaben}
    fd, name = tempfile.mkstemp(dir=pfad.parent, prefix=f".{pfad.name}.", suffix=".tmp")
    tmp = Path(name)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(inhalt)
        nachher = _auswerten(tmp, "Selbstkontrolle: neuer Inhalt")
        if [a.get("id") for a in nachher] != [a.get("id") for a in vorher]:
            raise ValueError("Selbstkontrolle: Anzahl oder Reihenfolge der Aufgaben waere veraendert")
        for alt, neu in zip(vorher, nachher):
            if neu != gesetzt.get(alt["id"], alt):
                art = "kaeme anders zurueck als uebergeben" if alt["id"] in gesetzt else "waere mitveraendert"
                raise ValueError(f"Selbstkontrolle: Aufgabe #{alt['id']} {art}")
        os.replace(tmp, pfad)
    finally:
        tmp.unlink(missing_ok=True)


def setze(pfad: Path, aufgaben: list) -> None:
    """Tauscht in der Trainer-Datei jede uebergebene Aufgabe (ausgewertete Form) gegen den Block
    mit derselben id. Bei einem Fehler (ValueError) bleibt die Datei unberuehrt."""
    pfad = Path(pfad)
    if not isinstance(aufgaben, list) or not aufgaben:
        raise ValueError("erwartet wird eine nicht leere Liste von Aufgaben")
    for a in aufgaben:
        pruefe(a)
    ids = [a["id"] for a in aufgaben]
    doppelt = sorted({i for i in ids if ids.count(i) > 1})
    if doppelt:
        raise ValueError(f"id mehrfach in den Daten: {', '.join(map(str, doppelt))}")
    roh = pfad.read_bytes().decode("utf-8")
    vorher = _auswerten(pfad, "Zieldatei")
    fehlt = sorted(set(ids) - {a.get("id") for a in vorher})
    if fehlt:
        raise ValueError(f"id nicht im AUFGABEN-Array: {', '.join(map(str, fehlt))}")
    datei_eol = "\r\n" if "\r\n" in roh else "\n"
    stellen = []
    for a in aufgaben:
        anfang, ende, einzug, einzug_zu = _finde(roh, a["id"])
        # Zeilenende des ersetzten Blocks, nicht der Datei: manche Trainer mischen CRLF und LF.
        alt = roh[anfang:ende]
        eol = "\r\n" if "\r\n" in alt else "\n" if "\n" in alt else datei_eol
        stellen.append((anfang, ende, _block(a, einzug, einzug_zu, eol)))
    for anfang, ende, block in sorted(stellen, reverse=True):
        roh = roh[:anfang] + block + roh[ende:]
    _schreibe_geprueft(pfad, roh.encode("utf-8"), vorher, aufgaben)


def main(argv) -> int:
    if len(argv) != 2:
        print("Aufruf: python tests/aufgaben_setzen.py <trainer.html> <daten.json>")
        return 2
    pfad = Path(argv[0])
    try:
        aufgaben = json.loads(Path(argv[1]).read_bytes().decode("utf-8-sig"))
        setze(pfad, aufgaben)
    except (ValueError, OSError) as e:
        print(f"FEHLER {pfad.name}: {e}")
        return 1
    for a in aufgaben:
        print(f"ok {pfad.name} #{a['id']}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
