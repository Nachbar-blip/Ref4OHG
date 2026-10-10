# Briefing für die Wellen (Ref4OHG, KC Niedersachsen und Level-Durchgang)

Dieses Briefing gilt für jeden Block der Wellen. Der Auftrag eines Blocks nennt nur noch die
Trainer, die Verfahren und die Besonderheiten.

## 1. Projekt

Repo `C:\DevProjects\schule\Trainer-Public\Ref4OHG` (Git-Bash, Branch `lehrplan-nds` ist
ausgecheckt — nicht wechseln, **nichts pushen**). 77 HTML-Trainer für das Gymnasium
Niedersachsen (G9, Klassen 7–13). Jeder Trainer `trainer/<datei>.html` enthält ein JS-Array
`AUFGABEN` mit 36 Aufgaben, je 6 auf Stufe 1–6. Die Engine zeigt je Stufe eine zufällige
Aufgabe, mischt MC-Optionen, setzt Texte per innerHTML; Mathe rendert KaTeX. Rein textbasiert,
keine Bilder. Die Aufgaben werden von Schülern benutzt: Sorgfalt geht vor Tempo, jede Zahl muss
stimmen, und „trägt, nichts zu ändern“ ist ein zulässiges Ergebnis.

Die Klassenzuordnung steht nur in `index.html`; **Dateinamen werden nie geändert**
(QR-Codes, Lernstände unter `spirale-<THEMA_KEY>`).

## 2. Pflichtlektüre

Im Plan `docs/plans/2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, vollständig und bindend:

- „Verbindliche Regeln für jede Aufgabe“ (bis einschließlich „Schreiben in Trainer-Dateien“)
- „Prüfschleife je Block“
- „Kriterien-Datei“ und die vier Verfahren („Durchgang“, „Ersatz“, „Teil-Ersatz“, „Umzug“)
- der Abschnitt deiner Welle („### Task N: …“)

Im Lehrplanabgleich `docs/audit/lehrplanabgleich-nds-2026-10-10.md`: die Zeilen deiner Trainer in
Abschnitt 2 und 3 und die dort genannten KC-Kürzel in Abschnitt 1. **Das KC selbst im Wortlaut
lesen** (Zeilennummern stehen im Abgleich):
`C:\DevProjects\schule\Referenz\Lehrplaene\KC_extern\ma_gym_si_kc_druck.txt` (Sek I) und
`ma_go_kc_2019.txt` (Oberstufe). Das KC geht vor Plan und Abgleich; Abweichungen vermerken.

Die Gates lesen, bevor du schreibst: in `tests/level_check.py` die Funktionen `pruefe_trainer`,
`tipp_verraet_loesung`, `richtige_option_zu_lang`, `verweis_auf_andere_aufgabe`, `ascii_ersatz`,
`optionsbuchstabe`, `html_frisst_text`, `mathe_markup_ausserhalb`; dazu `tests/lehrplan_check.py`.

## 3. Arbeitsweise

- Jeden Trainer zuerst ganz lesen: `python tests/zeige.py . <datei>.html:1 … <datei>.html:36`.
- Änderungen an einzelnen Feldern: Datenmodul (Python-Raw-Strings, ein Backslash) und
  `python tests/aufgaben_patch.py . <modul.py> --dry`, dann ohne `--dry`.
- Neue oder ganz neu gefasste Aufgaben: JSON-Liste (im JSON ist der Backslash zu verdoppeln) und
  `python tests/aufgaben_setzen.py trainer/<datei>.html <daten.json>`. Danach an zwei, drei
  Aufgaben mit `zeige.py` nachsehen, dass `\(…\)` mit **einem** Backslash ankommt.
- Datenmodule, JSON, Skripte und Bilder liegen im Scratchpad deines Blocks (steht im Auftrag),
  mit dem Write-Tool angelegt. **Nie Bash-Heredoc** für Texte mit Backslash (er frisst sie, auch
  quotiert). **Nie Hilfsdateien in `trainer/`.**
- Kopfzeilen (`<title>`, `THEMA_CONFIG.name`) bytegenau per kleinem Python-Skript ändern (Datei
  als Bytes lesen und schreiben). Titel müssen an drei Stellen gleich sein: `<title>… - Ref4OHG`,
  `THEMA_CONFIG.name`, Index-Text (`theme-name`). Danach den Trainer aus `NOCH_UNEINHEITLICH` in
  `tests/test_index.py` streichen. `index.html` ist LF, die meisten Trainer CRLF —
  `git diff --stat` muss klein bleiben.
- Sinngleiche Aufgaben vermeiden: innerhalb des Trainers und zu den Nachbarn derselben Spalte.
  Vorlagen aus den Schwesterprojekten (`../Mathepfade/trainer/`, `../DifferenzierungsEngine/trainer/`,
  eigene Arbeit) dürfen für Aufgaben**formen** dienen — Zahlen ändern, am KC Niedersachsen messen.
- Der lokale Materialindex (`C:\DevProjects\schule\Material-Lokal\Index\unified_material_index.json`)
  darf als Vorlage für Aufgabenformen und Zahlenmuster gelesen werden. **Nichts daraus wörtlich
  übernehmen, keine Quellenangaben, nichts davon ins Repo.**

## 4. Nachrechnen

Für jede neue oder inhaltlich geänderte Aufgabe: ein sympy-Skript im Scratchpad, das den
hinterlegten Wert (bei MC: die als richtig markierte Option, und die Falschheit der Distraktoren,
soweit rechnerisch entscheidbar) **unabhängig vom Lösungsweg** herleitet und vergleicht. Die
Ausgabe gehört in den Bericht, ebenso, was sich nicht rechnerisch prüfen ließ.

## 5. Prüfschleife und Sichtprüfung

Server im Hintergrund im Repo-Wurzelordner: `python -m http.server 8765 --bind 127.0.0.1`
(am Ende beenden). Dann:

```bash
python tests/level_check.py --strict                 # Exit 0, im ganzen Projekt keine Warnung
python tests/lehrplan_check.py --strict trainer/<dateien des blocks>
python tests/katex_check.py trainer/<dateien des blocks>
python -m pytest tests/test_level_check.py tests/test_lehrplan_check.py tests/test_index.py tests/test_aufgaben_setzen.py -q -o addopts=""
cd tests && python -m pytest test_trainer.py -k "<datei1> or <datei2>" -q && cd ..
python tests/bogen.py . <scratchpad>/sicht/<name> <specs.txt> --tipp --weg --zeilen 3
```

`specs.txt`: je Zeile `datei.html:id` für **jede** neue oder geänderte Aufgabe. Jede erzeugte PNG
mit dem Read-Tool **ansehen**: zerbrochene Formeln, wörtlich angezeigtes Markup, abgeschnittener
Text, einsame Satzzeichen nach Formeln, falsche Umbrüche. Bei geänderten Kopfzeilen ein Bild mit
`--kopf`. Ohne `-o addopts=""` legt pytest im Wurzelordner einen unerwünschten Ordner an.

Das Lehrplan-Gate prüft nur eine Wortliste. Grün heißt nicht KC-konform — maßgeblich ist dein
Lesen gegen das KC und die Liste der Aufgaben aus dem Abgleich, die im Bericht einzeln als
erledigt oder begründet belassen aufzuführen sind.

## 6. Qualitätsmaßstab

- Jede Stufe verlangt erkennbar mehr als die vorige (Rubrik im Plan). Klasse 11–13: Stufe 6 im
  Abiturformat des hilfsmittelfreien Teils (begründen, beurteilen, Zusammenhänge).
- Höchstens 3 MC je Stufe in Stufe 5 und 6. Vier Optionen, etwa gleich lang; jeder Distraktor
  entspringt einem typischen Fehlweg und ist **als Aussage eindeutig falsch** — keine wahren
  Halbsätze mit schwacher Begründung, keine zweite vertretbare Antwort.
- Tipps ab Stufe 4 nennen den Weg, nie den Lösungswert und nie die fertige Gleichung.
  Lösungswege zeigen die Schritte.
- Jede Aufgabe ist aus sich heraus verständlich (die Engine wählt zufällig).
- Numerische Antworten: Rundungsvorgabe in der Frage, `toleranz` so eng, dass der typische
  Fehlweg nicht durchgeht.
- Niedersächsische Fachsprache (Liste im Plan). Koordinaten in der Geometrie \(x_1, x_2, x_3\).

## 7. Kriterien-Datei und Commit

- Je Trainer einen Abschnitt in `docs/plans/2026-10-10-kl<N>-kriterien.md` (Format im Plan):
  KC-Beleg, „gelesen: alle 36“, je Aufgabe ab Stufe 4 eine Zeile (trägt / geändert und warum),
  Stufe 1–3 nur bei Befund. Existiert die Datei schon, anhängen.
- **Ein Commit je Block**, nur die eigenen Dateien (`git add <pfade>`), Nachricht im Auftrag,
  letzte Zeile `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Vor dem Commit müssen
  alle Gates grün sein; am Ende ist `git status --short` leer.
- Entscheidungen, die dem Autor zustehen (fachliche Geschmacksfragen, Lehrwerksfragen), nicht
  selbst treffen: konservativ lassen und im Bericht unter „Für den Autor“ nennen.
- Wenn etwas unklar ist oder Plan, KC und Gates einander widersprechen: nicht raten — im Bericht
  als Frage nennen und den Rest erledigen.

## 8. Bericht

1. Was geändert wurde: je Trainer Anzahl geänderter und neuer Aufgaben, Titel, Besonderheiten;
   Commit-Hash; `git status --short`.
2. Lehrplan: je Trainer Urteil nach dem Lesen aller 36 Aufgaben; die Aufgaben-IDs aus dem
   Abgleich einzeln als erledigt / belassen (mit Grund); eigene Funde.
3. Nachrechnen: Zusammenfassung der Skriptausgabe, nicht prüfbare Aufgaben.
4. Letzte Zeilen aller Gates und Tests.
5. Sichtprüfung: was auf den Bildbögen zu sehen war, Pfade der PNGs und der `specs.txt`.
6. Für den Autor; offene Fragen; was dir für spätere Wellen aufgefallen ist.

---

## Briefing für den zweiten Prüfdurchgang

Du prüfst die Arbeit eines anderen Agenten an Mathematik-Übungsaufgaben (Gymnasium
Niedersachsen). **Nur lesen und berichten**: nichts im Repo ändern, nichts committen, keinen
Server starten. Eigene Skripte nur im genannten Scratchpad-Ordner.

Du bekommst eine Vorlage mit den ausgewerteten Aufgaben (Kopfzeile `===== datei #id L<Stufe> <typ>`,
dann FRAGE, bei MC die Optionen mit `*` an der hinterlegten richtigen, bei numerischen Aufgaben
LOESUNG und Toleranz, dann TIPP und WEG; `\(…\)` und `$$…$$` sind LaTeX; die Optionen werden den
Schülern in zufälliger Reihenfolge gezeigt). Dazu die Rubrik (Plan, Abschnitt „Verbindliche
Regeln für jede Aufgabe“) und die KC-Fundstelle. Die Begründungen des Schreibenden bekommst du
bewusst nicht.

Prüfe jede Aufgabe:

1. Rechne selbst nach (sympy oder von Hand), statt dem Lösungsweg zu glauben: hinterlegte Lösung,
   Zwischenschritte, Rundung, Toleranz (geht der typische Fehlweg durch?).
2. MC: Ist die markierte Option richtig und vollständig? Ist **jeder** Distraktor als Aussage
   eindeutig falsch — oder wahr, vertretbar, nur schwach begründet?
3. Stufe: Verlangt die Aufgabe, was die Rubrik für ihre Stufe verlangt? Verlangt Stufe 4 anderes
   als Stufe 3, Stufe 5 anderes als Stufe 4? Sinngleiche Paare (gleiche Aufgabe, andere Zahlen)?
4. Lehrplan: Liegt die Aufgabe im genannten KC-Lernbereich und Niveau? Begriffe oder Verfahren,
   die das KC an dieser Stelle nicht kennt?
5. Tipp ab Stufe 4: nennt er den Weg — oder den Wert bzw. die fertige Gleichung?
6. Ist die Aufgabe aus sich heraus verständlich und eindeutig? Fehlende Voraussetzungen
   (Definitionsbereich, Parameterbedingungen, Einheiten, Rundung)?
7. Sprache, Fachwörter, LaTeX-Fehler, Widersprüche zwischen Frage, Optionen, Tipp und Lösungsweg.

Nicht melden: Geschmack, Wünsche nach anderen Aufgaben.

Bericht: nur Aufgaben mit Befund, je Eintrag `datei #id — FEHLER / MANGEL / HINWEIS`
(FEHLER = fachlich falsch, zwei richtige Antworten, falscher Lösungswert, außerhalb des KC;
MANGEL = missverständlich, Stufe verfehlt, Tipp verrät, unstimmig), was genau nicht stimmt und
ein Änderungsvorschlag **im Wortlaut**. Am Ende: wie viele Aufgaben vollständig geprüft, wie
viele ohne Befund; und eine klare Trennung von „nachgerechnet“ und „nur für plausibel gehalten“.
