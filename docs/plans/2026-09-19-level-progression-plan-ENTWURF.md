# Änderungsplan Level-Progression Ref4OHG — ENTWURF zur Absprache (2026-09-19)

Status: **Entwurf, noch nicht begonnen.** Anlass ist die am 2026-09-18 abgeschlossene
Level-Progression der DifferenzierungsEngine (alle 103 Trainer, Kl. 5–12). Ref4OHG ist in weiten
Teilen aus derselben Quelle entstanden und hat deshalb voraussichtlich dieselben Mängel geerbt.

Dieser Plan beruht auf einer **Messung**, nicht auf einer Vermutung — die Zahlen unten stammen aus
dem Rubrik-Gate der DiffEngine (`tests/level_check.py`), angewendet auf die 76 Ref4OHG-Trainer,
sowie aus einem Textvergleich gegen den DiffEngine-Stand vor der Überarbeitung (Commit `9baddf3`).

## Befundlage (gemessen am 2026-09-19)

**Umfang:** 76 Trainer, je 36 Aufgaben in 6 Stufen. Klassen 7–13
(7: 10 · 8: 10 · 9: 10 · 10: 12 · 11: 12 · 12: 14 · 13: 8 — Klasse 13 als eA-Jahrgang,
das ist die Niedersachsen-Besonderheit gegenüber der DiffEngine).

**Rubrik-Gate (DiffEngine-Maßstab, versuchsweise angewendet):**

| Ergebnis | Trainer |
|---|---|
| ohne Beanstandung | 20 |
| mit Warnung | 24 |
| mit hartem Fehler | 32 |

Verteilung der Fehler über die Jahrgänge: Kl. 10 neun Trainer, Kl. 9 sechs, Kl. 8 fünf, Kl. 13 vier,
Kl. 11 und 12 je drei, Kl. 7 zwei.

**Fehlerarten im Einzelnen:**

- **87 Stellen Markdown-Sternchen** (`**fett**`) in Frage-, Tipp- oder Lösungswegtexten. Die Engine
  rendert kein Markdown — die Sternchen erscheinen wörtlich auf dem Bildschirm. Identischer Befund
  wie in der DiffEngine (dort 124 Stellen, behoben in Commit `76fe215`).
- **19 Stufen mit MC-Überhang** in L5/L6 (bis zu 6 von 6 Aufgaben als Multiple Choice). Vier
  Antwortmöglichkeiten machen eine Begründungsaufgabe zur Ratefrage; der Maßstab erlaubt höchstens 3.
- **17 Aufgaben mit Formel- oder Rechenweg-Ansage ab Stufe 4** („Berechne mit der Formel …").
  Ab AFB II soll der Weg selbst gewählt werden.
- **6 Dezimallösungen ohne Toleranz** — der Schüler muss exakt treffen, sonst gilt die Antwort als falsch.
- Dazu Warnungen wegen **wortgleicher Aufgaben zwischen Trainern**, am deutlichsten
  `9-strahlensaetze` gegenüber `8-aehnlichkeit-streckung`: 35 von 36 Aufgaben sind dieselben.

**Darstellungsfehler in `spirale.css`:** `.aufgabe-text` ist eine Flex-Zeile
(`display: flex; align-items: center`). Dadurch steht jede Inline-Formel `\(...\)` als eigenes
Element in einer eigenen Zeile — derselbe Fehler, der in der DiffEngine am 2026-09-18 an der Ursache
behoben wurde (Commit `2b35b72`). Betrifft **alle** Trainer gleichzeitig.

**Keine Gates vorhanden:** `tests/` enthält nur `test_trainer.py`. Die beiden Prüfskripte
`level_check.py` (Rubrik, ohne Browser) und `katex_check.py` (rendert jede Aufgabe im Browser)
existieren bisher nur in der DifferenzierungsEngine.

## Der entscheidende Befund: 57 Trainer sind Kopien

Ein Textvergleich gegen den DiffEngine-Altstand zeigt, wie viel Arbeit bereits erledigt ist:

| Deckung mit dem DiffEngine-Altstand | Trainer | Konsequenz |
|---|---|---|
| ≥ 80 % (meist 36/36 Aufgaben identisch) | **57** | fertigen Stufenblock übertragen |
| 40–79 % | 8 | teilweise übertragbar, Rest von Hand |
| < 40 % (eigenständig) | 11 | eigene Überarbeitung nötig |

Etliche Kopien tragen **einen anderen Dateinamen**, weil Niedersachsen den Stoff anders verteilt.
Die Zuordnung ist eindeutig, hier die wichtigsten:

| Ref4OHG | entspricht DiffEngine |
|---|---|
| `9-pythagoras` | `8-pythagoras` |
| `9-strahlensaetze` | `8-aehnlichkeit-streckung` |
| `9-reelle-zahlen-quadratwurzeln` | `8-quadratwurzeln-reelle-zahlen` |
| `9-potenzen-wurzeln` | `9-pot-wurzeln-rational` |
| `9-binomische-formeln-vertieft` | `9-pot-gesetze` |
| `9-quadratische-funktionen` / `-gleichungen` / `-anwendungen` | `9-func-quadratisch` / `-quadrat-gleichungen` / `-quadrat-anwendungen` |
| `10-potenzen-ganzzahlig` / `10-potenzfunktionen` | `9-pot-ganzzahlige-exp` / `9-pot-natuerliche-exp` |
| `10-trig-anwendungen` / `10-trig-rechtwinkliges-dreieck` | gleichnamig in Kl. 9 |
| `11-*` (Analysis, 8 Trainer) | `11-analysis-*` |
| `12-ebenen` / `12-geraden-raum` / `12-vektoren-grundlagen` | `12-geom-ebenen` / `-geraden` / `-vektoren-wiederholung` |
| `12-steckbriefaufgaben` | `11-analysis-steckbriefaufgaben` |
| `13-eA-*` (6 Trainer) | `12-lk-*` |

**Das ändert den Zuschnitt der Arbeit grundlegend:** Für drei Viertel der Trainer ist der inhaltlich
schwierige Teil — neue AFB-II/III-Aufgaben erfinden, rechnen, prüfen — bereits getan. Es geht um
Übertragung mit Anpassung, nicht um Neuschreiben.

## Ziel

Dasselbe wie in der DifferenzierungsEngine: Jede Stufe eines Trainers ist eine eigene
**Anforderungsstufe**, nicht ein weiteres Teilthema.

- **Stufe 1–3 = AFB I** — Grundrechenarten, Standardverfahren, Klassenarbeitsniveau
- **Stufe 4 = AFB II** — Transfer; die Rechenart wird *nicht* mehr angesagt
- **Stufe 5/6 = AFB III** — mehrschrittig, Fehler finden, Aussage prüfen, Umkehraufgabe,
  Spezialfall begründen; in Kl. 11–13 auf IQB-Niveau (eA in den `13-eA-`Trainern)

## Vorgehen

### Schritt 1 — Gates und CSS-Fix übernehmen (Voraussetzung für alles Weitere)

1. `tests/level_check.py` und `tests/katex_check.py` aus der DifferenzierungsEngine übernehmen.
   Beide sind projektunabhängig geschrieben und laufen bereits jetzt gegen Ref4OHG.
2. `.aufgabe-text` in `spirale.css` von `display: flex` auf `display: block` umstellen
   (Begründungskommentar aus der DiffEngine mitnehmen), danach **Sichtprüfung am Bild**.
3. Die 87 Markdown-Stellen auf `<b>…</b>` umstellen — skriptgestützt, wie in der DiffEngine.
4. Die 6 fehlenden Toleranzen bei Dezimallösungen ergänzen.

Schritte 2–4 sind reine Reparaturen ohne didaktische Entscheidung und können als ein Block
committet werden. Erst danach zeigt das Gate die *inhaltlichen* Mängel unverstellt an.

### Schritt 2 — Übertragung der 57 Kopien

Je Trainer: den überarbeiteten Stufenblock (meist L5/L6, teils L4) aus dem DiffEngine-Gegenstück
holen, Bezeichner und Aufgaben-IDs anpassen, Gate laufen lassen, Zahlen erneut mit Wolfram prüfen,
KaTeX-Check, Screenshot ansehen, committen. Sinnvolle Bündelung in Wellen zu je 8–10 Trainern
entlang der Jahrgänge.

**Vor der Übertragung inhaltlich zu klären** (siehe offene Fragen): Ob der niedersächsische Lehrplan
an derselben Stelle steht. Die Klassenzuordnung weicht ab — was in Sachsen-Anhalt Kl. 8 ist,
steht hier teils in Kl. 9. Eine Aufgabe, die in der DiffEngine AFB III der Klasse 8 war, kann in
Ref4OHG Klasse 9 zu leicht sein.

### Schritt 3 — Die 8 teilweise deckungsgleichen Trainer

`10-sin-cos-parameter`, `10-sinusfunktion`, `10-trig-einheitskreis`,
`10-wachstum-linear-exponentiell`, `12-e-funktion`, `12-skalarprodukt`, `12-wachstum-begrenzt`,
`8-lgs-zwei-variablen`. Hier passt etwa die Hälfte der Aufgaben; der Rest wird nach demselben
Muster neu geschrieben.

### Schritt 4 — Die 11 eigenständigen Trainer

Vorher ein **Audit nach dem Muster der DifferenzierungsEngine**
(`docs/audit/audit-2026-09-17-level-progression.md`): je Trainer Score 0–3, kollabierende Stufen,
Hauptmangel, fehlende AFB-III-Formate. Dann Überarbeitung wie dort.

### Schritt 5 — Die Dublette `9-strahlensaetze` / `8-aehnlichkeit-streckung`

35 von 36 Aufgaben sind identisch. Zwei Trainer im selben Angebot, die dasselbe abfragen, sind für
Schüler wertlos. Vorschlag: `9-strahlensaetze` auf die Strahlensätze im engeren Sinn umstellen
(Streckenverhältnisse, Messaufgaben im Gelände, Umkehrung des ersten Strahlensatzes) und die
Ähnlichkeitsabbildungen bei `8-aehnlichkeit-streckung` belassen. **Das ist eine fachliche
Entscheidung und braucht deine Freigabe.**

## Arbeitsweise je Trainer (bewährt, aus der DifferenzierungsEngine)

1. Befund lesen → neuen Stufenblock in eine Scratchpad-`.js` schreiben
2. Einsetzen per Skript (Zeilenenden der Zieldatei erhalten!)
3. `level_check.py` — Rubrik
4. **Jede Zahl mit Wolfram nachrechnen** — ohne Ausnahme
5. `katex_check.py` (braucht `python -m http.server 8765`)
6. Screenshot erzeugen **und ansehen** (Sichtprüfung ist bindend, `schule/CLAUDE.md`)
7. Commit je Block

**Warnung aus der DiffEngine-Arbeit:** Aufgabentexte mit LaTeX niemals über ein Bash-Heredoc
schreiben — dabei werden doppelte Backslashes zerstört, `\\frac` wird zu `\f` (Seitenvorschub), und
KaTeX bricht. Immer Write/Edit verwenden.

## Aufwandsschätzung

| Schritt | Trainer | Aufwand |
|---|---|---|
| 1 Gates, CSS, Markdown, Toleranzen | alle 76 | ein Arbeitsblock |
| 2 Übertragung der Kopien | 57 | 6–7 Wellen |
| 3 teilweise deckungsgleich | 8 | 1 Welle |
| 4 eigenständig (inkl. Audit) | 11 | 2 Wellen |
| 5 Dublette Strahlensätze | 1 | nach Freigabe |

Zum Vergleich: Die 103 DiffEngine-Trainer haben an zwei Arbeitstagen gut 20 Commits gebraucht —
und dort musste jeder Stufenblock neu erfunden werden.

## Offene Fragen an den Autor

1. **Lehrplanabgleich Niedersachsen:** Die Klassenzuordnung weicht von Sachsen-Anhalt ab (Pythagoras
   Kl. 8 → 9, Potenzen Kl. 9 → 10, Analysis Kl. 11 → 11/12, LK → `13-eA-`). Soll ich die
   übertragenen Aufgaben schlicht mitnehmen, oder den Kerncurriculum-Abgleich je Jahrgang
   mitmachen? Letzteres kostet spürbar mehr, verhindert aber Aufgaben unter oder über Niveau.
2. **Klasse 13 (eA):** Die 8 `13-eA-`Trainer entsprechen den DiffEngine-LK-Trainern der Kl. 12.
   Dort wurden in `12-lk-geom-kreis-kreis` und `12-lk-geom-tangenten` lehrplanfremde Inhalte
   (Radikalachse, Potenz, Kreisbüschel, Radikalzentrum, Ähnlichkeitspunkte) durch lehrplankonforme
   Aufgaben ersetzt. `13-eA-tangenten-kreise` ist zu 35/36 die Kopie davon — dieselbe Entscheidung
   übernehmen, oder in Niedersachsen anders?
3. **Dublette Strahlensätze** (Schritt 5) — inhaltliche Freigabe.
4. **Engine-Tempo:** In der DiffEngine ist offengeblieben, ob der Stufenaufstieg nach 3 statt 2
   richtigen Antworten erfolgen soll. Gilt für Ref4OHG dieselbe Zurückstellung?
5. **Reihenfolge:** Von unten (Kl. 7) oder von oben (Kl. 13 / Abiturrelevanz zuerst)?

## Grundlagen

- `../DifferenzierungsEngine/docs/plans/2026-09-17-level-progression-plan-ENTWURF.md` — Ursprungsplan
- `../DifferenzierungsEngine/docs/audit/audit-2026-09-17-level-progression.md` — Auditmuster
- `../DifferenzierungsEngine/tests/level_check.py`, `katex_check.py` — die zu übernehmenden Gates
- `schule/CLAUDE.md` — Sichtprüfung (bindend), Materialindex (strikt lokal)
