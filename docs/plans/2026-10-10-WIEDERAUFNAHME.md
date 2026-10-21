# Wiederaufnahme: KC Niedersachsen und Level-Durchgang

> **VERALTET (Vermerk 2026-10-21):** Diese Wiederaufnahme-Notiz zeigt den Zwischenstand 52/77, nichts gepusht. Aktueller Stand: `2026-10-10-STAND.md` (77/77 fertig, live). Der hier genannte Ordner `Ref4OHG-Arbeitsstand-2026-10` wurde beim Ordner-Umbau gelöscht.

Geschrieben am 2026-10-11, 22:15 Uhr, zum Weiterarbeiten in einer **neuen Sitzung**. Diese Datei
sagt, was zuerst zu lesen ist, was gilt, wo das Arbeitsmaterial liegt und wie ein Block
beauftragt wird. Der laufende Stand steht in `2026-10-10-STAND.md`.

## 1 Wo wir stehen

- **52 von 77 Trainern fertig** (Spalte 7: 9/9, 8: 8/8, 9: 12/12, 10: 12/12, 11: 6/14,
  12: 3/13, 13: 2/9). Es läuft kein Agent, das Arbeitsverzeichnis ist sauber.
- Branch `lehrplan-nds` (lokal, baut auf `mc-optionen-und-reste` auf). `master` (`ffccaf5`) ist
  live. **Nichts ist gepusht.**
- Gates am 2026-10-11, 21:50 Uhr: `level_check --strict` Exit 0 (alle 77 „ok“); Lehrplan-Gate
  32 Fehler / 16 Warnungen, alle in den 25 offenen Trainern; pytest (Gates, Index, Werkzeug)
  92 bestanden.
- Nicht gelaufen: volle Playwright-Suite (zuletzt vor `8138027`); `katex_check` über alle 77 mit
  der am 2026-10-11 erweiterten Fehlererkennung.

## 2 Was der Autor festgelegt hat (bindend, bis er etwas anderes sagt)

1. **Die 25 offenen Trainer werden erst gestartet, wenn er es sagt.** („höre vor den 25 trainer
   … erst einmal auf“, 2026-10-11.)
2. **Kein Push** von `mc-optionen-und-reste` oder `lehrplan-nds` ohne sein ausdrückliches Wort.
3. **Höchstens drei Block-Agenten gleichzeitig**, je Block-Agent höchstens ein Unteragent
   (Prüfer). Hintergrund: Tageslimit des Abos; sieben parallele Agenten haben es in einer halben
   Stunde aufgebraucht.
4. **Keine Thermowache, keine Drosselung** — der Laptop darf ausgehen. Dafür Zwischenstände
   sichern: je Trainer ein Commit, je Block eine `STAND.md` im Scratchpad.
5. **Statusmeldungen**: was fertig ist, was fehlt, wie lange noch — keine Temperaturen.
6. Sichtprüfung als Bild vor jeder Übergabe; Materialindex strikt lokal (keine Quellen, keine
   wörtlichen Verlagspassagen, keine Indexdaten im Repo).

## 3 In der neuen Sitzung zuerst

1. Lesen: diese Datei, `2026-10-10-STAND.md` (vor allem „Für den Autor“ und die Notizen je
   Block), `2026-10-10-briefing-wellen.md` (Arbeitsvertrag der Block-Agenten, Abschnitte 1–10),
   im Plan `2026-10-10-lehrplan-nds-und-level-durchgang-plan.md` die Tasks 7 bis 10.
2. Prüfen: `git status --short` (leer), `git log --oneline -5` (oben `Stand: Halt bei 52 von 77`
   oder neuer), `python tests/level_check.py --strict`, `python tests/lehrplan_check.py | tail -1`.
3. Server: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/index.html`. Kommt
   nicht 200, im Repo-Wurzelverzeichnis im Hintergrund starten: `python -m http.server 8765`.
4. Den Autor fragen, ob die 25 offenen Trainer jetzt drankommen (Punkt 2.1), und seine offenen
   Entscheidungen ansprechen (Abschnitt 7).

## 4 Arbeitsmaterial der bisherigen Sitzung

Der Scratchpad der Sitzung vom 10./11. Oktober ist gesichert unter

    C:\DevProjects\schule\Trainer-Lokal\Ref4OHG-Arbeitsstand-2026-10\

(lokal, kein Repo, 408 MB, ohne die temporären Bilder). Wo Briefing, STAND oder Kriterien-Dateien
`…\scratchpad\w10a2\` oder ähnlich nennen, ist dieser Ordner gemeint. Er ist **Nachschlagewerk**
(nur lesen); neue Blöcke bekommen einen eigenen Unterordner im Scratchpad der neuen Sitzung.

- Je Block ein Ordner `w7a … w13c`: Datenmodule `d_*.py`, Nachrechen-Skripte `rechne_*.py`,
  `alles.py`/`bau.py` (bauen einen Trainer aus dem Datenmodul neu und rechnen nach), Prüfpakete
  und Prüfberichte `pruef_*`, Bilder `sicht\`, Originale ersetzter Trainer `orig\`, `STAND.md`.
- Rechen-Bibliotheken als Vorbild: `w10a1\tlib.py` (Dreiecke), `w9b2\rlib.py` (Kreis, Körper),
  `w10a2\klib.py`, `w10c\wlib.py` (Wachstum), `w11a1\slib.py` (Statistik), `w11a2\rlib.py`
  (Funktionen), `w12b\vlib.py` und `w12b\tx.py` (Vektoren, Text-Bausteine für Spaltenvektor,
  Punkt, Gerade, Ebene), `w13c\rechne_nv.py` (Normalverteilung).
- Werkzeuge des Auftraggebers im Hauptordner (Aufruf aus dem Repo-Wurzelverzeichnis):
  - `titel_setzen.py <datei.html> x "<neuer Titel>"` — Titel an allen drei Stellen
    (vorher `export PYTHONIOENCODING=utf-8`); `titel_zeigen.py <datei.html> …` — Kontrolle.
  - `abschnitt_ordnen.py name1 name2 …` — Zeilen eines Abschnitts der Übersicht ordnen.
  - `index_spalte_bild.py <spalte> <ziel.png>` — Spalte der Übersicht als Bild.
  - `bericht_sichern.py <tasks-ordner> <agent-id> <ziel>` — Schlussbericht eines Unteragenten
    aus seinem Protokoll holen (nach Abbruch des Eltern-Agenten).
  - `katex_gate_probe.py` — belegt, dass `tests/katex_check.py` rote Fehlbefehle findet.
- Vollständiges Protokoll der Sitzung:
  `C:\Users\Gnurp\.claude\projects\C--DevProjects-schule-Trainer-Public\2ced28fd-5bcc-4a36-8efe-77696bc2222b.jsonl`

## 5 Offene Blöcke (25 Trainer)

Je Block zwei bis drei Trainer; Kriterien-Datei je Block (Parallelbetrieb). Besonderheiten aus
dem Plan (Task 7 bis 9) **und** aus den Berichten der fertigen Blöcke:

| Block | Trainer | Kriterien-Datei | KC |
|---|---|---|---|
| 11B1 | `10-ableitung-einfuehrung`, `11-grenzwerte` (Ersatz → „Ableitungsfunktion“) | `kl11-kriterien-b1.md` | GO, Einführungsphase (Z. 1730–1761) |
| 11B2 | `11-ableitungsregeln` (Teil-Ersatz #19, 25, 28, 29, 30, 34, 35, 36), `11-tangenten-normalen` | `kl11-kriterien-b2.md` | GO, Einführungsphase |
| 11C1 | `11-monotonie-kruemmung`, `11-extrempunkte-wendepunkte` | `kl11-kriterien-c1.md` | GO, Einführungsphase |
| 11C2 | `11-extremwertaufgaben`, `11-kurvendiskussion` | `kl11-kriterien-c2.md` | GO, Einführungsphase |
| 12A1 | `12-steckbriefaufgaben`, `12-stammfunktionen`, `12-bestimmtes-integral` | `kl12-kriterien-a1.md` | GO, QP gA (Z. 1835–1851) |
| 12A2 | `12-flaechenberechnung`, `12-e-funktion` (nur Gegenlesen), `12-wachstum-begrenzt` | `kl12-kriterien-a2.md` | GO, QP gA |
| 12C1 | `12-stoch-grundlagen` (Teil-Ersatz Stufe 3–6 → „Zufallsgrößen & Erwartungswert“), `12-stoch-bedingte-wahrscheinlichkeit` | `kl12-kriterien-c1.md` | GO, QP gA (Z. 1966–1993) |
| 12C2 | `12-stoch-binomialverteilung`, `12-stoch-sigma-umgebungen` | `kl12-kriterien-c2.md` | GO, QP gA |
| 13A | `13-eA-integralrechnung-vertieft` (Teil-Ersatz), `13-eA-funktionenscharen`, `13-eA-wachstumsmodelle` | `kl13-kriterien-a.md` | GO, QP eA (Z. 2033–2050) |
| 13B1 | `12-ebenen` (Umzug, „Ebenen (Koordinatenform, eA)“), `13-eA-ebenen-lagebeziehungen` | `kl13-kriterien-b1.md` | GO, QP eA (Z. 2139–2167) |
| 13B2 | `13-eA-abstaende`, `13-eA-tangenten-kreise` (fakultativ) | `kl13-kriterien-b2.md` | GO, QP eA |

Dazu aus den fertigen Blöcken (Einzelheiten in STAND und in den Kriterien-Dateien):

- **11B, 11C:** Stufe 6 hat Abiturformat. Abgrenzen gegen `11-funktionen-ganzrational` #29, #35,
  #36 und `10-ganzrationale-funktionen` #19, #36 (Verlauf aus faktorisierter Form,
  Vorzeichenbereiche, Überlagerung — dort ohne Ableitung). Die Globalverhalten-Aufgaben
  `11-grenzwerte` #7–#10 sind schon in `10-ganzrationale-funktionen` aufgegangen. Keine
  Polynomdivision (`11-kurvendiskussion` #11, Lösungsweg #21); `11-tangenten-normalen` #23
  (e^x) ersetzen, „Anstiegswinkel“ → „Steigungswinkel“. Die beiden 11B-Blöcke brauchen einen
  gemeinsamen Zuschnitt (Einführung / Ableitungsfunktion / Regeln / Tangenten): entweder
  nacheinander fahren oder den Zuschnitt im Auftrag vorgeben.
- **12A2:** `12-wachstum-begrenzt` gegen den Klasse-10-Trainer „Begrenztes Wachstum & iterative
  Modelle“ (`10-potenzen-ganzzahlig`, iterativ, „Grenze G“, ohne e-Funktion) abgrenzen.
  `12-e-funktion` hat noch von Hand gesetzte Formelgruppen `\({…}\)` (niedrige Priorität).
- **12C1:** `12-stoch-bedingte-wahrscheinlichkeit` wiederholt auf Stufe 1–2, in #19, #20 und
  #31–#36 den Stoff des Spalte-9-Trainers „Baumdiagramme & Vierfeldertafeln“
  (`9-daten-zufall-boxplot`); dort Schreibweise, formale Unabhängigkeit, Stufenabstand prüfen.
- **12C2:** `12-stoch-sigma-umgebungen` #21, #22, #24, #28, #30 (σ-Umgebung für relative
  Häufigkeiten) sind eA und im Trainer „Prognose- & Konfidenzintervalle (eA)“ abgedeckt; #5
  trägt „Signifikanzniveau“, #36 „abgelehnt“. „2σ ≈ 95,4 %“ nicht als „95 %“ bezeichnen.
  `12-stoch-binomialverteilung` #27: „Tafelwerk“ → „Formelsammlung“.
- **13B1, 13B2:** Koordinaten \(x_1, x_2, x_3\). Der Kern trägt jetzt Ebenen in Parameterform
  (`12-geraden-raum`, 14 Aufgaben) — `12-ebenen` beginnt mit dem Formwechsel.
  `12-skalarprodukt` #25 übt „Vektor senkrecht auf zwei Vektoren“ über zwei Gleichungen (die
  Technik, die statt des Kreuzprodukts gebraucht wird: `12-ebenen` #13–18,
  `13-eA-ebenen-lagebeziehungen` #22 und Tipp #15). Der Kern hat nur Abstand Punkt–Punkt und
  Winkel Gerade–Gerade; alles Weitere ist frei für eA.
- **13A:** „DGL“ im Titel ausschreiben; Teil-Ersatz in `13-eA-integralrechnung-vertieft`
  (#25, 26, 27, 29, 30, 36 nichtlineare Substitution; #31, 32, 35 partielle Integration) →
  Rotationsvolumen, uneigentliche Integrale als Grenzwerte, Integralfunktion.
- **Titel:** kurz halten und am Wortanfang unterscheidbar — die mehrspaltige Übersicht kürzt
  lange Titel mit „…“. Ob „(eA)“ in den Titeln der eA-Spalte stehen soll, ist offen (Abschnitt 7).

## 6 Auftrag an einen Block-Agenten (Vorlage)

Agententyp `general-purpose`, im Hintergrund. Platzhalter in spitzen Klammern ersetzen; die
Besonderheiten aus Abschnitt 5 und dem Plan ausformulieren.

    Du arbeitest im Repo `C:\DevProjects\schule\Mathe\Trainer-Public\Ref4OHG` (Branch `lehrplan-nds`,
    lokal; NICHTS pushen, Branch nicht wechseln). Ref4OHG sind 77 HTML-Mathe-Trainer für ein
    niedersächsisches Gymnasium; sie werden Welle für Welle am Kerncurriculum Niedersachsen (KC)
    und an einer Stufen-Rubrik (6 Stufen × 6 Aufgaben) überarbeitet. 52 Trainer sind fertig.
    Andere Block-Agenten arbeiten gleichzeitig im selben Arbeitsverzeichnis. Dein Auftrag ist
    <Block>: <Anzahl> Trainer.

    ## Zuerst lesen (bindend, in dieser Reihenfolge)
    1. `docs/plans/2026-10-10-briefing-wellen.md` — vollständig (Rubrik, Nachrechnen,
       Prüfschleife, Sichtprüfung als Bild, Kriterien-Datei, Commit, Berichtsform, Abschnitt 9
       „Sichern und Parallelbetrieb“, Abschnitt 10 „Erfahrungen“).
    2. `docs/plans/2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, Abschnitt „<Task n>“;
       im Design `…-design.md` Abschnitt 1d (gA-Kern gegen eA), falls Qualifikationsphase.
    3. `docs/audit/lehrplanabgleich-nds-2026-10-10.md` — alle Zeilen zu deinen Trainern.
    4. KC-Text `C:\DevProjects\schule\Verwaltung\Lehrplaene\KC_extern\ma_go_kc_2019.txt`
       (<Lernbereich, Zeilen>) im Wortlaut.
    5. Eine fertige Kriterien-Datei als Vorbild (`docs/plans/2026-10-10-kl11-kriterien-a2.md`)
       und die Nachbartrainer, gegen die du abgrenzt: <Liste>.

    ## Die Trainer
    <je Trainer: Datei, Durchgang / Teil-Ersatz / Ersatz, Besonderheiten, Abgrenzung>
    Stufe 6 hat Abiturformat (hilfsmittelfreier Teil): begründen, beurteilen, Zusammenhang
    herstellen. Lege zuerst den Zuschnitt fest und schreibe ihn in deine Kriterien-Datei, bevor
    du Aufgaben setzt.

    ## Vorgaben
    - Parallelbetrieb: Du änderst nur deine Trainer und deine Kriterien-Datei
      `docs/plans/2026-10-10-<…>.md`. `index.html`, `tests/test_index.py` und die Titel in den
      Trainern nicht ändern — empfohlene Titel im Bericht nennen (kurz, ohne Abkürzungen).
      Commit nur mit ausdrücklichen Pfaden (`git commit -F nachricht.txt -- pfad1 pfad2`).
    - Sichern: Der Rechner kann jederzeit ausgehen. Je Trainer ein Commit, sofort wenn er
      fertig ist. `STAND.md` im Scratchpad führen (erledigt / läuft / danach).
    - Nur Text und KaTeX, keine Bilder; Tabellen als KaTeX-`array` mit `\footnotesize`, bei
      360 px im Bild prüfen; lange Formeln teilen. Jede Aufgabe aus sich heraus eindeutig.
    - Die Engine liest Zahleneingaben mit `parseFloat` (Komma → Punkt): eine Zahl je Aufgabe.
      Rundung und Toleranz mit Fehlweg-Netz und Zufallsnetz (Briefing Abschnitt 4 und 10).
    - Materialindex `C:\DevProjects\schule\Mathe\Material\Index\unified_material_index.json`
      nur als Formvorlage: keine Quellenangaben, keine wörtlichen Passagen, keine Indexdaten in
      die Trainer. Einmal laden, Treffer in eine Scratchpad-Datei.
    - Hilfsdateien nur im Scratchpad `<Scratchpad der Sitzung>\<block>\`. Niemals in
      `trainer/`. Skripte und Patches nur über Write/Edit — kein Heredoc, auch kein leerer.
      Vorbilder (nur lesen): `C:\DevProjects\schule\Trainer-Lokal\Ref4OHG-Arbeitsstand-2026-10\<ordner>\`.
    - Prüfschleife mit Maß: höchstens EIN Unteragent zur Zeit; je Trainer ein zweiter Prüfer
      (frischer Agent, ohne Browser, „Briefing für den zweiten Prüfdurchgang“) über alle 36,
      die Schwestertrainer als Vergleichstext; höchstens ein Nachtrag für Aufgaben mit neuen
      Zahlen. Vorschläge nachrechnen, bevor du sie übernimmst.
    - Sichtprüfung: alle Aufgaben als Bildbogen mit Tipp und Lösungsweg (`tests/bogen.py`), die
      PNGs mit dem Read-Tool ansehen; 360 px für Tabellen und lange Formeln; geänderte Aufgaben
      in der Endfassung noch einmal.
    - Gates vor jedem Commit: `python tests/level_check.py --strict`;
      `python tests/lehrplan_check.py --strict trainer/<datei>.html`;
      `python tests/katex_check.py trainer/<datei>.html`;
      `python -m pytest tests/test_level_check.py tests/test_lehrplan_check.py tests/test_aufgaben_setzen.py -o addopts="" -q`;
      in `tests/`: `python -m pytest test_trainer.py -k "<trainer>" -q`.
    - Commit-Nachricht „Level-Durchgang <Spalte> <Block>: <Thema>“ bzw. „Ersatz/Teil-Ersatz …“,
      letzte Zeile `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
    - Nicht anfassen: `docs/plans/2026-10-10-STAND.md`, Briefing, `spirale-engine.js`,
      `spirale.css`, andere Trainer, andere Kriterien-Dateien.

    ## Bericht (Schlussnachricht, Form aus Briefing Abschnitt 8)
    1 Was geändert wurde (Commits, empfohlene Titel, Zuschnitt) · 2 Lehrplan · 3 Nachrechnen ·
    4 Gates und Tests (letzte Zeilen) · 5 Sichtprüfung (angesehen / nicht angesehen) ·
    6 Bilanz der Prüfdurchgänge · 7 Für den Autor. Trenne „nachgerechnet“ von „für plausibel
    gehalten“.

Nach jedem Block macht der Auftraggeber selbst: `git log`/`git status`, drei bis vier Aufgaben
nachrechnen, einen Bildbogen ansehen, Titel an drei Stellen setzen, den Trainer aus
`NOCH_UNEINHEITLICH` in `tests/test_index.py` streichen, `python -m pytest tests/test_index.py
-o addopts="" -q`, Spalte der Übersicht im Bild ansehen, STAND fortschreiben, committen.
Wird ein Block-Agent unterbrochen (Limit, Ausfall), in derselben Sitzung per Nachricht an ihn
fortsetzen; Berichte verwaister Prüfer mit `bericht_sichern.py` in den Blockordner legen.

## 7 Offene Entscheidungen des Autors (Auswahl; vollständig in STAND „Für den Autor“)

1. „(eA)“ im Titel der eA-Trainer behalten oder überall streichen (Spaltenkopf und Marke sagen
   es schon)?
2. Konfidenzintervalle: Näherung mit h und Faktor 1,96 (jetzt Regelfall) oder Ungleichung für p?
3. Dritte Wurzel aus negativen Zahlen (`11-funktionen-potenzfunktionen` #29,
   `9-potenzen-wurzeln` #31) — definiert oder nicht?
4. „Asymptote“ im Klasse-10-Trainer Exponentialfunktionen zurück?
5. Boxplot in der Einführungsphase (7 von 36 Lagemaße-Aufgaben) — unterrichtet oder nicht?
6. Enge oder weite Lesart des gA-Kerns bei Ebenen (`12-geraden-raum` #21, #22, #29, #35).

## 8 Abschluss (Plan Task 10), wenn alle 77 fertig sind

- `level_check --strict` ohne Warnung, `lehrplan_check --strict` Exit 0, `katex_check` über
  alle 77, `cd tests && python -m pytest -q` (volle Playwright-Suite, rund 35 Minuten).
- `NOCH_UNEINHEITLICH` leer; Test `len(klassen_aus_index()) == 77` ergänzen.
- Kriterien-Dateien je Klasse zusammenführen (kl10 mit -c und -e; kl11, kl12, kl13 aus den
  Blockdateien) oder als Blockdateien belassen und in STAND verzeichnen.
- Nachmessung im Abgleich-Dokument, Plan-Status; dem Autor melden: `Ref4OHG_QR.docx` (Eintrag
  für `10-exponentialfunktionen`, geänderte Titel). Kein Push ohne Freigabe.
