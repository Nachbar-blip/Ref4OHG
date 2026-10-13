# Kriterien Qualifikationsphase Kern (Spalte 12, gA), Block C1: Stochastik — Zufallsgrößen und bedingte Wahrscheinlichkeit — Level-Durchgang 2026-10

Je Trainer ein Abschnitt (Format: Plan `2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, „Kriterien-Datei“).
KC = Kerncurriculum Mathematik für die gymnasiale Oberstufe, Niedersachsen (`ma_go_kc_2019.txt`), Zeilenangaben dort.
Lesart der Stufen für die Qualifikationsphase: Stufe 4 = Verfahren selbst wählen, Umkehraufgabe, Modell aus Text; Stufe 5 = zwei Verfahren
verbinden, Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung finden; Stufe 6 = Abiturformat des hilfsmittelfreien Teils
(begründen, beurteilen, Zusammenhänge herstellen, Grenzfall). „Befund“ beschreibt den Stand vor dem Durchgang.

## KC-Befund am Wortlaut

Lernbereich „Daten und Zufall“, grundlegendes Anforderungsniveau: Intentionen Z. 1946–1966, Kern Z. 1967–1994. Für diesen Block:

- **Bedingte Wahrscheinlichkeit und stochastische Unabhängigkeit** (Z. 1968–1973): „Einträge in Baumdiagrammen und Vierfeldertafeln nutzen,
  um den Begriff der bedingten Wahrscheinlichkeit zu erarbeiten und dabei zwischen bedingendem und bedingtem Ereignis unterscheiden“;
  „Teilvorgänge bei mehrstufigen Zufallsexperimenten auf stochastische Unabhängigkeit untersuchen“. Intentionen (Z. 1950–1953): „Der
  Vergleich zwischen dem Ziehen ohne Zurücklegen und dem Ziehen mit Zurücklegen fördert das Verständnis für die stochastische Unabhängigkeit.“
- **Erwartungswert und Standardabweichung diskreter Zufallsgrößen** (Z. 1974–1978): „Zusammenhang zwischen Kenngrößen der
  Häufigkeitsverteilung und Kenngrößen der Wahrscheinlichkeitsverteilung herstellen“; „Erwartungswert, Varianz und Standardabweichung
  berechnen und interpretieren“; „Faire Spiele mithilfe des Erwartungswerts kennzeichnen“. Intentionen (Z. 1954–1959): Häufigkeitsverteilungen
  durch diskrete Wahrscheinlichkeitsverteilungen modellieren, „Dabei wird die zugehörige Zufallsgröße angegeben“; die bekannten Kenngrößen
  empirischer Verteilungen werden auf das Modell übertragen und führen zu Erwartungswert und Standardabweichung.
- **Nicht in diesem Block** (eigene Trainer in Block 12C2): Binomialverteilung mit \(n\), \(p\), \(\mu = n \cdot p\), \(\sigma = \sqrt{n p (1-p)}\),
  Prognoseintervalle, „verträglich“ (Z. 1979–1993). Nicht im gA-Kern: Hypothesentests, Signifikanz, Konfidenzintervalle (eA, Z. 2280–2288).
- **Schreibweise der bedingten Wahrscheinlichkeit:** Das KC nennt keine (weder \(P_B(A)\) noch \(P(A \mid B)\)); es verlangt nur die Unterscheidung
  von bedingendem und bedingtem Ereignis. Der Trainer behält die vorhandene Schreibweise \(P(A \mid B)\) bei; die Entscheidung zwischen beiden
  Schreibweisen steht dem Autor zu (im Bericht unter „Für den Autor“).
- **Wörter ohne KC-Beleg, bewusst vermieden:** „Satz von Bayes“, „Sensitivität“, „Spezifität“, „Satz von der totalen Wahrscheinlichkeit“ (der alte
  Trainer trug sie in sechs Lösungswegen und Tipps). Die Umkehrung der Blickrichtung wird über das umgekehrte Baumdiagramm und die Pfadregeln
  erklärt; die Summe der Pfade zu einem Ereignis heißt nur „\(P(B)\)“.

## Zuschnitt der zwei Trainer

- **`12-stoch-grundlagen`** (Inhalt seit 2026-10: **Zufallsgrößen & Erwartungswert**): Zufallsgröße als Zuordnung, Wahrscheinlichkeitsverteilung
  ablesen, vervollständigen und aus Würfel, Münze, Glücksrad, Urne aufstellen; Erwartungswert, Varianz, Standardabweichung; arithmetisches
  Mittel der Häufigkeitsverteilung gegen Erwartungswert; Gewinnverteilung aus einem Spieltext, faires Spiel, Einsatz, Deutung des Erwartungswerts;
  Parameter aus Erwartungswert und Summe 1, Fehlersuche; Aussagen über faire Spiele und den Erwartungswert beurteilen, zwei Spiele mit gleichem
  Erwartungswert und verschiedener Streuung, Grenzfall (Ungleichung), Einsatz aus einer Zielvorgabe. **Keine Binomialverteilung**: Verteilungen
  mehrstufiger Experimente werden über das Baumdiagramm aufgestellt (#7, #12, #28, #30), nie über \(n \cdot p\).
- **`12-stoch-bedingte-wahrscheinlichkeit`**: Schreibweise \(P(A \mid B)\), bedingendes gegen bedingtes Ereignis, Vierfeldertafel und Baumdiagramm mit
  Wahrscheinlichkeiten (nicht mit Anzahlen), Multiplikationssatz \(P(A \cap B) = P(B) \cdot P(A \mid B)\), \(P(B)\) als Summe zweier Pfade, Umkehrung der
  Blickrichtung, Unabhängigkeit in Produktform und als \(P(A \mid B) = P(A)\), Ziehen mit und ohne Zurücklegen, Parameter aus Bedingungen,
  Aussagen begründet prüfen.
- **Abstand zu `9-daten-zufall-boxplot`** (Spalte 9, Inhalt „Baumdiagramme & Vierfeldertafeln“, alles in Worten und mit Anzahlen): Dort wird gezählt
  (Tafeln mit Anzahlen vervollständigen, Tafel aus Text, Anteile „unter den …“, Testaufgaben in natürlichen Häufigkeiten). Hier wird mit
  Wahrscheinlichkeiten und Formeln gearbeitet: Tafeln tragen von Stufe 1 an Wahrscheinlichkeiten, bedingte Wahrscheinlichkeiten stehen in
  Formelschreibweise, Unabhängigkeit kommt formal vor. Die alten Aufgaben #19 und #20 (Klasse mit 30 Personen, Brille, Anzahlen) und die
  sechs Testaufgaben der alten Stufe 6 (Krankheit, Spamfilter, Drogentest – Form des Spalte-9-Trainers #26/#35) sind entfallen; Kontexte und
  Namen des Spalte-9-Trainers (Brille, Chor, Sportverein, Kino, Abo, Rad, Helm, Fahrschein, Haustier, Parkplatz, Hofladen, Freiwürfe) kommen hier
  nicht vor. Einziger Berührungspunkt: #35 (Alarmanlage, Grenzfall über eine Ungleichung in \(p\)) ist der Form nach mit Spalte 9 #35 (Test,
  kleinste Anzahl Kranker) verwandt – hier mit unbekanntem Anteil \(p\) in Formelschreibweise statt mit Anzahlen; vermerkt für den Autor.
- **Abstand zu `8-zufallsversuche-mehrstufig`** (#22 Lieferanten A/B mit Ausschuss, #34 Pasch-Spiel „lohnt sich das Spiel?“) und
  `7-wahrscheinlichkeit` (#32 durchschnittlicher Gewinn eines Würfelspiels): Die Form „Einsatz, Würfel, Auszahlung“ ist in der Qualifikationsphase
  der KC-Gegenstand „faire Spiele“ und bleibt; die Zahlen sind so gewählt, dass kein Lösungswert mit den Aufgaben der Klassen 7/8 übereinstimmt
  (Prüfer: alt \(-0{,}33\) wie 8-zufall #34, jetzt \(-0{,}6\)); Maschinen/Lieferanten mit Ausschuss kommen hier nicht vor.

## Gemeinsame Regeln dieses Blocks

- **Darstellung:** nur Text und KaTeX. Wahrscheinlichkeitsverteilungen und Vierfeldertafeln als KaTeX-`array` mit `\footnotesize` in der Frage
  (Spaltenköpfe \(x_i\) / \(P(X = x_i)\) bzw. \(B\), \(\bar{B}\)); bei 360 px im Bild geprüft (Bögen `zg_360a/b`, `zg_nach360`, `bw_360*` im Scratchpad
  `w12c1/sicht`). Baumdiagramme in Worten oder als Liste von \(P(A)\), \(P(B \mid A)\), \(P(B \mid \bar{A})\). Abgesetzte Formeln über etwa 45 Zeichen
  sind in zwei Zeilen geteilt (#15, #19, #28 nach der ersten Sichtprüfung bei 360 px).
- **Eingaben:** eine Zahl je Aufgabe, „als Dezimalzahl“ bei nicht ganzzahligen Lösungen; Verluste als negative Zahl (steht in der Frage); Prozent
  nur, wo die Frage es sagt. Toleranzen unter der Rundungsstufe (0,001 bei zwei Stellen exakt, 0,0015 bei drei verlangten Stellen, 0,006 bei zwei
  verlangten Stellen, 0,0009 bei #9, damit die Zweistellen-Rundung nicht durchgeht).
- **Nachrechnen** (`rechne_zg.py`, `rechne_bw.py` mit `slib.py` im Scratchpad `w12c1`, je Stufe aufrufbar, Gleitkomma und `Fraction`): Verteilungen
  werden aus dem Ergebnisraum gebaut (alle Wurfpaare, alle Ziehungen), nicht aus dem Lösungsweg abgeschrieben; Erwartungswert, Varianz und
  Standardabweichung daraus; Parameteraufgaben durch Suche über ein Raster. Gegen die Toleranz laufen je Aufgabe die Fehlwege (Einsatz vergessen,
  Einsatz nur bei Niete, Varianz statt Standardabweichung, ungewichtetes Mittel, mit statt ohne Zurücklegen, nur ein Pfad, Grenzfall statt strikter
  Ungleichung, bedingendes und bedingtes Ereignis vertauscht, Anteil an allen statt bedingt, Gewichte vergessen) und das Zufallsnetz (Lösung =
  gegebene Zahl, Summe, Differenz, Produkt, Quotient, Mittel zweier gegebener Zahlen). Bei MC wird der Wahrheitswert jeder Option berechnet, wo
  das geht.

## 12-stoch-grundlagen — Zufallsgrößen & Erwartungswert

KC: QP gA „Daten und Zufall“, Kern „Erwartungswert und Standardabweichung diskreter Zufallsgrößen“ (G9, GO Z. 1974–1978), Intentionen
Z. 1954–1959. Kommentar in Zeile 2 der Datei gesetzt; Stufen-Kommentare im Quelltext angepasst; Dateiname und `THEMA_KEY` bleiben.
Titel (Empfehlung, nicht gesetzt – Parallelbetrieb): an allen drei Stellen „Zufallsgrößen & Erwartungswert“ (bisher `<title>` und Trainer
„Stochastik Grundlagen“, Index „Stochastik Grundlagen“).
Gelesen: alle 36 alten Aufgaben und alle 36 neuen. Urteil Lehrplan vorher (Abgleich Z. 168, 243, 342: „passt nur als Sek-I-Wiederholung; kaum
QP-eigener Stoff“): bestätigt. Stufe 1 Ergebnisraum und Ereignis (Klasse 7), Stufe 2 Laplace-Wahrscheinlichkeit (Klasse 7), Stufe 3 Schnitt,
Vereinigung, Gegenereignis, Stufe 4 Pfadregeln (Klasse 8), Stufe 5/6 mehrstufige Experimente, zweimal totale Wahrscheinlichkeit und Bayes-Form
(alt #29/#30 Firma mit Rad, #36 Instrument – Stoff des Schwestertrainers, dort als Kontext jetzt nicht mehr verwendet). **Einzige QP-Aufgabe: alt #33
(Erwartungswert der Augenzahl, Abgleich Z. 243) – erledigt**: die Idee lebt als #14 weiter, nach dem Prüfdurchgang mit einem unregelmäßig
beschrifteten Würfel (\(1, 2, 2, 4, 5, 5\)), weil \(3{,}5\) ohne Rechnung bekannt ist und in #35 als Beispiel vorkommt.
**Verfahren: vollständiger Ersatz statt Teil-Ersatz** (Plan: Teil-Ersatz Stufe 3–6, Stufe 1–2 „so anpassen, dass sie darauf hinführen“). Begründung:
Keine der zwölf Aufgaben der Stufen 1–2 enthielt eine Zufallsgröße oder eine Verteilung; „Anpassen“ hätte jede Aufgabe neu geschrieben.
Die Formen der alten #3 (Anzahl der Ergebnisse), #12 (Münzen), #21/#22 (Urne mit und ohne Zurücklegen) kehren als Verteilungsaufgaben wieder
(#3, #6, #12). Aus dem Altbestand ist sonst nichts KC-gedeckt und ungedeckt zugleich – alles Übrige steht in den Trainern der Klassen 7 und 8.
Nach dem Durchgang: 36 Aufgaben, davon 9 MC (Stufe 1: 3, Stufe 4: 2, Stufe 5: 2, Stufe 6: 3); Stufe 1–2 ohne Sachkontext (Würfel, Münze,
Glücksrad, Urne, abstrakte Tabellen).

| id | Stufe | Kriterium laut Rubrik | Aufgabe (neu) | Zahlenwahl, Prüfbefunde |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | Verteilung mit vier Werten, fehlende Wahrscheinlichkeit (0,1) | Zufallsnetz: 0,3 : 3 trifft 0,1 – kein Rechenweg; mehrere Zahlensätze mit Summe/Mittel zweier Einträge = Lösung verworfen |
| 2 | 1 | Begriff (MC) | Was ist eine Zufallsgröße? | Distraktoren: Ereignis, Anzahl Durchführungen, Ergebnismenge |
| 3 | 1 | ein Schritt | Augensumme zweier Würfel: Anzahl der Werte (11) | Fehlwege 12, 36 fallen |
| 4 | 1 | ein Schritt | \(P(X \geq 2)\) aus Tabelle (0,45) | Summe zweier Einträge ist der Rechenweg |
| 5 | 1 | Objekt prüfen (MC) | welche Zuordnung ist eine Verteilung (Summe 1, nicht negativ) | drei Distraktoren je mit einem Verstoß |
| 6 | 1 | Objekt lesen (MC) | Werte von „Anzahl Kopf“ bei drei Würfen | Distraktoren ohne 0, ohne 3, Ergebnisse statt Werte |
| 7 | 2 | zwei Schritte | Anzahl Sechsen bei zwei Würfen, \(P(X = 1)\) (0,278) | nur ein Pfad 0,139, „mindestens eine“ 0,306 fallen |
| 8 | 2 | zwei Schritte | zwei gleiche fehlende Einträge (0,32) | Rest ungeteilt 0,64 fällt |
| 9 | 2 | zwei Schritte | Maximum zweier Augenzahlen, \(P(X = 3)\) (0,139) | Toleranz 0,0009 nach Prüfer (0,14 ging durch); 1/6, 3/36 fallen |
| 10 | 2 | zwei Schritte | fehlender Eintrag, dann \(P(X \leq 20)\) (0,65) | erst \(P(X > 20)\), das kam ohne den fehlenden Eintrag aus (ein Schritt) |
| 11 | 2 | zwei Schritte | Glücksrad mit 0, 2, 5: Verteilung, \(P(X \geq 2)\) (0,375) | erst \(P(X = 2)\) mit 3 von 8 Feldern – ein Schritt und sinngleich zu 7-wahrscheinlichkeit #10 (Prüfer) |
| 12 | 2 | zwei Schritte | Urne 2 rot / 3 blau ohne Zurücklegen, \(P(X = 1)\) (0,6) | mit Zurücklegen 0,48, ein Pfad 0,3 fallen |
| 13 | 3 | Zwischenergebnis | \(E(X)\) aus Tabelle (1,85) | erst 0,1/0,2/0,4/0,3 → 1,9 = 2 − 0,1 (Zufallsnetz); ungewichtet 1,5 fällt |
| 14 | 3 | Zwischenergebnis | unregelmäßiger Würfel 1, 2, 2, 4, 5, 5: \(E(X)\) (3,17) | alte #33 (3,5) nach Prüfer ersetzt; Vorschlag 1, 1, 2, 4, 4, 6 (E = 3) verworfen: 3 = 1 + 2 = 4 − 1 = 6 : 2; ungewichtet 3 fällt |
| 15 | 3 | Zwischenergebnis | Varianz aus Tabelle (1,29) | Standardabweichung 1,14, mittlerer Abstand 0,9, \(E(X^2)\) fallen; Formel im Lösungsweg nach 360-px-Bild zweizeilig |
| 16 | 3 | Zwischenergebnis | zweiwertige Verteilung 0 / 10 mit 0,1 / 0,9: \(\sigma\) (3) | erst 0,2 / 0,8 → σ = 4 = 0,8 : 0,2; jetzt Varianz 9 = E(X) – beide fallen als Eingabe; \(\sqrt{p(1-p)} \cdot 10\) ist derselbe Wert (kein Fehlweg) |
| 17 | 3 | Zwischenergebnis | Glücksrad mit 1, 2, 6: Verteilung, dann \(E(X)\) (2,3) | ungewichtet 3 fällt |
| 18 | 3 | Zusammenhang Häufigkeits-/Wahrscheinlichkeitsverteilung | arithmetisches Mittel von 400 Drehungen (0,95); Lösungsweg zeigt die Gewichtung mit relativen Häufigkeiten | KC Z. 1975; Mittel der drei Zahlen 1,33 fällt |
| 19 | 4 | Modell aus Text | Würfelspiel: Gewinnverteilung, \(E(G)\) (−0,6) | nach Prüfer neue Zahlen (alt −0,33 = 8-zufallsversuche #34); ohne Einsatz 1,4, Einsatz nur bei Niete fallen |
| 20 | 4 | Urteil mit Begründung (MC) | Glücksrad 10/2/0/0 €, Einsatz 3 €: fair? | Distraktor „Ja – gleich große Felder“ war in der Ja/Nein-Antwort richtig (Prüfer) → jetzt „Nein – … erst bei gleicher Auszahlung“ |
| 21 | 4 | Umkehraufgabe | Einsatz für ein faires Spiel (2,2) | nur rot 1,5, ungewichtet 3, vertauscht 3,8 fallen |
| 22 | 4 | Umkehraufgabe | Wert \(a\) aus \(E(X) = 2{,}8\) (7) | erst \(E = 2{,}6\), \(a = 6 = 3 : 0{,}5\); ohne 0,9 bzw. ohne 0,5 fallen |
| 23 | 4 | Modell aus Text | Tombola 1000 Lose: \(E(G)\) (−0,5) | ohne Lospreis 0,5, Anzahlen vergessen fallen; Formel im Lösungsweg nach 360-px-Bild gekürzt |
| 24 | 4 | Deutung (MC) | „Welche Aussage folgt aus \(E(X) = 0{,}4\)?“ | nach Prüfer als „folgt“ formuliert (der Distraktor „40 % der Seiten“ ist nicht ausgeschlossen, folgt aber nicht) |
| 25 | 5 | Parameter aus zwei Bedingungen | \(P(X = 0)\) aus \(E(X)\) und Summe 1 (0,39) | \(P(X = 5) = 0{,}36\), 0,75, 0,46 fallen |
| 26 | 5 | Fehler finden (MC) | Luca gibt die Varianz 2,25 als Standardabweichung aus | drei falsche Beziehungen Varianz/σ als Distraktoren |
| 27 | 5 | Parameter, zwei Auszahlungen von \(a\) abhängig | faires Spiel: Sechs \(a\), Fünf \(a/2\), Einsatz 2 € (8) | erst „Fünf 2 €, Sechs \(a\)“ (7) – eine Gleichung wie #21/#22 und derselbe Spielrahmen wie #19 (Prüfer); Prüfervorschlag mit Einsatz 1,50 € (a = 6) wegen 6 = Augenzahl auf 2 € umgestellt; Fünf vergessen 12, a/3 fallen. Stehen gelassen: 8 = 2 + 6 |
| 28 | 5 | zwei Verfahren | Glücksrad zweimal, Summe: Verteilung über den Baum, dann σ (1,22) | Varianz 1,5, E = 1, \(\sqrt{2 \cdot 0{,}25 \cdot 0{,}75}\) fallen; Formel zweizeilig |
| 29 | 5 | Umkehraufgabe mit Term | \(a\) aus σ = 2 bei 0,8 / 0,2 (5) | erst 0,5 / 0,5 mit σ = 3: a = 6 = σ : p – jedes falsche Verhältnis traf; jetzt σ/p = 10, σ/(1−p) = 2,5, 2σ = 4 fallen |
| 30 | 5 | Fehler finden (MC) | Mara mittelt die Werte 0, 1, 2 ungewichtet | richtig \(E = \frac{1}{3}\); Distraktoren größter Wert, 3/36 |
| 31 | 6 | Aussage begründet prüfen (MC) | „Ein faires Spiel gewinnt man in der Hälfte der Fälle“ (Plan) | Gegenbeispiel im Lösungsweg (p = 0,1, Auszahlung 10 €); richtige Option nach Gate gekürzt |
| 32 | 6 | beurteilen (MC) | zwei faire Spiele, σ = 1 gegen σ ≈ 9,9 (Plan) | Distraktoren: unfair wegen Häufigkeit, falsche σ-Richtung, falscher E-Vergleich |
| 33 | 6 | Zusammenhang Erwartungswert – Häufigkeit, Parameter | Einsatz \(e\), 1200 Spiele, 300 € Gewinn (1,5) | nach Prüfer „Gewinn (Einsätze abzüglich Auszahlungen)“ statt „einnehmen“ (Bruttolesart 0,25); 0,25 und 0,5 fallen. Stehen gelassen: 1,5 = 6 : 4 (Würfelzahlen) |
| 34 | 6 | Fallunterscheidung, Ungleichung | kleinstes ganzzahliges \(a\) mit \(E(G) > 0\) (9) | Grenzfall 8 (fair) fällt, 10 und 11 fallen |
| 35 | 6 | Aussage begründet prüfen (MC) | „Der Erwartungswert ist immer ein möglicher Wert“ | Gegenbeispiele 3,5 und 0,5 |
| 36 | 6 | Abiturformat: Behauptung widerlegen, Zahl bestimmen | Anbieter: „Hälfte der Fälle, also fair“; Senkung des Einsatzes bis fair (0,77) | erst „Auszahlung erhöhen“ (4,6) – Rechnung wie #27 plus Subtraktion (Prüfer); jetzt Prüfervorschlag, nachgerechnet (37/30 ≈ 1,2333; 2 − 1,2333 = 0,7667); 1,23 und 1 fallen, 2 − 1,23 = 0,77 angenommen |

Nachrechnen: `rechne_zg.py`, 36 von 36 ohne Fehler (Ausgaben `aus_zg_L1..L6.txt`); nicht gerechnet, nur begrifflich entschieden: #2, #5 (Option
mit negativer Wahrscheinlichkeit), #6, #24, #35 und die Begründungstexte der Distraktoren in #20, #31, #32.
Zweiter Prüfdurchgang (frischer Agent ohne Browser, alle 36, Vergleich mit 7-wahrscheinlichkeit, 8-zufallsversuche-mehrstufig,
12-stoch-binomialverteilung, 12-stoch-sigma-umgebungen): kein Fehler; 5 Mängel (#11 ein Schritt und Dublette zu Klasse 7, #14 Lösung bekannt,
#27 Stufe 4 und Rahmen von #19, #33 „einnehmen“ mehrdeutig, #36 Rechnung wie #27) und 4 Hinweise (#9 Toleranz, #19 Lösungswert wie 8-zufall
#34, #20 Distraktor mit richtiger Ja/Nein-Antwort, #24 Distraktor nicht ausgeschlossen) – alle eingearbeitet, Zahlen der Vorschläge nachgerechnet
und bei #14 und #27 geändert (siehe Tabelle). Kein Nachtrags-Prüfer: Die neuen Zahlen von #11, #14, #19, #27, #36 sind im Skript nachgerechnet
und in der Endfassung im Bild angesehen (`zg_nach-01.png`, `zg_nach360-01.png`).

## 12-stoch-bedingte-wahrscheinlichkeit — Bedingte Wahrscheinlichkeit

KC: QP gA „Daten und Zufall“, Kern „Bedingte Wahrscheinlichkeit und stochastische Unabhängigkeit“ (G9, GO Z. 1968–1973), Intentionen
Z. 1950–1953 (Ziehen mit und ohne Zurücklegen). Titel: bisher an allen drei Stellen „Bedingte Wahrscheinlichkeit“ – bleibt (Empfehlung, nicht
gesetzt: unverändert). Stufen-Kommentare im Quelltext angepasst; Dateiname und `THEMA_KEY` bleiben.
Gelesen: alle 36 alten Aufgaben und alle 36 neuen. Urteil Lehrplan vorher (Abgleich Z. 169: „passt“): Thema passt, der Trainer lag aber eine bis
zwei Stufen zu tief und wiederholte den Spalte-9-Trainer: Stufe 1 sechsmal Randsumme einer Tafel als MC (Tipp mit der fertigen Formel),
Stufe 2 Tafel vervollständigen, Stufe 3 sechsmal \(P(A \mid B) = \frac{P(A \cap B)}{P(B)}\) mit der Formel im Tipp, Stufe 4 mit #19/#20 (Klasse,
Brille, Anzahlen – die Form von Spalte 9 #19/#20) und #24 (Stufe-3-Aufgabe), Stufe 5 vier Unabhängigkeitsaufgaben mit der Formel im Tipp,
Stufe 6 sechsmal dieselbe Testaufgabe (Bayes-Formel im Tipp; Sensitivität/Spezifität, Spamfilter, Drogentest). „Satz von Bayes“ stand im
Stufen-Kommentar und in sechs Tipps/Lösungswegen, „Satz von der totalen Wahrscheinlichkeit“ in #22 – beide Wörter kennt das KC nicht.
Verfahren: „Durchgang“ laut Plan; nach dem Lesen sind alle 36 Aufgaben neu gesetzt, weil keine Stufe trug (Begründung oben). Übernommene
Ideen: alt #1–#6 (Tafel lesen) → #4, #7, #12 mit Wahrscheinlichkeiten und bedingter Frage; alt #13/#14/#24 (Formel anwenden) → #1; alt #17/#18
(Pfadregel) → #3; alt #21 (Test erkennt 99 %) → #21 mit Alarmanlage; alt #23/#26/#27 (Unabhängigkeit) → #6, #10, #22, #26, #29, #31;
alt #22/#32/#33/#36 (zwei oder drei Quellen) → #14, #19, #23, #28; alt #30 (Sport/Musik) → #29 (jetzt unabhängig, neuer Kontext).
Nach dem Durchgang: 36 Aufgaben, davon 10 MC (Stufe 1: 2, Stufe 2: 1, Stufe 3: 1, Stufe 4: 2, Stufe 5: 2, Stufe 6: 3); Stufe 1–2 ohne
Sachkontext.

| id | Stufe | Kriterium laut Rubrik | Aufgabe (neu) | Zahlenwahl, Prüfbefunde |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | \(P(A \mid B)\) aus \(P(A \cap B)\) und \(P(B)\) (0,3) | Produkt 0,048, Differenz 0,28 fallen |
| 2 | 1 | Begriff (MC) | bedingendes Ereignis in \(P(R \mid S)\) | KC: „zwischen bedingendem und bedingtem Ereignis unterscheiden“ |
| 3 | 1 | ein Schritt | \(P(A \cap B)\) aus \(P(A)\) und \(P(B \mid A)\) (0,18) | Quotient 0,5 fällt |
| 4 | 1 | Objekt lesen (MC) | Tafel mit Wahrscheinlichkeiten: welcher Bruch ist \(P(B \mid A)\)? | Distraktoren: \(P(A \mid B)\), Kehrwert, durch 1 |
| 5 | 1 | ein Schritt | \(P(\bar{A} \mid B)\) aus \(P(A \mid B)\) (0,75) | — |
| 6 | 1 | ein Schritt | Produktformel bei Unabhängigkeit (0,2) | Summe 0,9, Additionssatz-Rest 0,7 fallen |
| 7 | 2 | zwei Schritte | Tafel ohne Randsummen: \(P(B)\), dann \(P(A \mid B)\) (0,6) | erst 0,24/0,26/0,16/0,34: \(P(\bar{B}) = 0{,}6\) traf die Lösung; jetzt \(P(B) = 0{,}3\); \(P(B \mid A)\) 0,4, \(P(A)\) 0,45 fallen |
| 8 | 2 | zwei Schritte | \(P(B)\) aus zwei Pfaden (0,34) | 9-daten #10 hat 0,3/0,8/0,4 – andere Zahlen; ein Pfad 0,21, Summe der Äste 0,8 fallen |
| 9 | 2 | zwei Schritte | \(P(\bar{B} \mid A)\) über \(P(B \mid A)\) (0,8) | erst 0,15: 0,6 + 0,15 = 0,75 traf die Lösung; jetzt 0,12 |
| 10 | 2 | Standardverfahren (MC) | Unabhängigkeit prüfen: ja (Produktformel) | alte #23 (Stufe 4) mit neuen Zahlen; Distraktoren mit Fehlkriterien; Lösungsweg nach Prüfer „nie größer als“ statt „kleiner als“ |
| 11 | 2 | zwei Schritte | \(P(A \mid B)\) über den Additionssatz (0,24) | zweimal Zahlen getauscht: 0,4·0,75 = 0,3 und \(P(A \cup B) - P(B)\) = Lösung; jetzt 0,78 − 0,5 = 0,28, 0,78 − 0,4 = 0,38 fallen |
| 12 | 2 | zwei Schritte | Tafel: \(P(B \mid \bar{A})\) (0,25) | erste Zeile 0,12/0,28 war die von 9-daten #8 (Prüfer) → 0,14/0,26; \(P(\bar{A} \mid B)\) 0,517, \(P(B \mid A)\) 0,35 fallen; Mittel aller vier Felder ist immer 0,25 (kein Rechenweg) |
| 13 | 3 | Zwischenergebnis | Spanisch/Französisch: \(P(F \mid S)\) (0,333) | \(P(S \mid F)\) 0,2 fällt |
| 14 | 3 | Zwischenergebnis | Gärtnerei: \(P(\text{alt} \mid \text{keimt})\) (0,077) | 0,3, 0,06, 0,923 fallen |
| 15 | 3 | Deuten (MC) | welche Angabe ist bedingt? (Musikschule) | Zahlen konsistent (0,3·0,6 = 0,18) |
| 16 | 3 | Zwischenergebnis | Bibliothek: Pfadende \(P(\bar{K} \cap \bar{V})\) (0,44) | 0,11, 0,18, 0,27 fallen |
| 17 | 3 | Zwischenergebnis | Urne 2/8 ohne Zurücklegen: \(P(B \mid A)\) (0,111) | erst 3/7 – dieselbe Urne wie `12-stoch-grundlagen` #21 (Prüfer); der Vorschlag 4/6 ist die Urne von 8-zufallsversuche #20, daher 2/8; mit Zurücklegen 0,2, 2/9 fallen; Lösungsweg nennt die Abhängigkeit |
| 18 | 3 | Zwischenergebnis, Bedingung wechseln | \(P(B \mid A)\) aus \(P(A)\), \(P(B)\), \(P(A \mid B)\) (0,28) | erst mit \(P(A \cap B)\) gegeben – ein Schritt wie #1 (Prüfer); jetzt Prüfervorschlag, nachgerechnet; 0,35, 0,175, 0,14 fallen |
| 19 | 4 | Modell aus Text, Umkehrung | Kundenservice: \(P(\text{Telefon} \mid \text{schnell})\) (0,39) | 0,95, 0,35, 0,3325, 0,61 fallen |
| 20 | 4 | Umkehraufgabe | Solaranlage/Wärmepumpe: \(P(S \mid W)\) aus \(P(S)\), \(P(W \mid S)\), \(P(W)\) (0,6) | 0,7, 0,21, 0,857 fallen |
| 21 | 4 | Fehlschluss erkennen (MC) | Alarmanlage: 98 % der Einbrüche ≠ 98 % der Alarme | alte #21 ohne Krankheitskontext und ohne „Bayes“ |
| 22 | 4 | Umkehraufgabe | \(P(B)\) aus Unabhängigkeit und \(P(A \cup B)\) (0,4) | 0,28, 0,215 fallen |
| 23 | 4 | Modell aus Text | Sprachkurs: \(P(M \mid W)\) in Prozent (51,6) | nach Prüfer mit benannten Ereignissen in Formelschreibweise (Abstand zur Sek-I-Frageform „Wie viel Prozent der …, die …“); 40, 16, 48,4, 32,5 fallen |
| 24 | 4 | Verfahren wählen (MC) | welche Rechnung liefert \(P(A \mid B)\)? | nach Gate (richtige Option zu lang) Distraktoren mit vollständigen Termen: Gewichte vergessen, nur \(P(B)\), falsches Gewicht 0,4 |
| 25 | 5 | Fehler finden (MC) | Jana teilt durch \(P(A)\) statt \(P(B)\) | Zahlen so, dass A, B nicht unabhängig sind (sonst wäre \(P(A \mid B) = P(A)\) ein zweiter Weg) |
| 26 | 5 | Parameter aus Bedingung | \(y\) so, dass A und B unabhängig (0,28) | 0,3, 0,18, 0,35 fallen; 0,4 − 0,12 ist der Rechenweg |
| 27 | 5 | Parameter | Urne 6 rote, \(n\) blaue: \(n\) aus \(P(B \mid A) = 0{,}25\) (15) | erst 5 rote, 0,4 → 6: gleiche Form und Lösungszahl wie 8-zufallsversuche #36 (Prüfer); Prüfervorschlag (6 rote, 0,5 → 5) verworfen, weil 5 die Zahl der verbleibenden roten Kugeln ist; mit Zurücklegen 18, 5/(6+n) → 14 fallen |
| 28 | 5 | drei Äste | Konzertkarten: \(P(\text{Abendkasse} \mid \text{ermäßigt})\) (0,278) | 0,5, 0,2, 0,1, 0,385, 0,556 fallen |
| 29 | 5 | zwei Verfahren (MC) | Podcasts/Hörbücher: Schnitt über „mindestens eines“ (74 %), dann Unabhängigkeit (0,6·0,35 = 0,21) | nach Prüfer: Ereignis \(C\) statt \(P\) (Kollision mit dem Symbol \(P\)) und Schnitt nicht mehr gegeben (sonst war es #10 mit Kontext); alte #30 war abhängig |
| 30 | 5 | Parameter aus \(P(B)\) als Pfadsumme | Homeoffice: Anteil der Verwaltung (0,4) | drei Zahlensätze verworfen (0,2 : 0,5; 0,5 − 0,1; 0,1 + 0,3 trafen die Lösung); jetzt 60/15/33 %; 0,55, 0,18, 0,44, 0,3 fallen |
| 31 | 6 | begründen (MC) | A, B unabhängig ⇒ \(\bar{A}\), B unabhängig | im Skript an einer unabhängigen Tafel geprüft; Distraktor „einander ausschließen“ widerlegt |
| 32 | 6 | Aussage begründet prüfen (MC) | \(P(A \mid B) = P(B \mid A)\) gilt genau dann, wenn \(P(A) = P(B)\) | **Prüfer: FEHLER** – für disjunkte \(A\), \(B\) sind beide Seiten \(0\) bei \(P(A) \neq P(B)\); jetzt Voraussetzung \(P(A \cap B) > 0\) in der Behauptung und im Lösungsweg. Distraktor „genau dann, wenn unabhängig“ an einer unabhängigen Tafel mit \(P(A) \neq P(B)\) widerlegt |
| 33 | 6 | Zusammenhang, quadratische Gleichung | \(p\) aus \(P(A \cup B) = 0{,}51\) bei \(P(A) = P(B) = p\), unabhängig (0,3) | Lösungsweg nach Prüfer über \((1 - p)^2 = 0{,}49\) statt „p-q-Formel“ (Wort nicht im KC, und \(p\) ist hier die Gesuchte); zweite Lösung 1,7, 0,255, 0,714 fallen. Prüfer: eher Stufe 5 als Abiturformat – belassen, für den Autor vermerkt |
| 34 | 6 | beurteilen (MC) | mit/ohne Zurücklegen: unabhängig oder nicht (KC Z. 1952) | \(P(B)\) ohne Zurücklegen = 3/8 im Skript aus allen Ziehungen bestätigt |
| 35 | 6 | Grenzfall, Ungleichung in \(p\) | \(P(A \mid E) = 0{,}9\), \(P(A \mid \bar{E}) = 0{,}03\): kleinstes \(P(E)\) mit \(P(E \mid A) \geq 0{,}5\) (3,2 %); Deutung (Alarmanlage) nur im Lösungsweg | erst 95 %/2 %: der Fehlweg 0,02/0,95 = 2,1 rundete wie die Lösung 2,06; jetzt 90 %/3 %: Lösung 3,226 → 3,2, Fehlweg 3,33 fällt (Toleranz 0,04). Prüfer: Struktur wie 9-daten #35 (Test, kleinste Anzahl Kranker für zwei Drittel) und gleicher Kontext wie #21 → nach Prüfervorschlag in Formelschreibweise ohne Kontext in der Frage |
| 36 | 6 | Zusammenhang herstellen | \(P(A) = 4 \cdot P(B)\) aus \(P(A \mid B) = 0{,}8\), \(P(B \mid A) = 0{,}2\) (4) | 0,25, 0,6, 0,16 fallen; 0,8 : 0,2 ist der Rechenweg |

Nachrechnen: `rechne_bw.py`, 36 von 36 ohne Fehler (Ausgaben `aus_bw_L1..L6.txt`): Tafeln aus den vier Feldern aufgebaut, Bäume in Tafeln
übersetzt, Urnen über alle geordneten Ziehungen; Parameter durch Suche über ein Raster. Nicht gerechnet, nur begrifflich entschieden: #2, #15,
#21 und die Begründungstexte der Distraktoren in #10, #29, #31, #32, #34.
Zweiter Prüfdurchgang (frischer Agent ohne Browser, alle 36, Vergleich mit 9-daten-zufall-boxplot, 8-zufallsversuche-mehrstufig,
12-stoch-grundlagen): 1 Fehler (#32 disjunkte Ereignisse), 3 Mängel (#18 ein Schritt, #29 Symbol \(P\) als Ereignisname und Stufe, #35
Struktur wie Spalte 9 #35) und 8 Hinweise (#10 Wortlaut, #12 Zahlen wie 9-daten #8, #17 Urne wie Schwestertrainer #21, #21/#35 gleicher
Kontext, #23 Sek-I-Frageform, #27 Lösungszahl wie 8-zufall #36, #30 Nähe zu 9-daten #29, #33 „p-q-Formel“) – alle eingearbeitet außer #30
(Kenntnisnahme; mit \(x\) als Wahrscheinlichkeit erkennbar mehr); bei #17 und #27 andere Zahlen als vorgeschlagen (siehe Tabelle). Kein
Nachtrags-Prüfer: Die neuen Zahlen von #12, #17, #18, #27, #29, #30, #35 sind im Skript mit Fehlweg- und Zufallsnetz nachgerechnet und in der
Endfassung im Bild angesehen (`bw_nach1-01.png`, `bw_nach2-01.png` bei 360 px, `bw_nach3-01.png`).
