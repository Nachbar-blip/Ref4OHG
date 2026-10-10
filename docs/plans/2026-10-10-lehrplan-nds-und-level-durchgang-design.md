# Ref4OHG: Kerncurriculum Niedersachsen und Level-Durchgang — Design (2026-10-10)

Status: Umfang „A, voll“ vom Autor freigegeben am 2026-10-10.
Vorbild: `../Mathepfade/docs/plans/2026-09-26-lehrplan-th-und-level-progression-design.md`.
Grundlage: `docs/audit/lehrplanabgleich-nds-2026-10-10.md` (trainergenauer Abgleich mit
KC-Fundstellen und Aufgaben-IDs).

## Ausgangslage

- Ref4OHG hat seit 2026-09-19 die Level-Progression der DifferenzierungsEngine: 57 Stufenblöcke
  übertragen, 20 Trainer eigens bearbeitet. Der damalige Lehrplanabgleich betraf nur diese
  57 Trainer und nur die Ebene der Doppeljahrgänge.
- Am 2026-10-10 kamen die Gates und Befunde aus Mathepfade dazu (Branches
  `befunde-aus-mathepfade`, `mc-optionen-und-reste`): 6 harte Fehler, 108 MC-Aufgaben,
  Tipps, hängende Verweise, Typografie.
- Was gegenüber Mathepfade fehlt: der trainergenaue Lehrplanabgleich mit Umzügen und
  Ersatzthemen, ein Lehrplan-Gate, der Level-Durchgang je Klasse mit Kriterien-Datei und der
  zweite Prüfdurchgang je Block. Nachgerechnet sind bisher rund 145 von 2736 Aufgaben.
- Messbarer Rückstand: Von den Tipps ab Stufe 4 enthalten in Ref4OHG 425 von 1368 eine fertige
  Gleichung mit Zahlen (31 %), in Mathepfade 90 von 1638 (5 %). Die Zählung ist grob, der
  Abstand nicht.

## Das Kerncurriculum in Kürze

Quellen: `schule/Referenz/Lehrplaene/KC_extern/ma_gym_si_kc_druck.txt` (Sek I, Gymnasium) und
`ma_go_kc_2019.txt` (gymnasiale Oberstufe).

- Sek I legt Kompetenzen je **Doppeljahrgang** fest (7/8, 9/10); die Reihenfolge darin bestimmt
  die Fachkonferenz. Zwischen Spalte 7 und 8 sowie 9 und 10 kann das KC nicht entscheiden.
- Ableitung und Integral beginnen erst in der Sek II. Die Einführungsphase (Kl. 11) hat drei
  Lernbereiche: Beschreibende Statistik, Elementare Funktionenlehre, Ableitungen.
- Die Qualifikationsphase (Kl. 12/13) ist nicht nach Jahrgängen gegliedert, sondern nach
  **gA** und **eA**. Die gemeinsamen Kompetenzen gelten auch für eA.
- Im KC für das Gymnasium kommen nicht vor: Polynomdivision, Newton-Verfahren, Hypothesentest,
  partielle Integration, Substitution mit nichtlinearer innerer Funktion, Additionsverfahren,
  Tangensfunktion, Umfangs-/Mittelpunktswinkelsatz, Vektorprodukt, gebrochen-rationale
  Funktionen. Fakultativ sind unter anderem Kreis- und Kugelgleichung, Ortskurven, Boxplots (EP).

## Teil 1 — Lehrplanabgleich

Die Klassenzuordnung steht nur in `index.html`. **Dateinamen bleiben**, damit die gedruckten
QR-Codes (`Ref4OHG_QR.docx`) und die gespeicherten Lernstände (`spirale-<datei>`) weiter gelten.

### 1a Umzüge zwischen Klassenspalten (6)

| Trainer | bisher | KC | neu |
|---|---|---|---|
| 7-kreise-umfang-flaeche | 7 | 9/10 Kreis- und Körperberechnungen | 9 |
| 8-aehnlichkeit-streckung | 8 | 9/10 Ähnlichkeit | 9 |
| 8-gebrochen-rationale-einfuehrung | 8 | neues Thema, siehe 1b | 10 |
| 10-ganzrationale-funktionen | 10 | EP Elementare Funktionenlehre | 11 |
| 10-ableitung-einfuehrung | 10 | EP Ableitungen | 11 |
| 12-ebenen | 12 | QP eA (Koordinatenform, Normalenvektor) | 13 (eA) |

Die Inhalte werden in der Welle der **Zielklasse** auf deren Niveau gebracht und gegen die
dortigen Nachbarn abgegrenzt (Kreise gegen `10-kreis-kugel`, ganzrationale Funktionen gegen
`11-funktionen-ganzrational`).

### 1b Ersatz lehrplanfremder Inhalte

Ganze Trainer — Dateiname bleibt, Titel und alle 36 Aufgaben neu, der Wechsel steht als Kommentar
im Kopf der Datei:

| Datei | bisher | neu | KC |
|---|---|---|---|
| 8-koerperberechnung | Zylinder, Pyramide, Kegel, Kugel | Flächeninhalte von Dreieck, Parallelogramm, Trapez; Prisma | 7/8 |
| 8-kreise-winkel | Winkelsätze am Kreis | Satz des Thales und besondere Linien im Dreieck (die 6 Thales-Aufgaben bleiben) | 7/8 |
| 8-gebrochen-rationale-einfuehrung | gebrochen-rationale Funktionen | Näherungsverfahren und Grenzprozesse (Heron, 0,9̅ = 1, 1/x) | 9/10 |
| 9-daten-zufall-boxplot | Boxplots | Baumdiagramme und Vierfeldertafeln | 9/10 |
| 10-potenzfunktionen | Potenzfunktionen (doppelt zu Kl. 9 und 11) | Sinussatz und Kosinussatz | 9/10 |
| 10-potenzen-ganzzahlig | negative Exponenten (doppelt) | begrenztes Wachstum und iterative Modelle | 9/10 |
| 11-grenzwerte | Grenzwerte gebrochen-rationaler Funktionen, Stetigkeit | Ableitungsfunktion: Graph und Ableitungsgraph, Ableitungen von sin, cos, √x, 1/x | EP |
| 12-e-funktion | a·bˣ ohne e | e-Funktion gA: (eˣ)′, Produkt- und Kettenregel mit linearer innerer Funktion, Exponentialgleichungen mit ln | QP gA |

Die 36 bisherigen Aufgaben von `12-e-funktion` sind KC-Stoff aus 9/10 und gehen nicht verloren:
Sie ziehen in eine **neue Datei `10-exponentialfunktionen.html`** (77. Trainer, Spalte 10).

Teile von Trainern:

| Datei | ersetzt werden | durch | KC |
|---|---|---|---|
| 7-koerper-volumen | Zylinder, Pyramide (14 Aufgaben) | Prisma: Netz, Oberfläche, Volumen, Rückwärtsrechnen | 7/8 |
| 10-cos-tan-funktion | Tangensfunktion (#13–24) | Kosinusfunktion; Titel „Kosinusfunktion“ | 9/10 |
| 11-ableitungsregeln | Produktregel, eˣ, ln (8 Aufgaben) | Summen- und Faktorregel mit sin, cos, √x, x⁻ⁿ | EP |
| 12-stoch-grundlagen | Sek-I-Wiederholung (Stufe 3–6) | Zufallsgrößen: Erwartungswert, Varianz, Standardabweichung, faire Spiele | QP gA |
| 13-eA-integralrechnung-vertieft | nichtlineare Substitution, partielle Integration (9 Aufgaben) | Rotationsvolumen, uneigentliche Integrale, Integralfunktion | QP eA |
| 13-eA-beurteilende-statistik | Hypothesentests (16 Aufgaben) | Konfidenzintervalle vertieft, Prognose- gegen Konfidenzintervall, Verträglichkeit | QP eA |

Einzelaufgaben (in der jeweiligen Welle): Additionsverfahren in `8-lgs-zwei-variablen`,
Polynomdivision in `11-kurvendiskussion` #11, eˣ in `11-tangenten-normalen` #23, Kreuzprodukt als
Tipp in `12-vektoren-grundlagen` #35, eA-Abstände in `12-geraden-raum` #27/#35 (stattdessen
Ebenen in Parameterform, die nach dem Umzug von `12-ebenen` für gA fehlen), Dreiecksarten und
Winkelsumme in `7-dreiecke-konstruktionen` Stufe 1–3 (stattdessen Grundkonstruktionen, Kongruenz).

### 1c Benennung und Übersicht

- Bei rund 28 Trainern weichen Index-Titel, `<title>` und Kopfzeile voneinander ab. Je Trainer
  gilt künftig **ein** Titel an allen drei Stellen.
- Die Qualifikationsphase heißt in der Übersicht nach dem KC: Spalte 12 „Qualifikationsphase
  (12/13) — gemeinsamer Kern“, Spalte 13 „Qualifikationsphase — zusätzlich eA“. Der Filter
  „Klasse 12“ darf die eA-Spalte nicht mehr ausblenden; „Nur eA“ zeigt den Kern mit.
- Wörter aus anderen Bundesländern im sichtbaren Text werden in der jeweiligen Welle ersetzt:
  „Aufleiten“, „Tafelwerk“, „Anstieg/Anstiegswinkel“, „Mitternachtsformel“, „Peripherie-/
  Zentriwinkel“, „Scheitelform/Normalform“ (KC: Scheitelpunktform, allgemeine Form).

### 1d Bewusst nicht geändert

- Aufteilung 7 gegen 8 und 9 gegen 10, soweit der Trainer im richtigen Band liegt.
- `12-stoch-sigma-umgebungen` bleibt in Spalte 12. Das KC nennt σ-Umgebungen zwar erst bei eA,
  verlangt für gA aber Prognoseintervalle und die Prüfung auf Verträglichkeit; der Trainer wird
  in der Welle darauf zugeschnitten.
- `13-eA-tangenten-kreise` bleibt (fakultative Erweiterung des KC). Folge: Für den
  Gauß-Algorithmus, die Projektion mit Matrizen und abschnittsweise definierte Funktionen (eA)
  gibt es weiterhin keinen eigenen Trainer. **Offen für den Autor**, ob fakultativer Stoff einer
  dieser Kernlücken weichen soll.
- Fakultatives in kleiner Zahl (Ortskurven, Kugel, Integralfunktion gA, Erwartungswert in 7/8),
  Begriffe ohne KC-Wort bei KC-gedecktem Inhalt (Strahlensatz, Krümmung, Kurvendiskussion,
  Steckbrief), Lösungsformel statt p-q-Formel, Φ-Tabelle bei der Normalverteilung.
- `11-funktionen-potenzfunktionen` #29 (dritte Wurzel für negative x) bis zur Entscheidung des
  Autors.

## Teil 2 — Level-Durchgang nach der Rubrik

Rubrik wie in DifferenzierungsEngine und Mathepfade (bindend):

| Stufe | AFB | Kriterium | Verboten |
|---|---|---|---|
| 1 | I | ein Rechenschritt, Objekt gegeben, schöne Zahlen | Kontext |
| 2 | I | Standardverfahren, zwei Schritte | Kontext, Parameter |
| 3 | I | Klassenarbeits-Standard, Zwischenergebnis nötig | Formel im Text |
| 4 | II | Verfahren wählen, Modell aus Text aufstellen oder Umkehraufgabe | Rechenweg im Text, angesagte Rechenart |
| 5 | III | zwei Verfahren kombinieren, Parameter aus zwei Bedingungen oder Fehler im Rechenweg finden | gelieferte Formel, trivialisierende Stelle |
| 6 | III | Fallunterscheidung, Aussage begründet prüfen; Kl. 11–13 im Abiturformat | Muster aus Stufe 1–3 mit Kontext |

Vorgehen, abweichend von Mathepfade nur dort, wo Ref4OHG schon weiter ist:

- **Alle 77 Trainer**, in Wellen je Klasse 7 → 13, Blöcke von höchstens sechs Trainern.
- Je Trainer zuerst alle 36 Aufgaben gegen die KC-Fundstelle lesen (der Abgleich hat 44 Trainer
  nur per Stichprobe gesehen). Dann je Stufe gegen die Rubrik messen.
- Stufe 5 und 6 sind seit dem 19.09. neu. Sie werden **geprüft und nur dort neu geschrieben**,
  wo sie die Rubrik oder den niedersächsischen Jahrgang verfehlen — viele Blöcke stammen aus
  Sachsen-Anhalt, wo der Stoff ein Jahr früher oder später liegt. Stufe 4 wird neu, wo Stufe 3
  und 4 oder 4 und 5 dasselbe verlangen. Stufe 1–3 bleiben und werden nur entdoppelt.
- Tipps ab Stufe 4 nennen den Weg, nicht die fertige Gleichung. MC-Optionen werden über ihren
  Inhalt angesprochen und sind gleich lang. Jede Aufgabe ist aus sich heraus verständlich.
- Je Klasse eine Kriterien-Datei `docs/plans/2026-10-XX-klN-kriterien.md`: je Trainer KC-Beleg,
  was je Aufgabe geändert wurde und warum. Kriterien stehen nicht im öffentlichen HTML.
- Aufgabenformen und Zahlenmuster dürfen aus dem Materialindex adaptiert werden — umformuliert,
  ohne Quellenangaben, kein Rohmaterial im Repo (`schule/CLAUDE.md`).

## Teil 3 — Prüfung je Block (bindend)

1. `python tests/level_check.py --strict` — 0 Fehler, 0 Warnungen
2. `python tests/lehrplan_check.py --strict` — neu, siehe unten
3. Jede Zahl nachgerechnet (Wolfram oder Skript), von einem zweiten, unabhängigen Durchgang
4. `python tests/katex_check.py` für die geänderten Trainer (lokaler Server)
5. Playwright-Suite für die geänderten Trainer, am Ende jeder Welle vollständig
6. Bild erzeugen **und ansehen**, je geänderter Aufgabe mit Tipp und Lösungsweg
7. Ein Commit je Block. Aufgabentexte nie per Heredoc schreiben; Trainer-Dateien nur
   bytegenau ändern (CRLF bleibt).

**Lehrplan-Gate Niedersachsen** (`tests/lehrplan_check.py`, Muster Mathepfade): liest die
Klassenspalte aus `index.html` und meldet Begriffe, die das KC dort nicht kennt — in der Sek I
Vektor, Ableitung, Integral; durchgehend Polynomdivision, Hypothesentest, Signifikanzniveau,
Newton-Verfahren, partielle Integration, Vektorprodukt; in 7/8 Additionsverfahren; dazu als
Warnung die Wörter aus 1c. Ausnahmen stehen mit KC-Beleg in der Datei.

`tests/test_index.py` (Muster Mathepfade) sichert: jeder Trainer steht genau einmal in der
Übersicht, Titel stimmen an allen drei Stellen überein, die Filter zeigen die eA-Spalte.

## Reihenfolge

| Schritt | Inhalt |
|---|---|
| 0 | Werkzeug: Lehrplan-Gate, `test_index.py`, Bild-Bogen für viele Aufgaben |
| 1 | Übersicht: 6 Umzüge, Spaltenköpfe und Filter der Qualifikationsphase, neue Datei `10-exponentialfunktionen` — ein eigener Commit |
| Welle 7 | 9 Trainer; Teil-Ersatz Körper |
| Welle 8 | 8 Trainer; Ersatz Flächeninhalte, Thales |
| Welle 9 | 12 Trainer (Zuzug Kreise, Ähnlichkeit); Ersatz Vierfeldertafeln |
| Welle 10 | 12 Trainer (Zuzug Grenzprozesse, Exponentialfunktionen); Ersatz Sinus-/Kosinussatz, begrenztes Wachstum; Teil-Ersatz Kosinusfunktion |
| Welle 11 | 14 Trainer (Zuzug ganzrationale Funktionen, Ableitung); Ersatz Ableitungsfunktion; Teil-Ersatz Ableitungsregeln |
| Welle 12 | 13 Trainer; Ersatz e-Funktion; Teil-Ersatz Zufallsgrößen |
| Welle 13 | 9 Trainer (Zuzug Ebenen); Teil-Ersatz Integral, Konfidenzintervalle |
| Abschluss | Kriterien zusammenführen, Gesamtmessung, QR-Dokument um den 77. Trainer ergänzen (außerhalb des Repos) |

Nichts geht live, bevor der Autor es sagt. Gearbeitet wird auf einem Branch, der auf
`mc-optionen-und-reste` aufsetzt.
