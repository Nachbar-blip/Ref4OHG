# Änderungsplan Level-Progression Ref4OHG — ENTWURF zur Absprache (2026-09-19)

Status: **Schritte 1 bis 4 umgesetzt (2026-09-19).** Das Rubrik-Gate meldet für alle 76 Trainer
keinen harten Fehler mehr: **74 ohne Beanstandung, 2 Warnungen, 0 Fehler** (Ausgangslage 36 / 8 / 32).
`katex_check` ist für alle 76 Trainer grün.

| Schritt | Inhalt | Commit |
|---|---|---|
| 1 | Gates übernommen, CSS-Fix, 93 Markdown-Stellen, 6 Toleranzen | `c8b6bca` |
| 2 | 57 Kopien übertragen (Wellen Kl. 7 / 8 / 9+10 / Oberstufe) | `2797fbb`, `bd9f1e2`, `4ed9e65`, `028c028` |
| 3 | 8 teilweise deckungsgleiche Trainer | `569d555` |
| 4 | 12 Trainer ohne Kopiervorlage | `188d2b1` |

**Offen bleibt allein Schritt 5:** `8-aehnlichkeit-streckung` und `9-strahlensaetze` sind weiterhin
zu 35/36 identisch. Das ist die einzige verbliebene Gate-Warnung und braucht eine fachliche
Entscheidung (Vorschlag unten unverändert).

## Was der Lehrplanabgleich ergeben hat

Der Abgleich lief gegen das niedersächsische Kerncurriculum (Sek I `ma_gym_si_kc_druck.pdf`,
Oberstufe `ma_go_kc_druck_2019.pdf`, beide unter `schule/Referenz/Lehrplaene/KC_extern/`).
Wichtige Einschränkung: Beide Lehrpläne legen die Kompetenzen in **Doppeljahrgängen** fest
(5/6, 7/8, 9/10), nicht jahrgangsscharf — ein Abgleich kann also nur bandscharf sein.

Von 57 übertragenen Kopien wechseln nur 4 das Band, und alle vier zu Recht:

- **Pythagoras, Wurzeln, Ähnlichkeit/Strahlensätze** stehen in Niedersachsen im Doppeljahrgang
  **9/10** (Lernbereich „Entdeckungen an rechtwinkligen Dreiecken und Ähnlichkeit"), in
  Sachsen-Anhalt in Klasse 8. Ref4OHGs Einordnung stimmt; die übertragenen Aufgaben sind
  Einführungsniveau und passen.
- **Ganzrationale Funktionen** gehören in die **Einführungsphase** (Kl. 11) — ebenso Extrem- und
  Wendepunkte sowie die Tangentensteigung.

Drei Befunde haben die Arbeit inhaltlich verändert:

1. **LGS mit zwei Variablen** stehen im KC im Doppeljahrgang **7/8** („am Ende von Schuljahrgang 8",
   ausdrücklich nur Einsetzungs- und Gleichsetzungsverfahren in einfachen Fällen), in
   Sachsen-Anhalt in Klasse 10. Die Vorlage enthält Parameter-LGS, das Additionsverfahren und eine
   quadratische Funktion — für Klasse 8 zu weit. Statt zu übertragen wurde ein eigenes Level 5
   geschrieben.
2. **Die Tangensfunktion** mit Null- und Polstellen steht **nicht** im Kern des Lernbereichs
   „Periodische Zusammenhänge"; dort stehen Sinus- und Kosinusfunktion, Einheitskreis,
   Parametervariation und die Modellierung periodischer Abläufe. `10-cos-tan-funktion` wurde
   entsprechend umgebaut.
3. **Kreis- und Kugelgleichung** sind im Lernbereich „Raumanschauung und Koordinatisierung (eA)"
   eine **fakultative Erweiterung**, kein Kernbestand. `13-eA-tangenten-kreise` deckt damit
   Wahlstoff ab — inhaltlich vertretbar, aber bewusst zu wissen.

## Weitere Funde, die nichts mit der Stufung zu tun hatten

- **„(LK)" statt „(eA)"** in sechs Klasse-13-Trainern — das Kürzel Sachsen-Anhalts aus der
  Kopiervorlage, für Schüler sichtbar falsch. 12 Stellen korrigiert.
- **`12-wachstum-begrenzt` enthielt kein begrenztes Wachstum**, sondern Exponentialwachstum mit
  Verdopplungs- und Halbwertszeit — 19 Aufgaben wortgleich mit `10-wachstum-linear-exponentiell`.
  Vollständig neu geschrieben; Seitentitel und Kopfzeile heißen jetzt wie die Übersicht.
- **Sechs Ref4OHG-eigene Korrekturen** an Aufgaben, welche die DiffEngine ohnehin ersetzt hat,
  darunter ein falscher Lösungsschlüssel (`11-monotonie-kruemmung` #22) und ein Fachfehler bei
  den Strahlensätzen (`AB ∥ CD` statt `AC ∥ BD`).
- **Sechs hängende Verweise** auf „die vorige Aufgabe" aufgelöst.

## Nebenbefund für später

In 7 Trainern stehen Umlaute und ß als Ersatzschreibung im Aufgabentext („Wie heisst die laengste
Seite", 18 × „Flaeche", 14 × „groesse"). Kein Level-Problem — gehört bei Gelegenheit bereinigt.

## Ziel

Dasselbe wie in der DifferenzierungsEngine: Jede Stufe eines Trainers ist eine eigene
**Anforderungsstufe**, nicht ein weiteres Teilthema.

- **Stufe 1–3 = AFB I** — Grundrechenarten, Standardverfahren, Klassenarbeitsniveau
- **Stufe 4 = AFB II** — Transfer; die Rechenart wird *nicht* mehr angesagt
- **Stufe 5/6 = AFB III** — mehrschrittig, Fehler finden, Aussage prüfen, Umkehraufgabe,
  Spezialfall begründen; in Kl. 11–13 auf IQB-Niveau (eA in den `13-eA-`Trainern)

## Vorgehen

### Schritt 1 — Gates und CSS-Fix übernehmen (Voraussetzung für alles Weitere) — **erledigt 2026-09-19**

1. `tests/level_check.py` und `tests/katex_check.py` aus der DifferenzierungsEngine übernehmen.
   Beide sind projektunabhängig geschrieben und laufen bereits jetzt gegen Ref4OHG.
2. `.aufgabe-text` in `spirale.css` von `display: flex` auf `display: block` umstellen
   (Begründungskommentar aus der DiffEngine mitnehmen), danach **Sichtprüfung am Bild**.
3. Die 87 Markdown-Stellen auf `<b>…</b>` umstellen — skriptgestützt, wie in der DiffEngine.
4. Die 6 fehlenden Toleranzen bei Dezimallösungen ergänzen.

Schritte 2–4 sind reine Reparaturen ohne didaktische Entscheidung und können als ein Block
committet werden. Erst danach zeigt das Gate die *inhaltlichen* Mängel unverstellt an.

**Ergebnis:** Beide Gates liegen in `tests/`, der CSS-Fix ist drin (Sichtprüfung am Bild erfolgt),
93 Markdown-Stellen in 15 Dateien sind auf `<b>…</b>` umgestellt, 6 fehlende Toleranzen ergänzt
(zwei davon in der kompakten einzeiligen Schreibweise `loesung: 9.5, toleranz: 0,`, die das
DiffEngine-Skript nicht erfasste). Gate-Stand danach: **43 ohne Beanstandung, 12 Warnungen,
21 harte Fehler** — von 32 harten Fehlern bleiben also 21, und die sind durchweg inhaltlicher
Natur (MC-Überhang in L5/L6, Formel-Ansage ab Stufe 4). Genau die nimmt Schritt 2 in Angriff.

**Nebenbefund für später:** In 7 Trainern stehen Umlaute und ß als Ersatzschreibung im Text
(„Wie heisst die laengste Seite", 18 × „Flaeche", 14 × „groesse"). Das ist kein Level-Problem und
gehört nicht in diesen Plan, sollte aber bei Gelegenheit bereinigt werden — am besten zusammen mit
der Überarbeitung des jeweiligen Trainers.

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
