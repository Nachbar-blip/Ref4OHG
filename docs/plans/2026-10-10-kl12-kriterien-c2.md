# Kriterien Qualifikationsphase Kern (Spalte 12, gA), Block C2: Stochastik — Binomialverteilung und Sigma-Umgebungen — Level-Durchgang 2026-10

Je Trainer ein Abschnitt (Format: Plan `2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, „Kriterien-Datei“).
KC = Kerncurriculum Mathematik für die gymnasiale Oberstufe, Niedersachsen (`ma_go_kc_2019.txt`), Zeilenangaben dort.
Lesart der Stufen für die Qualifikationsphase: Stufe 4 = Verfahren selbst wählen, Umkehraufgabe, Modell aus Text; Stufe 5 = zwei Verfahren
verbinden, Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung finden; Stufe 6 = Abiturformat des hilfsmittelfreien Teils
(begründen, beurteilen, Zusammenhänge herstellen, Grenzfall). „Befund“ beschreibt den Stand vor dem Durchgang.

## KC-Befund am Wortlaut

Lernbereich „Daten und Zufall“, grundlegendes Anforderungsniveau: Intentionen Z. 1946–1966, Kern Z. 1967–1994; dazu die inhaltsbezogenen
Kompetenzen Z. 1138–1145. Für diesen Block gilt der Kern „Binomialverteilung“ (Z. 1979–1993) im Wortlaut:

- „Eignung des Modells beurteilen“; „Beziehung zwischen Häufigkeitsverteilungen und Binomialverteilungen erläutern“; „Zufallsgröße sowie
  Parameter n und p der Binomialverteilung im Sachkontext angeben“; „die Bedeutung der Faktoren im Term \(\binom{n}{k} p^k (1-p)^{n-k}\)
  erläutern“; „Wahrscheinlichkeiten für binomialverteilte Zufallsgrößen berechnen“; „die Kenngrößen Erwartungswert und Standardabweichung
  berechnen“; „die grafischen Darstellungen von Binomialverteilungen im Hinblick auf Parameter und Kenngrößen deuten“;
  „Prognoseintervalle grafisch oder tabellarisch ermitteln und interpretieren“; „beurteilen, ob ein vorgegebener Anteil der Grundgesamtheit
  bzw. ein vorgegebener Wert des Parameters p mit einer gegebenen Stichprobe verträglich ist“; „Simulationen … verwenden“.
- Intentionen (Z. 1960–1966): Binomialverteilungen und ihre grafischen Darstellungen werden „exemplarisch“ erkundet; Situationen, die
  „näherungsweise auf die Binomialverteilung führen“; Prognoseintervalle über Stichproben „bei vorliegender Grundgesamtheit“; umgekehrt die
  Frage, ob ein vermuteter Anteil „mit einer vorliegenden Stichprobe verträglich ist“.
- Kompetenzen Z. 1140–1145: „erläutern und verwenden die Binomialverteilung sowie Binomialkoeffizienten“; „charakterisieren
  Wahrscheinlichkeitsverteilungen anhand der Kenngrößen Erwartungswert und Standardabweichung und nutzen diese bei der Binomialverteilung
  für Interpretationen“; „ermitteln Prognoseintervalle für Stichproben im Kontext der Binomialverteilung“.
- **Nur eA** (Z. 2280–2289, Trainer `13-eA-normalverteilung` und `13-eA-beurteilende-statistik`): Normalverteilung, Näherung der
  Binomialverteilung, „Prognoseintervalle auch mithilfe von σ-Umgebungen für Anteile“, Konfidenzintervalle. **In keinem KC-Teil:**
  Hypothesentest, Signifikanzniveau, Ablehnungsbereich, Nullhypothese (Gate-Wörter).
- **Sigma-Regeln und σ-Umgebungen für absolute Trefferzahlen** nennt das KC für gA nicht wörtlich. Sie bleiben hier als das Mittel, mit dem
  „Erwartungswert und Standardabweichung … bei der Binomialverteilung für Interpretationen“ genutzt werden (Z. 1142–1143) und mit dem ein
  Prognoseintervall ohne Rechner angegeben werden kann (Design 1d, Abgleich Z. 331). Die Werte 68,3 % / 95,4 % / 99,7 % stehen als
  Näherungswerte; „2σ“ wird nirgends als „95 %“ bezeichnet (95 % gehört zum Faktor 1,96, der hier nicht vorkommt). Daneben steht der
  KC-Weg „tabellarisch“: Tabellen kumulierter Wahrscheinlichkeiten \(P(X \le k)\) in der Aufgabe, aus denen ein Intervall abgelesen wird.
- „Bernoulli-Kette“ kennt das KC nicht (Abgleich Z. 298: „fachlich unkritisch“); das Wort bleibt als Name der Voraussetzungen (zwei
  Ausgänge, festes p, unabhängige Durchführungen), weil die niedersächsischen Lehrwerke es tragen. „Tafelwerk“ (#27) ist ersetzt.
- „Formelsammlung bzw. Rechner“: Kumulierte Wahrscheinlichkeiten für n = 50 (#27) stehen in Niedersachsen nicht in der Formelsammlung, sondern
  kommen aus dem digitalen Werkzeug. Der Lösungsweg nennt deshalb „Tabelle oder Rechner“; die Aufgabe bleibt die einzige, die ohne Tabelle in
  der Frage nicht auskommt (Hilfsmittelteil). Alle anderen Aufgaben sind mit Formel, Taschenrechner oder mit abgedruckter Tabelle lösbar.

## Zuschnitt der zwei Trainer

- **`12-stoch-binomialverteilung`** (Titel bleibt „Binomialverteilung“): Bernoulli-Kette erkennen, \(n\) und \(p\) im Sachkontext, Binomialkoeffizient
  (Berechnung und Bedeutung als Anzahl der Pfade), Bedeutung der Faktoren im Term, \(P(X = k)\), kumulierte Wahrscheinlichkeiten über
  Gegenereignis und Intervalle (Sprache „mehr als“, „höchstens“, „mindestens“), Erwartungswert \(n \cdot p\) nur als Zwischenschritt oder in der
  Umkehraufgabe (#28, #30), Beziehung Häufigkeitsverteilung – Binomialverteilung (#18, #36), Eignung des Modells (#2, #5, #35), Umkehraufgaben nach
  \(n\) und \(p\), Deutung der grafischen Darstellung über Kenngrößen (#31), Aussagen prüfen. **Keine σ-Umgebungen, kein Prognoseintervall**
  (alte #33 rechnete mit der Sigma-Regel – jetzt über Symmetrie).
- **`12-stoch-sigma-umgebungen`** (empfohlener Titel „Sigma-Umgebungen & Prognoseintervalle“, bisher „σ-Umgebungen“): Sigma-Regeln (Stufe 1),
  \(\mu = n \cdot p\) und \(\sigma = \sqrt{n p (1-p)}\) als Kenngrößen (Stufe 2 – hier und nicht im Schwestertrainer, weil sie hier der erste Schritt
  jeder Umgebung sind), \(k\sigma\)-Umgebungen für **absolute** Trefferzahlen mit ganzzahligen Grenzen, Prognoseintervall tabellarisch aus einer
  Tabelle \(P(X \le k)\) (#15, #22, #30) und über die Sigma-Regel, Deutung („bei vielen Serien liegen etwa 95,4 % der Trefferzahlen …“),
  „verträglich“ am Intervall, Umkehraufgaben (\(n\), \(p\), \(\mu\) aus Grenzen), Abstand in Standardabweichungen, Zusammenhang \(n\) – Breite,
  größtmögliches \(\sigma\), Simulation deuten. **Keine relativen Häufigkeiten** (alte #21, #22, #24, #28, #30: eA, jetzt im Trainer
  „Prognose- & Konfidenzintervalle (eA)“ Stufe 2–4), **keine Testsprache** (alte #5 „Signifikanzniveau“, #36 „abgelehnt“).
- **Abstand zu `12-stoch-grundlagen`** (Zufallsgrößen & Erwartungswert): Dort wird \(E(X)\), \(V(X)\), \(\sigma\) aus einer Verteilungstabelle
  gerechnet, nie über \(n \cdot p\). Hier kommt keine Verteilungstabelle einer allgemeinen Zufallsgröße vor.
- **Abstand zu `13-eA-normalverteilung`** (#7 Sigma-Regel der Normalverteilung mit μ, σ gegeben; #23 Faustregel σ > 3): Hier gelten die Regeln
  für die Binomialverteilung mit \(n\), \(p\); die Faustregel steht nur als Nebensatz im Lösungsweg von #1 („näherungsweise, sofern σ > 3“).
- **Abstand zu `13-eA-beurteilende-statistik`**: kein \(h\), kein 1,64 / 1,96 / 2,58, kein Konfidenzintervall; „verträglich“ wird hier am
  Prognoseintervall für die **Anzahl** entschieden (KC gA Z. 1991).
- **Abstand zu `9-daten-zufall-boxplot`** (Baumdiagramme, Anzahlen): Berührung nur in #11 (Anzahl der Pfade mit genau zwei Treffern – hier als
  Bedeutung des Binomialkoeffizienten).

## Gemeinsame Regeln dieses Blocks

- **Darstellung:** nur Text und KaTeX. Tabellen kumulierter Wahrscheinlichkeiten als zweispaltiges KaTeX-`array` (\(k\) / \(P(X \le k)\)) mit
  `\footnotesize`, bei 360 px im Bild geprüft. Abgesetzte Formeln kurz; lange Rechnungen in zwei Zeilen.
- **Eingaben:** eine Zahl je Aufgabe; Rundungsvorgabe in der Frage; Toleranzen unter der Rundungsstufe (0,00015 bei vier Stellen, 0,0015 bei
  drei, 0,006 bei zwei; 0 bei ganzzahligen Lösungen).
- **Nachrechnen** (`rechne_bv.py`, `rechne_su.py` mit `slib.py` im Scratchpad `w12c2`, je Stufe aufrufbar): Binomialwahrscheinlichkeiten exakt
  mit `math.comb`, kumulierte Werte als Summe; Umkehraufgaben durch Suche über \(n\) bzw. ein Raster für \(p\). Gegen die Toleranz laufen je
  Aufgabe die Fehlwege (Binomialkoeffizient vergessen, Exponenten vertauscht, falsche Grenze der Summe, Gegenereignis vergessen, \(P(X \le k)\) statt
  \(P(X < k)\), \(1\sigma\)/\(3\sigma\) statt \(2\sigma\), \(\sqrt{np}\) statt \(\sqrt{np(1-p)}\), Varianz statt σ, relative statt absolute Häufigkeit,
  Sigma-Regel statt Tabelle) und das Zufallsnetz (Lösung = gegebene Zahl, Summe, Differenz, Produkt, Quotient, Mittel zweier gegebener Zahlen).

## 12-stoch-binomialverteilung — Binomialverteilung

KC: QP gA „Daten und Zufall“, Kern „Binomialverteilung“ (G9, GO Z. 1979–1989), Intentionen Z. 1960–1963, Kompetenzen Z. 1140–1143.
Titel bleibt „Binomialverteilung“ (an allen drei Stellen schon einheitlich). Stufen-Kommentare im Quelltext angepasst; Dateiname und
`THEMA_KEY` bleiben. Verfahren: Durchgang.
Gelesen: alle 36 Aufgaben. Urteil Lehrplan vorher (Abgleich Z. 170 „passt“): bestätigt – alles im gA-Kern; Befunde des Abgleichs: #27
„Tafelwerk“ (Z. 292) erledigt; „Bernoullikette“ (Z. 298) belassen, Schreibweise nach dem Prüfer überall zu „Bernoulli-Kette“ vereinheitlicht.
Eigene Funde: #27 nannte im Lösungsweg falsche Zwischenwerte (0,9449 − 0,2246; richtig 0,8594 − 0,1390, Differenz zufällig gleich); #22 hatte
den Distraktor „\(P(X = 3) + P(X = 4) + \ldots\)“, der als Aussage wahr ist; #29 (Stufe 5) war eine Dublette von #5; #25, #31, #35 waren dreimal
„mindestens \(n\), damit mindestens ein Treffer“; #33 verlangte Tabellenwerte für \(n = 100\) (Hilfsmittel) und rechnete mit der Sigma-Regel
(Stoff des Schwestertrainers); Stufe 4 war durchweg „berechne \(P(X \le k)\) für \(B(n;\,p)\)“ ohne Modellbildung.
Nach dem Durchgang: 36 Aufgaben, davon 11 MC (Stufe 1: 5, Stufe 2: 2, Stufe 4: 1, Stufe 5: 1, Stufe 6: 3); 19 Aufgaben neu oder neu gefasst,
dazu 7 Wortlautänderungen nach dem Prüfer; Stufe 1–2 ohne Sachkontext (Urne, Würfel, Münze, Test mit Antwortmöglichkeiten).

| id | Stufe | Kriterium laut Rubrik | Befund (alt) / Aufgabe (neu) | Zahlenwahl, Prüfbefunde |
|---|---|---|---|---|
| 2 | 1 | Begriff (MC) | trägt | „Bernoulli-Kette“ (Prüfer) |
| 3 | 1 | ein Schritt | MC mit dem Wert im Tipp → numerisch \(p = 0{,}25\) | 1/8, 1/2 fallen |
| 4 | 1 | ein Schritt (MC) | Qualitätskontrolle (Sachkontext auf Stufe 1, Prüfer) → Urne 2 von 100, mit Zurücklegen | — |
| 5 | 1 | Begriff (MC) | zwei inhaltsgleiche Distraktoren (Prüfer) → „rote und blaue Kugeln“, Distraktor „nicht gleich wahrscheinlich“ | — |
| 7 | 2 | Standardverfahren | \(\binom{5}{2} = 10 = 5 \cdot 2\) (Zufallstreffer) → \(\binom{6}{3} = 20\) | 18, 120 fallen |
| 8 | 2 | Standardverfahren | sinngleich zu #7 (Prüfer) → \(m\) mit \(\binom{9}{2} = \binom{9}{m}\) (7) | \(9 - 2\) ist der Rechenweg |
| 10 | 2 | Bedeutung der Faktoren (MC, KC Z. 1984) | Binomialkoeffizient (vierte gleiche Form) → was gibt \(0{,}8^7\) an? | Distraktoren: Anzahl der Pfade, ganzer Term, „mindestens sieben“ |
| 11 | 2 | Bedeutung des Binomialkoeffizienten | Binomialkoeffizient (fünfte gleiche Form) → Anzahl der Pfade mit genau 2 Treffern (15) | 12, 30, 64 fallen |
| 16 | 3 | n, p aus dem Text, dann \(P(X = 2)\) (KC Z. 1983) | \(0{,}8^4\) (ein Schritt) → Prüfung 10 Fragen je 5 Antworten (0,3020) | p = 0,25: 0,2816 fällt |
| 17 | 3 | Zwischenergebnis | sinngleich zu #13 (Prüfer) → \(P(X \le 1)\) für \(B(8;\,0{,}4)\) (0,1064) | nur \(P(X = 1)\) 0,0896, \(P(X \le 2)\) fallen |
| 18 | 3 | Häufigkeits- gegen Wahrscheinlichkeitsverteilung (KC Z. 1982) | \(0{,}6^5\) (ein Schritt) → erwartete Anzahl der Serien mit genau 2-mal Kopf (187,5) | 125, 250, 0,375 fallen |
| 19 | 4 | Modell aus Text, Gegenereignis wählen | \(P(X \le 1)\) abstrakt mit Formel im Tipp → Medikament 80 %, 6 Personen, höchstens 4 (0,3446) | \(1 - P(5)\) 0,6068, \(P(4)\) 0,2458, \(P(X < 4)\) fallen |
| 20 | 4 | Modell aus Text | \(P(X \ge 2)\) abstrakt → Torwartin 0,1, 8 Schüsse, mindestens einer (0,5695) | nach Prüfer Kontext gewechselt (Glücksrad „mindestens einmal“ = 8-zufallsversuche #19); \(0{,}9^8\), \(P(1)\) fallen |
| 21 | 4 | Umkehraufgabe | \(P(X \le 2)\) abstrakt → \(n\) aus \(P(X = n) = 0{,}07776\) bei \(p = 0{,}6\) (5) | 4, 6 fallen |
| 22 | 4 | Verfahren wählen (MC) | Distraktor als Aussage wahr → „Welcher Term ist gleich \(P(X \ge 3)\)?“ mit drei falschen Identitäten | im Skript als Identitäten geprüft |
| 23 | 4 | Modell aus Text, Sprache übersetzen | \(P(1 \le X \le 3)\) abstrakt → Pralinen: „mehr als eine und weniger als fünf“ (0,6056) | 1..5, 2..5, 1..4 fallen |
| 24 | 4 | Treffer selbst festlegen | \(1 - 0{,}9^6\) mit fertiger Gleichung im Tipp → Saatgut: höchstens eines keimt nicht (0,6590) | „mindestens 11 keimen“ ist derselbe Wert (gleichwertig); \(0{,}9^{12}\), Gegenereignis fallen |
| 25 | 5 | Ungleichung mit Logarithmus | trägt (17 Würfe) | Prüfer: Form wie 8-zufallsversuche #35 (Münze, 90 %) – als Abitur-Standardtyp belassen |
| 26 | 5 | Umkehraufgabe \(p\) | Tipp „Auch hier …“ (Verweis, Prüfer) → Tipp neu | 0,8926/10, 1 − 0,1074 fallen |
| 27 | 5 | zwei Verfahren | Differenz kumulierter Werte, „Tafelwerk“, falsche Zwischenwerte → nach Prüfer: „weicht um höchstens 3 vom Erwartungswert ab“ (erst μ, dann Grenzen, dann Differenz); 0,72 | \(P(X \le 12)\) abgezogen 0,64, F17−F11 0,643 fallen; Gate: „Verwende …“ in der Frage ist Rechenweg-Ansage → umformuliert |
| 28 | 5 | Parameter aus zwei Bedingungen | Tipp mit beiden Formeln (Prüfer) → Tipp nennt nur den Vergleich \(\sigma^2\) mit \(\mu\) | 36 exakt; 27, 54, 6 fallen |
| 29 | 5 | Fehler finden (MC) | Dublette von #5 → Lea vergisst den Binomialkoeffizienten (0,0164 statt 0,2458) | Distraktoren im Skript als Werte geprüft |
| 30 | 5 | zwei Verfahren | \(P(X \le 1)\) im Sachkontext (Stufe 4) → \(n\) aus \(\mu = 8\), dann \(P(X = 10)\) (0,107) | \(n = 50\): 0,1398, \(P(X \le 10)\), ein Pfad fallen |
| 31 | 6 | Säulendiagramme über Kenngrößen deuten (MC, KC Z. 1988) | „mindestens n Lose“ (wie #25) → \(B(100;\,0{,}5)\) gegen \(B(100;\,0{,}1)\): Lage und Breite | Modus 10, σ = 3 gegen 5 im Skript; richtige Option nach Gate gekürzt |
| 32 | 6 | Zusammenhang, Gleichung | trägt (\(p = \frac{1}{6}\)) | 1/5, 1/4 fallen |
| 33 | 6 | Symmetrie nutzen | Tabellenwerte für \(n = 100\) und Sigma-Regel → \(P(45 \le X \le 55)\) aus \(P(X \le 44)\) über die Symmetrie (0,729) | 1 − 0,1356, 2 · 0,1356 fallen; nach Prüfer Satz zur Sigma-Näherung im Lösungsweg |
| 34 | 6 | Fehler finden, begründen (MC) | trägt (\(P(X = 10) \approx 0{,}176\)) | \(\binom{20}{10} 0{,}5^{20} = 0{,}1762\) exakt |
| 35 | 6 | Eignung des Modells beurteilen (MC, KC Z. 1981) | „mindestens n Elfmeter“ (wie #25) → 10 aus 1000 ohne Zurücklegen: warum das Binomialmodell trotzdem brauchbar ist | \(50/991 = 0{,}0505\); hypergeometrisch 0,5973 gegen 0,5987 (Prüfer) |
| 36 | 6 | Behauptung prüfen | Prüfplan „abgelehnt“ → Händler behauptet „jede zehnte Lieferung“; tatsächlich 0,26; nach Prüfer Modellannahme in der Frage | \(1 - 0{,}9^{10}\) 0,65, \(P(X \le 1)\) 0,74, 0,1 fallen |

Belassen (trägt, nachgerechnet): #1, #6, #9, #12, #13, #14, #15 (Stufe 1–3; #13–#15 mit der fertigen Gleichung im Tipp, auf Stufe 3 erlaubt).
Nachrechnen: `rechne_bv.py`, 36 von 36 ohne Fehler (Ausgaben `aus_bv_L1..L6.txt`), alle Binomialwerte exakt über `math.comb`; nicht gerechnet,
nur begrifflich entschieden: #1, #2, #4, #5, #6, #12, #22 (Identitäten von Hand), #35 und die Begründungstexte in #10, #31.
Zweiter Prüfdurchgang (frischer Agent ohne Browser, alle 36, Vergleich mit 12-stoch-sigma-umgebungen, 12-stoch-grundlagen,
13-eA-beurteilende-statistik, 8-zufallsversuche-mehrstufig): kein Fehler; 5 Mängel (#4 Sachkontext auf Stufe 1, #17 sinngleich zu #13, #26 Tipp
verweist, #27 Stufe 5 verfehlt, #28 Tipp liefert die Formeln) und 8 Hinweise (#2 Schreibweise, #5 Distraktoren, #8 sinngleich zu #7, #14 Nähe zu
12-stoch-grundlagen #7, #20 Kontext wie 8-zufall #19, #25 Form wie 8-zufall #35, #33 Nähe zur 1σ-Umgebung, #36 Modellannahme) – alle
übernommen außer #14 und #25 (Kenntnisnahme, siehe Tabelle). Vorschläge nachgerechnet (#8: 36 = 36; #17: 0,1064 mit Fehlwegen; #27: 0,72).
Kein Nachtrags-Prüfer: Die neuen Zahlen von #8 und #17 sind im Skript mit Fehlweg- und Zufallsnetz nachgerechnet und in der Endfassung im Bild
angesehen (`bv_nach1-01.png`, `bv_nach2-01.png` und `bv_nach3-01.png` bei 360 px).

## 12-stoch-sigma-umgebungen — Sigma-Umgebungen und Prognoseintervalle

KC: QP gA „Daten und Zufall“, Kern „Binomialverteilung“ (GO Z. 1979–1993: Kenngrößen Erwartungswert und Standardabweichung, Prognoseintervalle
„grafisch oder tabellarisch“, „verträglich“), Kompetenzen Z. 1142–1145. Titel bisher „σ-Umgebungen“; **empfohlener Titel „Sigma-Umgebungen &
Prognoseintervalle“** (nicht geändert, `index.html` bleibt). Stufen-Kommentare im Quelltext angepasst; Dateiname und `THEMA_KEY` bleiben.
Verfahren: **Teil-Ersatz** (33 von 36 Aufgaben geändert, davon 22 neu gesetzt, 11 nur im Wortlaut).
Gelesen: alle 36 Aufgaben. Urteil Lehrplan vorher (Abgleich Z. 331 „Design 1d“): Befund am Wortlaut geändert – der alte Trainer rechnete auf
Stufe 4–5 fünfmal mit **relativen Häufigkeiten** (#21, #22, #24, #28, #30: eA-Stoff Z. 2284, „σ-Umgebungen für Anteile“), #5 sprach vom
„Signifikanzniveau“, #36 von „abgelehnt“ (Testsprache, in keinem KC-Teil), #19/#23/#29/#31/#33/#36 nannten die fertige Umgebung in der Frage
(die Leistung war nur der Vergleich zweier Zahlen); Stufe 5 bestand aus vier gleichen Grenzberechnungen (#25–#28); Stufe 6 war Stufe-3-Rechnung
mit Kontext (#32, #34, #35). Kein tabellarisches Prognoseintervall, keine Deutung, keine Umkehraufgabe.
Nach dem Durchgang: 36 Aufgaben, davon 11 MC (Stufe 1: 4, Stufe 3: 1, Stufe 4: 2, Stufe 5: 1, Stufe 6: 3); Stufe 1–2 ohne Sachkontext (Würfel
als Zahlenlieferant für \(p = \frac{1}{6}\)); alle Umgebungen für absolute Trefferzahlen; „2σ“ nirgends als „95 %“.

| id | Stufe | Kriterium laut Rubrik | Befund (alt) / Aufgabe (neu) | Zahlenwahl, Prüfbefunde |
|---|---|---|---|---|
| 1 | 1 | Begriff (MC) | trägt; „1-σ-Intervall“ → \(1\sigma\)-Umgebung, Geviertstrich → Halbgeviertstrich (Prüfer) | 68,3 % Standardwert; Nebensatz „sofern σ > 3“ |
| 2 | 1 | Begriff (MC) | trägt; Wortlaut wie #1 | — |
| 3 | 1 | Begriff (MC) | trägt; „3-σ-Regel“ → \(3\sigma\)-Regel | 99,7 % Standardwert |
| 4 | 1 | ein Schritt | MC mit Intervallen → numerisch: obere Grenze der \(1\sigma\)-Umgebung bei μ = 50, σ = 5 (55) | 60, 45, 65 fallen; Zufallsnetz 50 + 5 ist der Rechenweg |
| 5 | 1 | ein Schritt | „Signifikanzniveau“ (Testsprache) → Anteil außerhalb der \(2\sigma\)-Umgebung (4,6) | 2,3, 5, 0,3 fallen |
| 6 | 1 | k ablesen (MC) | trägt; Schreibweise | k = 3 |
| 7 | 2 | Standardverfahren | trägt: μ = 200 · 0,3 = 60 | Prüfer: „ein Schritt“ – belassen, siehe Bilanz |
| 8 | 2 | Standardverfahren | „Runde auf zwei Dezimalstellen“ bei σ = 5 gestrichen (Prüfer) | √50 = 7,07 fällt |
| 9 | 2 | Standardverfahren | trägt: σ = √75 ≈ 8,66 | 10, 75, √300 fallen |
| 10 | 2 | Standardverfahren | trägt: Würfel 180-mal, μ = 30 | Prüfer: „ein Schritt“ – belassen |
| 11 | 2 | Standardverfahren | war Dublette von #10 (180 Würfe, σ = 5) → 720 Würfe, σ = 10 | √120 = 10,95, 120, 100 fallen |
| 12 | 2 | Umkehr auf Stufe 2 | σ für n = 900, p = 0,4 (dieselbe Zahl wie #18, Prüfer) → aus σ = 6, p = 0,5 folgt n = 144 | 12, 72, 36 fallen |
| 13 | 3 | Zwischenergebnis | trägt (untere Grenze 2σ, 40); Schreibweise | √(np)-Weg 35,86 fällt |
| 14 | 3 | Zwischenergebnis | war die obere Grenze zu #13 (gleiche Zahlen) → n = 300, p = 0,2, obere Grenze 1σ (66,93) | 67,75 (√np), 2σ fallen |
| 15 | 3 | Prognoseintervall tabellarisch (KC Z. 1990) | Grenze 1σ mit denselben Zahlen wie #9 → Tabelle \(B(15;\,0{,}4)\), \(P(3 \le X \le 9)\) für die genannte \(2\sigma\)-Umgebung (0,9391) | nach Prüfer mit Sigma-Bezug statt reiner Tabellendifferenz; 2σ-Grenzen [2,21; 9,79] im Skript; F9 − F3, F8 − F2, 0,954 fallen |
| 16 | 3 | Zwischenergebnis | trägt (obere Grenze 3σ, 79,44); Schreibweise | √(np)-Weg 83,24 fällt |
| 17 | 3 | Intervall zuordnen (MC) | n = 100, p = 0,5 wie #13 und Tipp nannte das Intervall (Prüfer) → n = 400, p = 0,2, 3σ-Intervall [56; 104] | Distraktoren 2σ [64; 96], 1σ [72; 88], [48; 112]; Tipp ohne Intervall |
| 18 | 3 | Zwischenergebnis | trägt (Breite 4σ = 58,79); Schreibweise | 2σ = 29,39, 6σ fallen |
| 19 | 4 | Umkehraufgabe | MC „liegt 185 in [180; 220]?“ (Umgebung in der Frage) → n aus der Breite 40 bei p = 0,5 (400) | 1600 (Breite = 2σ), 100, 200 fallen |
| 20 | 4 | verträglich? (MC, KC Z. 1991) | Umgebung in der Frage → Münze 100-mal, 63-mal Kopf: Beurteilung mit selbst berechneter Umgebung | nach Prüfer Distraktoren: √(np)-Weg [36; 64] „verträglich“, 1σ [45; 55]; Lösungsweg nennt beide Fehlwege; exakt \(P(X > 60) = 0{,}018\) |
| 21 | 4 | Modell aus Text | relative Häufigkeit (eA) → Würfel 720-mal: höchstens wie viele Sechsen noch verträglich (140) | nach Prüfer Modellanteil gestärkt (p selbst festlegen, Spielhalle); 141, 130, 150 fallen; exakt \(P(X \le 140) = 0{,}978\) |
| 22 | 4 | Prognoseintervall tabellarisch | relative Häufigkeit (eA) → Tabelle \(B(50;\,0{,}1)\): kleinstes symmetrisches Intervall mit ≥ 90 % (obere Grenze 8) | d = 3: 0,9083; d = 2: 0,7662; Sigma-Regel-Grenze 9 fällt |
| 23 | 4 | Deutung (MC) | „man beobachtet 74“ mit Umgebung in der Frage → was bedeutet „etwa 95,4 % … zwischen 48 und 72“? | Distraktoren: Aussage über p, Anteil der Versuche, „unmöglich“; 2σ-Grenzen [47,04; 72,96] im Skript |
| 24 | 4 | Modell aus Text | relative Häufigkeit (eA) → 90 % erscheinen zum Online-Kurs, 900 Anmeldungen: untere Grenze 2σ (792) | nach Prüfer Kontext gewechselt (Saatgut = 12-stoch-binomialverteilung #24); 801, 783, 753 fallen; exakt \(P(792 \le X \le 828) = 0{,}960\) |
| 25 | 5 | Parameter aus zwei Bedingungen | Grenze 2σ für 360 Würfe (Stufe-3-Muster) → p aus μ = 48 und oberer Grenze 60 (0,25) | 0,2, 0,75, 0,8 fallen |
| 26 | 5 | Fehler finden (MC) | obere Grenze zu #25 (gleiche Zahlen) → Tom rechnet σ = √(np) | Distraktoren im Skript als Werte geprüft (16, 20, √20) |
| 27 | 5 | zwei Verfahren | Grenze 2σ, Ausschuss (Stufe-3-Muster) → 180 Würfe, 46 Sechsen: kleinstes k mit 46 in der \(k\sigma\)-Umgebung (4) | nach Prüfer 42 → 46, damit √(np)-Weg (k = 3) abgewiesen wird; 3,2 fällt |
| 28 | 5 | Parameter aus zwei Bedingungen | relative Häufigkeit (eA) → n aus den unteren Grenzen der 1σ- und 2σ-Umgebung (54, 48): 150 | 135, 120, 60 fallen |
| 29 | 5 | Umkehr, Ganzzahligkeit | MC mit Prognoseintervall in der Frage, Tipp nannte die Lösung → Glücksrad p = 0,3, 100 Drehungen: ab wie vielen Gewinnen wird geprüft (40) | Prüfer schlug n = 500, p = 0,02 vor – dort liefert √(np) ebenfalls 17; hier 41 (√np), 35 (1σ), 44 (3σ), 39 (abgerundet) fallen |
| 30 | 5 | Sigma-Regel gegen Tabelle | relative Häufigkeit (eA) → Tabelle \(B(20;\,0{,}3)\): 2σ-Grenzen selbst bestimmen (2 bis 10), dann \(P(2 \le X \le 10)\) (0,9753) | nach Prüfer hinterlegt der Tabellenwert 0,9753 (exakt 0,9752 im Lösungsweg erklärt); F10 − F2, F10 − F0, F9 − F1, 0,954 fallen |
| 31 | 6 | Behauptung beurteilen (MC, KC Z. 1991) | Umgebung in der Frage → Batterien 90 %, 168 von 200: Umgebung selbst berechnen | nach Prüfer Distraktor „mindestens 1000“ (wie #20) → √(np)-Weg „untere Grenze 153,2, verträglich“; exakt \(P(X \le 168) = 0{,}005\) |
| 32 | 6 | Zusammenhang herstellen | Abstand in σ für eine Lieferung (Stufe-3-Muster, Prüfer) → zwei Lieferungen mit gleichem Anteil 4 %: welche spricht stärker gegen p = 0,03, Abstand in σ (B: 2,64) | A 2,34, 9/√12 = 2,60, 9/11,64, 4 fallen |
| 33 | 6 | Breite gegen n | Wahlprognose mit Umgebung in der Frage (relativ, eA-nah) → für welches n ist die 2σ-Breite 5 % von n (1600) | 400, 6400, 800 fallen |
| 34 | 6 | Aussage begründet prüfen (MC) | obere Grenze 2σ, Medikament (Stufe-3-Muster) → „außerhalb der 2σ-Umgebung ⇒ p sicher falsch“? | Distraktoren: „kann nicht auftreten“, „ab 30 exakt“, „sagt nichts über p“ |
| 35 | 6 | Grenzfall | untere Grenze 2σ, Qualitätskontrolle (Stufe-3-Muster) → größtes σ bei n = 100 (5) | nach Prüfer „Scheitelpunkt“ → Symmetrie der Parabel, Beispiel σ = 4 bei p = 0,2 (statt σ = 3 bei p = 0,1 wie 12-stoch-binomialverteilung #31); √50, 10, 25 fallen |
| 36 | 6 | Simulation deuten (MC, KC Z. 1992) | „abgelehnt“ (Testsprache) → 1000 Serien zu 100 Würfen, 952 in [40; 60] | exakt \(P(40 \le X \le 60) = 0{,}965\); Distraktoren: 68,3 %, „nicht fair“, „beweist p = 0,5“ |

Belassen (trägt, nachgerechnet): #7, #9, #10 (Stufe 2, unverändert).
Nachrechnen: `rechne_su.py`, 36 von 36 ohne Fehler (Ausgaben `aus_su_L1..L6.txt`), alle Tabellenwerte exakt über `math.comb`, Umgebungen aus
\(n\), \(p\); Fehlwegnetz je Grenze (\(k \pm 1\), \(\sqrt{np}\), Varianz, relative Häufigkeit, andere Grenze, \(1 - p\) vertauscht); nicht gerechnet,
nur begrifflich entschieden: #1–#3 (Standardwerte der Sigma-Regel), #6, die Distraktoren der Deutungsaufgaben #23, #34 und die Begründungstexte
in #20, #31, #36.
Zweiter Prüfdurchgang (frischer Agent ohne Browser, alle 36, Vergleich mit 12-stoch-binomialverteilung, 12-stoch-grundlagen,
13-eA-normalverteilung, 13-eA-beurteilende-statistik): kein Fehler; 6 Mängel (#20 MC trivialisiert, #27 √(np)-Weg liefert dasselbe k, #29 Stufe 5
verfehlt und Tipp nennt die Lösung, #30 hinterlegte Lösung ≠ Tabellenweg, #31 Fehlweg ungenutzt, #32 Stufe-3-Muster) und 9 Hinweise (#7/#10
ein Schritt, #8/#9/#11/#12 sinngleich und Rundungssatz, #15 ohne Sigma-Bezug, #17 Zahlen wie #13 und Tipp nennt das Intervall, #21 kaum mehr
als #16, #24 Kontext wie Schwestertrainer, #35 Zahlen und „Scheitelpunkt“, Notation Unicode-σ und Geviertstrich). Übernommen: alle 6 Mängel
(#29 abweichend: Glücksrad p = 0,3 statt des Vorschlags n = 500, p = 0,02, weil dort der √(np)-Fehlweg dieselbe Zahl 17 ergibt – Prüfer hatte
das selbst angemerkt) und die Hinweise #8, #11, #12, #15, #17, #21, #24, #35, Notation. Nicht übernommen: #7/#10 (μ = n·p bleibt auf Stufe 2
als erster Schritt vor σ; Stufe 1 ist mit vier MC und zwei Zahlenaufgaben zur Regel voll; #9 behält den Rundungssatz, da 8,66 nicht ganzzahlig
ist). Vorschläge nachgerechnet (#20 √(np): [35,9; 64,1]; #27: 16/5 = 3,2 → k = 4, √(np): 2,92 → 3; #29: 39,17 → 40, √(np) 40,95 → 41; #30:
0,9829 − 0,0076 = 0,9753; #31: 180 − 2·√180 = 153,2; #32: B 9/3,41 = 2,64 > A 2,34; #12: 0,25 · 144 = 36; #17: μ = 80, σ = 8).
Kein Nachtrags-Prüfer: Die neuen Zahlen (#11, #12, #15, #17, #21, #24, #27, #29, #30, #31, #32, #35) sind im Skript mit Fehlweg- und Zufallsnetz
nachgerechnet und in der Endfassung im Bild angesehen (`su_nach1-01.png`, `su_nach2-01.png` mit Tipp und Lösungsweg, `su_nach3-01.png` bei
360 px für die beiden Tabellen #15, #30); die vollständigen Stufenbögen `su_L1..L6-01.png` und `su_360a/b-01.png` stammen aus dem Stand vor dem
Nachtrag.
