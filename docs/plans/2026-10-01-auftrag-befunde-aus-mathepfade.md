# Auftrag: Befunde aus der Mathepfade-Sitzung auf Ref4OHG übertragen

Angelegt 2026-10-01 aus dem Mathepfade-Projekt heraus. **Für eine eigene Session in diesem Ordner.**

> **Stand 2026-10-10: erledigt** (Branch `befunde-aus-mathepfade`, Commits `d35bbee` … `9e62686`).
> Alle fünf Punkte des Vorgehens sind durch: Werkzeug übernommen, 6 harte Fehler behoben,
> 17 Tipps umgeschrieben, Anführungszeichen korrigiert (52 Stellen in 44 Aufgaben – die 44 im
> Text unten zählt Aufgaben), Sichtprüfung je geänderter Aufgabe, dazu ein unabhängiger
> Prüfdurchgang mit Nachträgen. Schlussmessung: `level_check --strict` Exit 0 ohne harte Fehler
> und ohne Tipp-Warnung, `katex_check` 76/76 ok, pytest 475 bestanden (lokaler Server).
>
> **Nachtrag 2026-10-10 (zweiter Durchgang, Branch `mc-optionen-und-reste`): die drei damals
> offenen Punkte sind erledigt.**
> - **MC-Optionen angeglichen:** alle 108 Aufgaben, in denen die richtige Option deutlich länger
>   war als die Distraktoren (meist Distraktoren um eine falsche Begründung verlängert, teils die
>   richtige Option gekürzt). Dabei behoben: `12-stoch-sigma-umgebungen` #33 hatte einen zweiten
>   wahren Distraktor, `9-binomische-formeln-vertieft` #24 die Option „Beide Antworten sind
>   richtig“ (zeigt bei gemischter Reihenfolge ins Leere), `13-eA-tangenten-kreise` #34 und
>   `8-kreise-winkel` #31 je einen vertretbaren Distraktor.
> - **Typografie:** 25 gerade Anführungszeichen-Paare, 25-mal ` -- ` im Aufgabentext, vier
>   Seitentitel (`Ableitung -- Einfuehrung` u. a.), Dezimalpunkte im Boxplot-Trainer,
>   „kongrünt“ (3 ×, Überkorrektur der Umlaut-Bereinigung), „einschliesst“, „ausserhalb“.
> - **Tipps:** die fünf vorrechnenden Nachbar-Tipps, dazu `12-flaechenberechnung` #29,
>   `12-stoch-sigma-umgebungen` #23 und `12-stoch-bedingte-wahrscheinlichkeit` #20.
> - **Hängende Verweise aufgelöst** („vorige Aufgabe“, „siehe Aufgabe 9“, „Aus Level 2“,
>   „dieselbe Datenreihe“, Figur nur aus einer anderen Aufgabe): `10-wachstum-linear-exponentiell`
>   #14, `11-statistik-streumasse` #13, `12-flaechenberechnung` #29,
>   `12-stoch-bedingte-wahrscheinlichkeit` #20, `12-stoch-grundlagen` #30,
>   `9-daten-zufall-boxplot` #32, `9-strahlensaetze` #30, `10-cos-tan-funktion` #34.
> - **Gate erweitert** (`tests/level_check.py`, 7 neue Tests): Verweis auf eine andere Aufgabe
>   ist harter Fehler, ASCII-Ersatz (` -- `, gerade Anführungszeichen, Dezimalpunkt) Warnung.
>   Mathepfade und DifferenzierungsEngine haben diese beiden Prüfungen noch nicht.
> - **Unabhängiger Prüfdurchgang** über alle 122 geänderten Aufgaben: kein Rechenfehler, kein
>   falscher Lösungswert; 5 von 6 Mängeln und alle 14 Hinweise eingearbeitet (der sechste
>   Mangel steht unten als offene Entscheidung).
>
> Schlussmessung: `level_check --strict` Exit 0 ohne Fehler und ohne Warnung, `katex_check` über alle 56 geänderten Trainer ok,
> Playwright-Suite 456 bestanden (lokaler Server), `test_level_check.py` 26 bestanden.
>
> **Bewusst nicht geändert, fachliche Entscheidung nötig:** `11-funktionen-potenzfunktionen` #29
> erklärt \(x^{1/3}\) für alle reellen \(x\) (punktsymmetrisch). Viele Schulbücher definieren
> die dritte Wurzel nur für \(x \geq 0\) – dann wäre der Distraktor „nur für \(x \geq 0\)
> definiert“ die Lehrbuchantwort.

## Warum überhaupt

Ref4OHG ist inhaltlich in gutem Zustand: Die Level-Progression ist durch (Schritte 1–5 des
Entwurfs von 2026-09-19, letzter offener Punkt mit `83b0283` erledigt), `level_check --strict`
läuft über alle 76 Trainer auf **Exit 0 ohne eine einzige Warnung**, und das Mathepfade-Audit
vom 2026-09-19 führt Ref4OHG mit 1 % dünnen Lösungswegen als Referenzprojekt.

**Das Problem ist nicht der Inhalt, sondern der Maßstab.** In der Mathepfade-Sitzung vom
2026-09-30 (alle 90 Trainer, Klassen 7–12) sind vier Fehlerklassen aufgefallen, die **kein**
damaliges Gate kannte — gefunden wurden sie von Prüf-Agenten und in der Sichtprüfung am Bild.
Ref4OHGs `tests/level_check.py` enthält keine davon. Sein grünes Ergebnis sagt also nur, dass
die Fehler von 2026-09 behoben sind, nicht die von 2026-09-30.

Ich habe die neuen Prüfungen versuchsweise über Ref4OHG laufen lassen. Ergebnis:

| Befund | Ref4OHG | Schwere |
|---|---|---|
| MC-Option über Buchstabe/Position angesprochen | **5** | harter Fehler |
| Mathe-Markup außerhalb `\(…\)` | **1** | harter Fehler |
| `<` direkt vor einem Buchstaben | 0 | harter Fehler |
| Tipp nennt den Lösungswert (ab Stufe 4, auch Brüche) | **17** | Warnung |
| Auswertung bei x = 0 in Ableitungs-Trainern | 0 | Warnung |
| deutsche Anführung mit geradem `"` geschlossen | **44** | Kosmetik |

Dazu zwei Werkzeug-Punkte, die schwerer wiegen als die Zahlen (siehe unten).

## Die vier neuen Prüfungen — und warum es sie gibt

Alle vier stammen aus echten Fehlern, die im Quelltext unsichtbar waren. Die Implementierungen
stehen in `../Mathepfade/tests/level_check.py`, die Tests in `../Mathepfade/tests/test_level_check.py`.

1. **`html_frisst_text()` — `<` direkt vor einem Buchstaben.** Die Engine setzt `frage`,
   `optionen`, `tipp` und `loesungsweg` per `innerHTML`. Ein `<` unmittelbar vor einem Buchstaben
   startet für den HTML-Parser ein Tag und frisst den Text bis zum nächsten `>`. `1<x<5` kostete
   in zwei Mathepfade-Trainern die halbe Fallunterscheidung — gültiger String, gültiges KaTeX,
   im Browser die Hälfte weg. `< ` und `<0` sind harmlos, `<b>` bleibt erlaubt.
2. **`mathe_markup_ausserhalb()` — KaTeX-Markup im Klartext.** `0{,}5` außerhalb von `\(…\)`
   rendert wörtlich als „0{,}5". `katex_check` sieht das nicht, weil er nur rendert, was *in*
   der Mathe-Umgebung steht.
3. **`optionsbuchstabe()` — Verweis auf eine MC-Option.** Die Engine mischt die Optionen
   (Fisher-Yates). Ein Lösungsweg mit „Option B" oder „die dritte Antwort" zeigt im Bild auf eine
   **andere** Option. In Mathepfade zeigten zwei Renderings derselben Aufgabe verschiedene
   Reihenfolgen; im Bild stand die im Quelltext erste Option an dritter Stelle.
4. **`tipp_verraet_loesung()` erweitert.** Die alte Fassung prüfte erst ab Betrag 10 und nur
   dezimal; Tipps wie „= 1/5" oder „≈ 0,0808" rutschten durch. Ab Stufe 4 zählen jetzt auch
   Brüche und Kommazahlen. **Wichtig:** Kleine ganze Zahlen zählen nur hinter `=` oder `⇒` —
   eine erste Fassung meldete jede Ziffer und lag zur Hälfte daneben, weil Zahlen ständig als
   Index (`E_2`), Exponent (`r^2`) oder Nenner (`1/3`) im Text stehen. Ein Gate, das zur Hälfte
   Unsinn meldet, erzieht dazu, Warnungen zu ignorieren.

## Zwei Werkzeug-Punkte, die wichtiger sind als die Fundzahlen

**1. Die Playwright-Suite testet die veröffentlichte Seite, nicht die Arbeit.**
`tests/helpers.py` und `tests/conftest.py` setzen fest
`BASE_URL = "https://nachbar-blip.github.io/Ref4OHG"`. In Mathepfade stand dasselbe — und weil
das Repo der Veröffentlichung 52 Commits voraus war, hat **jedes** „pytest grün" der Wellen den
alten deployten Stand bestätigt statt der neuen Aufgaben. Ref4OHG ist aktuell 0 Commits voraus,
der Fehler ist hier also noch **latent**: Er schlägt in dem Moment zu, in dem jemand anfängt zu
arbeiten. Vor der ersten inhaltlichen Änderung umstellen:

```python
BASE_URL = os.environ.get("REF4OHG_BASE_URL", "http://127.0.0.1:8765")
```

Damit läuft die Suite lokal; die deployte Seite prüft man ausdrücklich per Umgebungsvariable.

**2. Es gibt kein Werkzeug für die Sichtprüfung.** `tests/bild.py` fehlt in Ref4OHG. Die
Sichtprüfung am Bild ist nach `schule/CLAUDE.md` bindend, und in Mathepfade wurden **drei**
Fehlerklassen ausschließlich im Bild gefunden: ein gerades `"`, das den JS-String beendete
(Rechenweg weg, leeres Kästchen); das verschluckte `<`; und „V = 1 l = 1000 cm³", das sich als
„V = 11" las, weil das Liter-`l` in der Mathe-Kursiven wie eine Eins aussieht. Übernimm
`../Mathepfade/tests/bild.py` mitsamt beider Schalter:

- `--aufgabe <id>` zeigt gezielt **eine** Aufgabe (die Engine wählt sonst zufällig aus der Stufe).
  Ohne das legten Agenten Kopien in `trainer/` ab — die landen im Dubletten-Vergleich und
  erzeugen dutzende Falschwarnungen.
- `--loesungsweg` antwortet absichtlich falsch und fotografiert das aufgedeckte Feedback. Die
  oben genannten Fehler steckten **im Lösungsweg**, den das Bild sonst gar nicht zeigt.

## Was nicht übertragbar ist

- **`lehrplan_check.py` gehört Thüringen.** Ref4OHG zielt auf das **Kerncurriculum
  Niedersachsen** (Klassen 7–13, Doppeljahrgänge). Die Wortlisten des Mathepfade-Gates sind
  wertlos hier. Ob ein KC-Gate lohnt, ist eine eigene Entscheidung — der Lehrplanabgleich ist
  laut Entwurf von 2026-09-19 ohnehin schon gelaufen, und die KC-Doppeljahrgänge erlauben nur
  bandscharfe Aussagen.
- **Die acht Ersatz-Trainer** von Mathepfade (lehrplanfremde Themen ersetzt) haben hier keine
  Entsprechung.
- **Klasse 13** existiert in Mathepfade nicht — für die eA-Trainer gibt es dort keine Vorlage.

## Vorgeschlagenes Vorgehen

1. **Werkzeug zuerst, vor jeder inhaltlichen Änderung.** `BASE_URL` auf lokal umstellen,
   `bild.py` übernehmen, die vier Prüfungen aus `../Mathepfade/tests/level_check.py` in das
   hiesige `level_check.py` einbauen — **mitsamt den Tests** aus
   `../Mathepfade/tests/test_level_check.py`, sie halten die Grenzfälle fest (`E_2` und `r^2`
   dürfen nicht anschlagen, „die dritte Zeile" eines Gleichungssystems ist keine Option).
   Danach `level_check --strict` über alle 76 Trainer laufen lassen: Die Zahlen oben sind die
   Erwartung.
2. **Die 6 harten Fehler beheben** (Liste unten). Das ist wenig Arbeit und macht das Gate scharf.
3. **Die 17 Tipp-Warnungen durchsehen.** Nicht blind ändern: In Mathepfade waren rund ein Drittel
   Zitate aus der Aufgabenstellung, also Fehlalarme. Die echten nennen den Wert als Ergebnis.
4. **Die 44 Anführungszeichen** als mechanischen Sweep am Ende, wenn keine andere Arbeit läuft
   (`„…"` → `„…“`). Rendert lesbar, ist aber die Vorstufe des Fehlers, der in Mathepfade einen
   JS-String beendet hat.
5. **Sichtprüfung** je geänderter Aufgabe, mit Lösungsweg.

Punkt 1 und 2 sind ein überschaubarer erster Schritt. Punkt 3–5 kann eine zweite Runde sein.

## Fundstellen (Stand 2026-10-01)

**Harte Fehler — MC-Option über Buchstabe oder Position angesprochen (Lösungsweg):**

```
11-ableitungsregeln.html            #35 L6
11-funktionsbegriff.html            #1  L1
11-funktionsbegriff.html            #31 L6
11-tangenten-normalen.html          #35 L6
8-gebrochen-rationale-einfuehrung.html  #23 L4
```

**Harter Fehler — Mathe-Markup außerhalb der Mathe-Umgebung:**

```
8-lgs-zwei-variablen.html           #32 L6  (Feld: frage)
```

**Warnungen — Tipp nennt den Lösungswert (ab Stufe 4 bzw. ab Betrag 10):**

```
10-ableitung-einfuehrung.html       #24 L4   loesung=6
10-potenzfunktionen.html            #31 L6   loesung=3
10-wachstum-linear-exponentiell.html #27 L5  loesung=2
11-ableitungsregeln.html            #30 L5   loesung=3
11-funktionen-ganzrational.html     #36 L6   loesung=4
11-grenzwerte.html                  #20 L4   loesung=2
12-e-funktion.html                  #19 L4   loesung=3
12-steckbriefaufgaben.html          #32 L6   loesung=2
12-steckbriefaufgaben.html          #33 L6   loesung=1
13-eA-funktionenscharen.html        #19 L4   loesung=3
7-prozent-anwendungen-zins.html     #19 L4   loesung=12
7-prozent-grundaufgaben.html        #6  L1   loesung=10
8-gleichungen-linear.html           #13 L3   loesung=12
8-kreise-winkel.html                #28 L5   loesung=55
8-lineare-funktionen-anwendungen.html #36 L6 loesung=1200
9-quadratische-anwendungen.html     #16 L3   loesung=20
9-reelle-zahlen-quadratwurzeln.html #3  L1   loesung=12
```

Die 44 Anführungszeichen-Stellen liegen in 26 Dateien; sie lassen sich mit derselben Suche
jederzeit neu erzeugen, deshalb hier nicht ausgeschrieben.

## Arbeitsweise, die sich in Mathepfade bewährt hat

- **Blöcke mit disjunkten Dateilisten**, je ein Implementier-Agent; danach **ein zweiter Agent,
  der nur prüft** (nachrechnen, Rubrik, Dubletten, Form, Gates, Sichtprüfung). Der Prüfschritt
  hat in jeder Welle Befunde gebracht, die der Implementierer nicht gesehen hat — darunter vier
  echte Rechenfehler und zwei Selbstauskünfte, die zu optimistisch waren.
- **Prüfungen so schneiden, dass zusammengehörige Abgrenzungen bei einem Prüfer liegen.** In
  Kl. 12 sah ein Prüfer Geometrie gA und eA gemeinsam und fand dabei eA-Aufgaben, die gA-Stoff
  mit identischen Zahlen wiederholten — ein Prüfer je Block hätte das nicht gesehen.
- **Jede Zahl mit dem Wolfram-MCP nachrechnen**, auch die nicht gefragten Fälle. Der eine
  Rechenfehler der Kl.-10-Welle war ein übersehener Grenzfall.
- **Fehlersuchaufgaben gegenprüfen:** Führt der vorgeführte falsche Weg wirklich zu einem
  falschen Ergebnis? In Kl. 11 traf einer zufällig die richtige Lösung — der Schüler hätte die
  falsche Regel als bestätigt erlebt.

## Fallen, die in Mathepfade Zeit gekostet haben

- **Bash-Heredoc frisst Backslashes — auch quotiert** (`<<'PY'`). `\\cdot` kommt als `\cdot` an,
  `\\,` als `\,`. Die Regel „nie Heredoc für Aufgabentexte" gilt deshalb auch für
  **Einsetz-Skripte**, die per Heredoc an die Shell gehen. Richtig: Skript mit Write anlegen und
  aufrufen, oder Edit direkt.
- **Python-Rohstring:** In `r"…"` bleibt `ä` wörtlich stehen, wird also nicht zu „ä".
- **Das Edit-Tool kann CRLF-Dateien still auf LF stellen** — vor dem Commit prüfen.
- **`git add` explizit reicht nicht**, wenn ein paralleler Agent Dateien im Index liegen lässt:
  Ein Commit hat so zwei fremde Dateien miterfasst. Richtig ist `git commit -- <pfade>`, das den
  übrigen Index ignoriert.
- **Hilfsdateien nie in `trainer/`** ablegen — sie landen im Dubletten-Vergleich.
- Eine Ersatzzeile muss auf `},` enden, außer bei der letzten Aufgabe (dort `];`).

## Zum Nachlesen im Mathepfade-Projekt

- `../Mathepfade/docs/plans/2026-09-26-STAND.md` — Gesamtbilanz, Gate-Erweiterungen mit
  Begründung, Werkzeug-Fallen, Review-Bilanzen je Welle
- `../Mathepfade/docs/plans/2026-09-26-kl10-kriterien.md` … `kl12` — Kriterium je Aufgabe und
  die Review-Nachträge, also welche Befunde die Prüf-Agenten gefunden haben
- `../Mathepfade/tests/level_check.py`, `test_level_check.py`, `bild.py`, `audit_messung.py`
