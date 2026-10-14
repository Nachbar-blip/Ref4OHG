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
