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
