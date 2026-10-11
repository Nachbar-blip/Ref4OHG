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

## 9. Rechner schonen und sichern (bindend)

Der Arbeitsrechner ist ein Laptop mit stark eingeschränkter Kühlung (Stand 2026-10-11 mittags):
Schon ein einzelnes Python-Skript, das einen Kern eine Minute auslastet, treibt ihn auf 96 °C.
Eine Thermowache hält deshalb ab 60 °C alle `python`-, `node`- und
`chrome-headless-shell`-Prozesse an und lässt sie unter 52 °C weiterlaufen; ab 80 °C beendet
sie die Test-Browser, als letzte Stufe schickt sie den Rechner in den Ruhezustand.

- Rechenläufe dauern dadurch in der Wanduhr etwa viermal so lang (45 s CPU ≈ 3 min). Das ist
  gewollt. Bash-Aufrufen mit Python, pytest oder Playwright ein großzügiges `timeout` geben
  (bis 600000 ms); nach einem Timeout einmal wiederholen, nie parallel starten.
- Rechenlast klein halten: keine Brute-Force-Suchen über große Bereiche, float statt sympy, wo
  es reicht; Nachrechnen in Portionen (je Stufe ein Aufruf), Ergebnisse in Dateien schreiben.

- Höchstens **ein** Playwright-Lauf zur Zeit, nichts parallel, keine volle Playwright-Suite.
  `katex_check` und `test_trainer.py -k …` nur für die eigenen Trainer und nur am Ende eines
  Teilblocks; `bogen.py` in Portionen von höchstens 6 Aufgaben, nur für Geändertes.
- Bricht ein Browserlauf mit `TargetClosedError` oder ähnlich ab, hat die Thermowache
  eingegriffen: zwei Minuten warten, dann in kleineren Portionen wiederholen.
- Ein Server läuft meist schon auf Port 8765 (prüfen mit
  `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/index.html`). Läuft er, benutzen
  und **nicht** beenden; läuft er nicht, selbst im Hintergrund starten.
- Zwischenstände sofort auf Platte (Datenmodule, JSON, Nachrechen-Skripte, eine `STAND.md` im
  Scratchpad). In Teilblöcken von zwei bis drei Trainern arbeiten und **je Teilblock committen**
  (fertig geprüft, Gates grün) — bei einem Ausfall geht sonst alles Ungesicherte verloren.

## 10. Erfahrungen aus den ersten Blöcken

- Der häufigste Befund: Stufe 4 ist nur „das nächste Teilthema“ auf dem Niveau von Stufe 1/2
  (ein Schritt, Formel oder fertige Rechnung im Tipp). Das ehrlich benennen und ändern.
- Nachrechnen heißt auch Fehlwege prüfen: Ist die Lösung zufällig gleich einer gegebenen Zahl?
  Liefert ein verkehrter Weg (falsche Zuordnung, Vorzeichenfehler, Halbieren statt Wurzel)
  denselben Wert? Dann Zahlen ändern.
- Dem zweiten Prüfer die Stufen 1–3 als reine Vergleichsdatei mitgeben (nicht zum Prüfen),
  sonst kann er Stufe 3 gegen 4 und Dubletten zu den unteren Stufen nicht beurteilen.
- Formeln nicht von Hand „umbruchsicher“ machen (keine `\({…}\)`-Gruppen, keine Satzzeichen in
  der Formel): Umbruch, Überlauf und Satzzeichen regelt seit Commit `8138027` die Engine.
- Zwei Trainer derselben Spalte dürfen nicht dieselbe Aufgabenidee tragen (z. B. „erst +20 %,
  dann −20 %“ in beiden Prozent-Trainern): entflechten.
- Als „trägt“ belassene Altaufgaben der Stufen 5 und 6 so streng gegen Stufe 1–4 halten wie
  neue: In Welle 9 waren sechs von neun Mängeln solche belassenen Aufgaben.
- Liegt ein ganzer Trainer eine Stufe zu tief, genügt es nicht, Stufe 4–6 zu ersetzen: die alten
  Aufgaben der Stufen 4/5 gehören dann nach 2/3.
- Numerische Antworten, die keine ganze Zahl sind: „als Dezimalzahl“ in die Frage schreiben —
  die Engine liest „5/2“ als 5 (`parseFloat`).
- Begriffs-MC brauchen den Zusatz „in jedem …“ bzw. den Ausschluss des Sonderfalls, sonst ist
  ein Distraktor im Sonderfall wahr.
- Zwei Formeln direkt hintereinander („bei \(W\) \(125°\)“) und nummerierte Regeln direkt nach
  einem Satzende („… 0,144. 2. Pfadregel“) liest man im Bild falsch: umstellen.
- Gleiche Personennamen und Kontexte in verwandten Aufgaben zweier Trainer fallen als Echo auf.
- Stufen-Kommentare im Quelltext (`// LEVEL n — …`) an den neuen Inhalt anpassen (bytegenau).
- Die Engine nimmt große Zahlen mit Tausenderpunkt und mit Leerzeichen an („250.000“,
  „250 000“); Zusätze wie „ohne Punkte eingeben“ sind unnötig.
- Zufallstreffer reichen weiter als „Lösung = gegebene Zahl“: auch Summe, Differenz, Mittelwert
  und Produkt der gegebenen Zahlen sowie Symmetrien (halbe Höhe, gleichschenklige Lage) dürfen
  nicht den Lösungswert treffen. Das gehört von vornherein ins Nachrechen-Skript.
- Nach einem Stufenumbau prüfen, ob die nächsthöhere Stufe noch mehr verlangt als die
  umgebaute.
- Textgeometrie: Lagebeschreibung als Konstante im Datenmodul führen und in jeder Aufgabe
  ausschreiben; jede Figur muss sich allein aus dem Text eindeutig zeichnen lassen.
- Abgesetzte Formeln ab etwa 45 Zeichen brechen hinter einem Operator um (einzelnes Zeichen in
  der Folgezeile): in zwei Formelzeilen teilen oder in den Fließtext legen. Hohe Brüche in
  wörtlicher Rede zerreißen die Zeile: Verhältnisschreibweise nehmen.
- Prüfervorschläge im Wortlaut nachrechnen, bevor sie übernommen werden: zweimal hätte ein
  Vorschlag einen falschen Satz oder einen neuen Zufallstreffer eingebracht.
- Die Heredoc-Regel gilt auch für kleine Hilfsskripte und Patches: Write- oder Edit-Tool.
- Tabellen in Aufgaben (Vierfeldertafel, Wertetabelle): KaTeX-`array` mit kurzen Spaltenköpfen,
  in der Frage `\footnotesize`; HTML-Tabellen lehnt das Level-Gate ab. Bei 360 px im Bild prüfen
  (Vorbild und Messskript `ueberlauf.py`: Trainer `9-daten-zufall-boxplot`, Scratchpad `w9c`).
- Toleranz nie genau auf die Rundungsstufe legen (0,61 − 0,6 > 0,01 in Gleitkomma): 0,011 bzw.
  0,05 bei einer Nachkommastelle.
- Bei π-Aufgaben runden π-Taste und 3,14 oft verschieden (16π: 50,3 gegen 50,2): Zahlen so
  wählen, dass beide Wege gleich runden, statt die Toleranz zu weiten; oder „in der Form k·π“.
- Kleine ganze Zahlen treffen in Formelaufgaben auffällig oft eine andere Größe derselben Figur
  (r = 3: r²/3 = r; r = 4: r² = 4r; R − r = 2): im Nachrechen-Skript alle Größen der Figur, auch
  mit d als r, gegen die Toleranz laufen lassen (`rlib.breit` im Scratchpad `w9b2`).
- Trigonometrie und mehrschrittige Geometrie: Ins Fehlweg-Netz gehören auch berechnete
  Zwischenwinkel und der Weg „wie ein rechtwinkliges Dreieck gerechnet“ (fast rechtwinklige
  Dreiecke lassen ihn durch). Besondere Winkelpaare meiden: Summe 90°, Differenz 30°, einer das
  Doppelte des anderen, b = 2a. Vorbild: `tlib.py` und `rechne_sk.py` im Scratchpad `w10a1`.
- Toleranzen nicht auf volle Hundertstel legen, wenn ein Fehlweg genau dort landet; den Abstand
  zum nächsten Fehlweg im Skript ausgeben und die Toleranz darunter wählen.
- Ein Prüfdurchgang je Trainer plus ein Nachtrag für geänderte Aufgaben genügt in der Regel.
  Weitere Nachträge nur für Aufgaben mit neuen Zahlen; reine Wortlaut- und Toleranzänderungen
  selbst nachrechnen und im Bild ansehen.
- Nachrechen-Skripte von Anfang an je Stufe aufrufbar und mit Gleitkomma schreiben (ein Lauf
  unter einer Sekunde); sympy nur, wo es exakt sein muss.
- Kugel: r = 3 (V und O gleiche Maßzahl), r = 6 (halbes Volumen = Oberfläche), d = 8 (r³ = d²)
  und r = 1 meiden. Anteilsfragen können bauartbedingt eine andere Größe treffen
  (Oberflächenanteil = r : R): dann die Frage ändern, nicht die Zahlen.
- MC mit zusammengesetzten Aussagen als 2×2-Raster bauen (zwei Merkmale, je zwei Ausprägungen)
  und prüfen, ob der Tipp ein Merkmal verrät.
- Glatte Lösungen mit Toleranz 0 weisen den Dezimalweg ab (6,9988 statt 7): eine kleine
  Toleranz geben, wenn es einen zweiten Rechenweg gibt.
- Zahlwörter im Text („alle vier Seiten“, „sechs Wände“) gehören ins Zufallsnetz.
- Die Heredoc-Regel gilt auch für leere Heredocs (`python - <<'EOF'` hängt).

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
