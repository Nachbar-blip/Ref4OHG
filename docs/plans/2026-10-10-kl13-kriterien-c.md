# Kriterien Qualifikationsphase eA (Spalte 13), Block C: Stochastik — Level-Durchgang 2026-10

Je Trainer ein Abschnitt (Format: Plan `2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, „Kriterien-Datei“).
KC = Kerncurriculum Mathematik für die gymnasiale Oberstufe, Niedersachsen (`ma_go_kc_2019.txt`), Zeilenangaben dort.
Lesart der Stufen für die Qualifikationsphase: Stufe 4 = Verfahren selbst wählen, Umkehraufgabe, Modell aus Text; Stufe 5 = zwei Verfahren
verbinden, Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung finden; Stufe 6 = Abiturformat (begründen, beurteilen,
Zusammenhänge herstellen, Grenzen eines Verfahrens). „Befund“ beschreibt den Stand vor dem Durchgang.

## KC-Befund am Wortlaut

Lernbereich „Daten und Zufall“, erhöhtes Anforderungsniveau: Intentionen Z. 2222–2243, Kern Z. 2244–2289; dazu die inhaltsbezogenen
Kompetenzen Z. 1155–1175. Über den gemeinsamen Kern (gA, Z. 1966–1993) hinaus nennt das KC für eA:

- **Normalverteilung** (Z. 2273–2279): „Diskrete und stetige Zufallsgrößen unterscheiden“, „Notwendigkeit von Histogrammen erläutern“,
  „Parameter der Normalverteilung erläutern und in Sachkontexten nutzen“. Dazu Z. 1155–1160: „unterscheiden zwischen diskreten und stetigen
  Zufallsgrößen sowie zwischen Säulendiagrammen und Histogrammen“, „nutzen den Erwartungswert und die Standardabweichung einer
  normalverteilten Zufallsgröße für Interpretationen“.
- **Binomial- und Normalverteilung** (Z. 2280–2289): „Angemessenheit der Approximation der Binomialverteilung durch die Normalverteilung
  beurteilen“, „Prognoseintervalle auch mithilfe von σ-Umgebungen für Anteile berechnen und interpretieren“, „Konfidenzintervalle für den
  Parameter p der Binomialverteilung ermitteln und interpretieren“, „die Intervallgrenzen von Konfidenzintervallen als zufällige Größen
  erläutern“, „die Sicherheitswahrscheinlichkeit als relative Häufigkeit deuten, mit der die Konfidenzintervalle bei Verwendung der
  Normalverteilung den wahren Wert überdecken“, Simulationen.
- Intentionen (Z. 2240–2243): „Prognose- und Konfidenzintervalle lassen sich durch Variation der Parameter ermitteln und mithilfe der
  Normalverteilung auch berechnen. Sie stellen Näherungen für die entsprechenden Intervalle der Binomialverteilung dar.“
- Für gA bleibt (Z. 1990–1992): „Prognoseintervalle grafisch oder tabellarisch ermitteln und interpretieren“ und „beurteilen, ob … ein
  vorgegebener Wert des Parameters p mit einer gegebenen Stichprobe verträglich ist“.

Folgerungen:

- **Kern des Normalverteilungs-Trainers** sind laut Wortlaut nicht die Φ-Tabelle und die z-Transformation (so der alte Trainer: 12 von 36
  Aufgaben), sondern: diskret gegen stetig, Histogramm gegen Säulendiagramm, die Bedeutung von μ und σ, das Nutzen der Verteilung im
  Sachkontext und das Urteil, wann sie eine Binomialverteilung annähern darf. Wahrscheinlichkeiten „mit digitalem Werkzeug“ nennt das KC als
  Verfahren nicht; weil die Trainer ohne Werkzeug auskommen müssen, stehen die nötigen Werte \(\Phi(z)\) als Tabellenwerte in jeder Aufgabe
  (Design 1d: die Φ-Tabelle bleibt als Hilfsmittel). \(\Phi(z)\) wird dabei in Worten erklärt („Wahrscheinlichkeit für einen Wert von höchstens
  \(\mu + z \cdot \sigma\)“), die Standardnormalverteilung als eigener Begriff entfällt.
- **Nicht im KC und deshalb nicht aufgebaut:** die Stetigkeitskorrektur als Rechenverfahren (alte #28–30, #34; Gate-Wort), Quantile als
  Begriff, die Poisson-Näherung (alter Lösungsweg #36), der Hypothesentest mit allen seinen Wörtern.
- **Im KC nicht wörtlich, aber als Mittel zum genannten Zweck verwendet:** die Sigma-Regeln der Normalverteilung (68,3 %, 95,4 %, 99,7 % –
  „Parameter erläutern“), die Faustregel „σ größer als 3“ für die Näherung der Binomialverteilung („Angemessenheit beurteilen“; sie steht in
  jeder Aufgabe, die sie benutzt, im Wortlaut), das Wort Dichtefunktion (nur in #3 als Name des Graphen), die Faktoren 1,64 / 1,96 / 2,58 zu
  den Sicherheitswahrscheinlichkeiten 90 % / 95 % / 99 %.
- **Konfidenzintervall – welche Rechnung?** Das KC nennt keine Formel. Es beschreibt das Konfidenzintervall über die „Variation der Parameter“
  und die Verträglichkeit: alle \(p\), in deren Prognoseintervall die beobachtete relative Häufigkeit \(h\) liegt, also die Ungleichung
  \(|h - p| \le 1{,}96 \cdot \sqrt{p(1-p)/n}\). So wird es im Trainer **definiert** (#6, #27, #35). **Gerechnet** wird – wo nichts anderes
  gesagt ist – mit der üblichen Näherung, bei der in der Standardabweichung \(h\) an die Stelle von \(p\) tritt
  (\(h \pm 1{,}96 \cdot \sqrt{h(1-h)/n}\)); das steht in jeder dieser Aufgaben („Näherung: Standardabweichung mit \(h\) statt \(p\) berechnet“).
  Zwei Aufgaben rechnen ausdrücklich „ohne weitere Näherung“ über die Verträglichkeit (#27: untere Grenze aus der quadratischen Gleichung;
  #35: \(h = 0\), wo die Näherung versagt). Die Entscheidung, welche der beiden Rechnungen der Regelfall sein soll, steht dem Autor zu
  (Lehrwerksfrage) – siehe Bericht.

## Zuschnitt der zwei Trainer und Abstand zur Kern-Stochastik

Vorher: `13-eA-normalverteilung` rechnete auf Stufe 2–4 dreimal dasselbe (z-Wert, Tabellenwert ablesen, einsetzen), auf Stufe 5–6 Quantile
und die Stetigkeitskorrektur; Histogramme und „diskret gegen stetig“ fehlten ganz. `13-eA-beurteilende-statistik` bestand auf Stufe 4–6 aus
Hypothesentests (15 Aufgaben mit Gate-Wörtern), Stufe 2 rechnete Konfidenzintervalle mit der Formel im Text, Stufe 3 Prognoseintervalle für
absolute Trefferzahlen (viermal dieselben Zahlen \(n = 600\), \(p = \frac{1}{6}\)).

- `13-eA-normalverteilung` („Normalverteilung (eA)“): die **stetige Verteilung selbst** – diskret/stetig, Histogramm (Flächeninhalt der Säule
  ist die relative Häufigkeit), Glockenkurve, μ und σ ablesen und deuten, Sigma-Regeln, Wahrscheinlichkeiten und Umkehraufgaben mit
  Tabellenwerten, bedingte Wahrscheinlichkeit und Baumdiagramm mit normalverteilten Größen, Angemessenheit der Näherung einer
  Binomialverteilung. **Keine** Intervalle für Anteile, kein \(h\), kein \(n\) einer Stichprobe.
- `13-eA-beurteilende-statistik` (empfohlener Titel „Prognose- & Konfidenzintervalle (eA)“): der **Schluss zwischen Gesamtheit und
  Stichprobe** – Prognoseintervall für die relative Häufigkeit (σ-Umgebungen **für Anteile** mit den Faktoren 1,64 / 1,96 / 2,58),
  Konfidenzintervall für \(p\), „verträglich“, Einfluss von \(n\) und der Sicherheitswahrscheinlichkeit, Stichprobenumfang, Deutung der
  Sicherheitswahrscheinlichkeit, zufällige Intervallgrenzen. Die Normalverteilung kommt hier nur als Herkunft der Faktoren vor.
- Brücke zwischen beiden: `13-eA-normalverteilung` #19 (welcher Tabellenwert gehört zu „95 % in der Mitte“ – 1,96, nicht 1,64) erklärt den
  Faktor, mit dem der zweite Trainer rechnet.
- **Kern-Trainer `12-stoch-sigma-umgebungen`** (gA, wird in Welle 12 zugeschnitten): Sigma-Regeln und Prognoseintervalle für **absolute
  Trefferzahlen** einer binomialverteilten Zufallsgröße mit \(1\sigma / 2\sigma / 3\sigma\), „verträglich“ am abgelesenen Intervall. Die beiden
  eA-Trainer rechnen nirgends mit absoluten 2σ-Intervallen einer Binomialverteilung. Was dort für Anteile gerechnet wird (alte #21, #22, #24,
  #28, #30 „Schwankungsintervall für die relative Häufigkeit“), steht jetzt hier auf Stufe 2–4 und kann dort ohne Verlust entfallen.
  `12-stoch-binomialverteilung` rechnet einzelne und kumulierte Wahrscheinlichkeiten; damit gibt es keine Überschneidung.
- Darstellung: nur Text und KaTeX. Histogramme stehen als Tabelle (zwei Spalten, `\footnotesize`), Glockenkurven in Worten (Hochpunkt,
  Wendestellen). Die Tabellenwerte \(\Phi(z)\) stehen im Fließtext: Eine Tabelle mit vier Wertespalten lief bei 360 px über.
- Eingabe: eine Zahl je Aufgabe (Grenze, Breite, Anzahl, Faktor); Intervalle als Ganzes nur in MC.

## 13-eA-normalverteilung — Normalverteilung (eA)

KC: QP eA „Daten und Zufall“ (G14): Normalverteilung, GO Z. 2273–2279; Angemessenheit der Approximation, Z. 2281–2282; Kompetenzen
Z. 1155–1163. Titel bleibt „Normalverteilung (eA)“ (an allen drei Stellen schon einheitlich).
Gelesen: alle 36 Aufgaben. Urteil Lehrplan vorher: Thema passt, der Schwerpunkt nicht – Kern des KC (diskret/stetig, Histogramm, Parameter
deuten, Angemessenheit der Näherung) fehlte bis auf #36; #28–30 und #34 Stetigkeitskorrektur (Gate), #17 Lösungsweg nennt „Hypothesentests“
(Gate), #36 Lösungsweg Poisson-Näherung (fakultativ „andere Verteilungen“).
Urteil Stufen vorher: Der Trainer lag eine Stufe zu tief und wiederholte sich: Stufe 2 sechsmal der z-Wert, Stufe 3 sechsmal ein Tabellenwert
(ohne Tabelle nicht lösbar), Stufe 4 Einsetzen mit fertiger Transformation im Tipp, Stufe 6 fünfmal dasselbe Quantil im Sachkontext
(„Muster aus Stufe 1–3 mit Kontext“). Deshalb sind alle 36 Aufgaben neu gesetzt; die alten Formen sind eine bis zwei Stufen tiefer wieder da.
Nach dem Durchgang: 36 Aufgaben, davon 10 MC (Stufe 1: 4, Stufe 3: 1, Stufe 5: 2, Stufe 6: 3).

| id | Stufe | Kriterium laut Rubrik | Befund (alt) | Änderung (neu) |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | Fläche unter der Kurve (jetzt #3) | neu: Welche Zufallsgröße ist stetig? (KC Z. 2274) |
| 2 | 1 | ein Schritt | Wendepunkte als MC (jetzt #5) | neu: Histogramm – relative Häufigkeit am Flächeninhalt der Säule (KC Z. 2278, 1157) |
| 3 | 1 | ein Schritt | Sigma-Regel 68,3 % als MC | Gesamtfläche unter der Glockenkurve ist 1 (alte #1), Distraktoren mit Fehlvorstellung statt „2π“ |
| 4 | 1 | ein Schritt | Symmetrie als MC | numerisch: Stelle des Hochpunkts bei gegebenem μ und σ |
| 5 | 1 | ein Schritt | Bedeutung von Φ als MC | numerisch: größere Wendestelle (alte #2) |
| 6 | 1 | ein Schritt | Parameter der Standardnormalverteilung | neu: \(P(X = 170) = 0\) bei stetiger Zufallsgröße |
| 7 | 2 | zwei Schritte | z-Wert | Sigma-Regel anwenden: obere Grenze von \([\mu - 2\sigma; \mu + 2\sigma]\) |
| 8 | 2 | zwei Schritte | z-Wert | standardisierter Wert, negativ (alte #9; einzige verbliebene Aufgabe dieser Art) |
| 9 | 2 | zwei Schritte | z-Wert | σ aus „\(x\) liegt 2,5 Standardabweichungen über μ“ (nach Prüfer 1: vorher sinngleich zu #7) |
| 10 | 2 | zwei Schritte | z-Wert | Symmetrie: \(P(44 \le X \le 56)\) aus \(P(X \le 44)\) |
| 11 | 2 | zwei Schritte | Umkehrung des z-Werts | neu: Säulenhöhe aus relativer Häufigkeit und Klassenbreite |
| 12 | 2 | zwei Schritte | z-Wert | Anteil oberhalb von \(\mu + 2\sigma\) aus der Sigma-Regel |
| 13 | 3 | Zwischenergebnis | \(\Phi(1)\) „ablesen“ ohne Tabelle | \(P(X > 115)\) mit Tabellenwert (Gegenereignis); alte Stufe 4 |
| 14 | 3 | Zwischenergebnis | \(\Phi(2)\) ablesen | symmetrisches Intervall mit einem Tabellenwert |
| 15 | 3 | Zwischenergebnis | Gegenwahrscheinlichkeit | μ und σ aus Hochpunkt und Wendestelle, dann Sigma-Regel (nach Prüfer 1 ohne das Intervall als Formel) |
| 16 | 3 | Zwischenergebnis | Symmetrieregel mit Formel im Tipp | unsymmetrisches Intervall mit zwei Tabellenwerten (alte #23) |
| 17 | 3 | Zwischenergebnis | \(\Phi(1{,}96)\) ablesen; „Hypothesentests“ im Weg | neu: fehlende Säulenhöhe eines Histogramms (Tabelle); Zahlen nach dem Nachrechnen getauscht (Zufallstreffer Differenz der Höhen) |
| 18 | 3 | Zwischenergebnis | Gegenwahrscheinlichkeit | neu, MC: zwei Testergebnisse über Standardabweichungen vergleichen (KC Z. 1158–1160 „für Interpretationen“) |
| 19 | 4 | Umkehraufgabe | Rechenweg im Tipp | symmetrisches 95-%-Intervall: Tabellenwert selbst wählen (1,96, nicht 1,64) – Brücke zum Schwestertrainer |
| 20 | 4 | Umkehraufgabe, Modell aus Text | Einsetzen, Transformation im Tipp | Garantiezeit: untere Grenze zu 6,68 % (nach Prüfer 1; vorher unsymmetrisches Intervall, sinngleich zu #16) |
| 21 | 4 | Umkehraufgabe | Einsetzen | σ aus einem Anteil oberhalb einer Grenze (alte #26, Stufe 5) |
| 22 | 4 | Modell aus Text | Einsetzen | Toleranzbereich: Anteil unbrauchbarer Bauteile, zweiseitig |
| 23 | 4 | Umkehraufgabe | Einsetzen | Faustregel σ > 3: ab welchem \(n\)? (KC Z. 2281) |
| 24 | 4 | Verfahren wählen | Einsetzen | Histogramm mit ungleich breiten Klassen: höchste Säule (nicht die größte relative Häufigkeit); Zahlen nach dem Nachrechnen getauscht |
| 25 | 5 | Parameter aus zwei Bedingungen | ein Quantil | μ aus zwei Anteilen (zwei Gleichungen für μ und σ) |
| 26 | 5 | zwei Verfahren | σ aus einem Anteil (jetzt #21) | bedingte Wahrscheinlichkeit mit normalverteilter Größe |
| 27 | 5 | Fehler finden | μ aus einem Anteil | MC: Fehler \(\Phi(-1{,}5) = -\Phi(1{,}5)\) in vorgelegter Rechnung |
| 28 | 5 | Fehler finden | Stetigkeitskorrektur (nicht im KC) | MC: diskret gegen stetig – \(P(X = 50)\) ist eine Säulenfläche, \(P(Y = 50) = 0\) (Plan: Ersatz durch „diskret gegen stetig“; nach Prüfer 1 als Fehlersuche, der Satz zur Fläche zwischen 49,5 und 50,5 ist gestrichen) |
| 29 | 5 | Umkehraufgabe mit zwei Flächen | Stetigkeitskorrektur | Histogramm: zwei Klassen zusammenfassen, rückwärts (nach Prüfer 1; vorwärts waren es nur zwei Schritte) |
| 30 | 5 | zwei Verfahren | Stetigkeitskorrektur als MC | Säulenhöhe eines Histogramms aus der Normalverteilung (Histogramm-Deutung: Säule und Glockenkurve) |
| 31 | 6 | Zusammenhang begründen | Quantil im Sachkontext | MC: σ verdoppeln – doppelt so breit, halb so hoch, weil die Fläche 1 bleibt |
| 32 | 6 | beurteilen | σ aus Toleranzbereich | MC: Näherung von \(B(50; 0{,}04)\) nicht angemessen – tragfähige Begründung wählen (KC Z. 2281) |
| 33 | 6 | Zusammenhang herstellen | Quantil im Sachkontext | MC: gerundete Messwerte – diskrete Daten im stetigen Modell |
| 34 | 6 | Zusammenhang (zwei Themen) | Näherung mit Stetigkeitskorrektur | zwei Maschinen: Normalverteilung, Baumdiagramm, Umkehrung der Bedingung |
| 35 | 6 | Fallunterscheidung über \(p\) | Quantil im Sachkontext | für welche \(p\) ist bei \(n = 100\) die Faustregel erfüllt (quadratische Ungleichung) |
| 36 | 6 | Zusammenhang, beurteilen | MC Laplace-Bedingung | zwei Maschinen mit verschiedener Streuung: einzustellender Erwartungswert, Einsparung |

Nachrechnen: `rechne_nv.py` (Scratchpad `w13c`), 36 von 36 ohne Fehler; Wahrscheinlichkeiten über `statistics.NormalDist`/`math.erf`
(Rechnerweg) und daneben über die abgedruckten Tabellenwerte – beide Wege runden in jeder Aufgabe auf denselben verlangten Wert und liegen
in der Toleranz. Nicht gerechnet, nur begrifflich entschieden: MC #1 und je eine Option von #2.
Zweiter Prüfdurchgang (alle 36): kein Fehler; vier Mängel (#9 sinngleich zu #7, #20 sinngleich zu #16, #28 und #29 unter Stufe 5) und
fünf Hinweise (#3 Optionslänge, #15 Formel im Text, #32 „rund 7 %“, #34 Toleranz, #35 rein rechnerisch). Alle übernommen außer #35: Die
Aufgabe bleibt als Fallunterscheidung über \(p\); sie ist die parametrische Fassung von „Angemessenheit beurteilen“ und unterscheidet sich
von #23 durch die quadratische Ungleichung. Für den Autor vermerkt.
Nachtrag (die vier neu gefassten Aufgaben #9, #20, #28, #29): ohne Befund.

## 13-eA-beurteilende-statistik — Prognose- & Konfidenzintervalle (eA)

KC: QP eA „Daten und Zufall“ (G14): Prognoseintervalle mit σ-Umgebungen für Anteile, GO Z. 2283; Konfidenzintervalle für \(p\), Z. 2284;
Intervallgrenzen als zufällige Größen, Z. 2285; Sicherheitswahrscheinlichkeit als relative Häufigkeit, Z. 2286–2287; Kompetenzen
Z. 1164–1171; „verträglich“ aus dem gemeinsamen Kern (G9, Z. 1991–1992).
Titel: bisher „Beurteilende Statistik (eA)“; empfohlen „Prognose- & Konfidenzintervalle (eA)“ (nicht gesetzt – Parallelbetrieb).
Verfahren: Teil-Ersatz laut Plan für #19–26, 28, 29, 31–33, 35, 36 (Hypothesentest) – an den ausgewerteten Aufgaben bestätigt: Alle 15
tragen Gate-Wörter oder sind Testaufgaben. Darüber hinaus sind auch die übrigen 21 Aufgaben neu gesetzt, weil der Trainer nach dem Ersatz
nicht über sechs Stufen trug:
- Stufe 1 (#1–6): sechs Begriffs-MC, davon #4 mit der Option „Ein Test, ob eine Hypothese abgelehnt wird“, #5 mit \(\hat{p}\) statt \(h\),
  #6 mit „Standardfehler“ im Tipp. Prognoseintervall und „verträglich“ kamen nicht vor.
- Stufe 2 (#7–12): Konfidenzintervall mit der fertigen Formel im Tipp, #9 und #10 dieselben Zahlen (untere und obere Grenze), #8 und #12
  beide „halbe Breite“.
- Stufe 3 (#13–18): Prognoseintervall für **absolute** Trefferzahlen (gA-Stoff des Kern-Trainers), #14–17 eine Aufgabe in vier Teilen
  (\(\mu\), \(\sigma\), untere, obere Grenze zu \(n = 600\), \(p = \frac{1}{6}\)) mit der Formel in der Frage.
- #27, #30, #34 (nicht in der Ersatzliste): #27 Stichprobenumfang (Form bleibt, jetzt #25 und #34), #30 obere Grenze (jetzt Stufe 3/4),
  #34 Lösungsweg „auf dem 5-%-Niveau abgelehnt“ (Testsprache; Form „liegt der Wert im Konfidenzintervall“ jetzt als „verträglich“).
Aufbau neu: Stufe 1–3 führen vom Prognoseintervall (bekanntes \(p\), Vorhersage für \(h\)) zum Konfidenzintervall (bekanntes \(h\),
Bereich für \(p\)); Stufe 4–6 verlangen die Wahl zwischen beiden, Umkehrungen und Deutungen. Keine der 36 Aufgaben enthält die Wörter
Hypothese, Signifikanz oder Ablehnungsbereich (Volltextsuche über die Trainer-Datei).
Nach dem Durchgang: 36 Aufgaben, davon 11 MC (Stufe 1: 4, Stufe 3: 2, Stufe 4: 1, Stufe 5: 1, Stufe 6: 3).

| id | Stufe | Kriterium laut Rubrik | Befund (alt) | Änderung (neu) |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | Definition Grundgesamtheit | MC: Was bezeichnet \(p\)? (alte #3, ohne \(\hat{p}\); nach Prüfer ohne Sachkontext) |
| 2 | 1 | ein Schritt | Definition Stichprobe | numerisch: relative Häufigkeit \(h\) (alte #5) |
| 3 | 1 | ein Schritt | Parameter \(p\) | MC: Was sagt ein Prognoseintervall vorher? |
| 4 | 1 | ein Schritt | Punktschätzung; Option nennt „Hypothese“ | MC: 95 % gehört zu 1,96 Standardabweichungen |
| 5 | 1 | ein Schritt | \(\hat{p}\) als MC | numerisch: Breite eines Intervalls |
| 6 | 1 | ein Schritt | „größere Stichprobe, genauere Schätzung“ | MC: Wann heißt \(p\) mit einer Stichprobe verträglich? (KC Z. 1991) |
| 7 | 2 | zwei Schritte | Formel-MC | Standardabweichung der relativen Häufigkeit berechnen |
| 8 | 2 | zwei Schritte | halbe Breite, Formel im Tipp | obere Grenze des Prognoseintervalls bei gegebenem σ |
| 9 | 2 | zwei Schritte | untere Grenze (Zahlen wie #10) | \(h\) bestimmen und Standardabweichung schätzen |
| 10 | 2 | zwei Schritte | obere Grenze (Zahlen wie #9) | untere Grenze des Konfidenzintervalls bei gegebener geschätzter Standardabweichung |
| 11 | 2 | zwei Schritte | Bedeutung als MC (jetzt Stufe 6, #31) | vierfacher Stichprobenumfang, halbe Standardabweichung |
| 12 | 2 | zwei Schritte | halbe Breite (wie #8) | von 1,96σ auf 2,58σ umrechnen |
| 13 | 3 | Zwischenergebnis | MC Prognoseintervall | 95-%-Prognoseintervall für die relative Häufigkeit, untere Grenze (KC Z. 2283) |
| 14 | 3 | Zwischenergebnis | \(\mu = np\) mit Formel in der Frage | 90-%-Prognoseintervall, obere Grenze |
| 15 | 3 | Zwischenergebnis | σ mit Formel in der Frage | MC: Würfel – ist \(p = \frac{1}{6}\) verträglich? (vier Intervalle aus vier Rechenwegen) |
| 16 | 3 | Zwischenergebnis | untere Grenze, absolut, Formel in der Frage | Konfidenzintervall aus \(n\) und Trefferzahl, untere Grenze (KC Z. 2284); Zahlen nach dem Prüfer getauscht (die halbe Breite 0,0196 stand dreimal) |
| 17 | 3 | Zwischenergebnis | obere Grenze, absolut, Formel in der Frage | Breite des Konfidenzintervalls |
| 18 | 3 | Zwischenergebnis | MC „120 liegt außerhalb“ | MC: Prognose- oder Konfidenzintervall, und wie weit reicht es? (Raster Intervallart × halbe Breite; nach Prüfer mit Rechnung, vorher sinngleich zu #23) |
| 19 | 4 | Verfahren wählen, Modell aus Text | Hypothesentest | Kundenbefragung: Intervall für den Anteil in der Gesamtheit, obere Grenze (nach dem Nachtrag: #16 fragt die untere); Zahlen nach dem Prüfer getauscht |
| 20 | 4 | Verfahren wählen, Modell aus Text | Hypothesentest | Fluggäste: Bereich für den Anteil in der Stichprobe bei 99 % |
| 21 | 4 | Umkehraufgabe | Hypothesentest | Stichprobenumfang aus einem gegebenen Konfidenzintervall (nach Prüfer: \(n = 625\) mit \(h = 0{,}5\) gibt es nicht; jetzt 200 von 400, Grenzen auf vier Stellen – mit drei Stellen passten alle geraden \(n\) von 392 bis 408) |
| 22 | 4 | Modell aus Text | Hypothesentest | Tombola: Mindestzahl der Gewinne, damit die Angabe verträglich ist (Rundungsrichtung) |
| 23 | 4 | Verfahren wählen | Hypothesentest | MC: In welcher Situation ist ein Konfidenzintervall zu bestimmen? |
| 24 | 4 | Umkehraufgabe | Hypothesentest | Breite auf ein Viertel: sechzehnfacher Stichprobenumfang |
| 25 | 5 | zwei Verfahren | Hypothesentest | Stichprobenumfang für eine geforderte Breite mit Vorstudie (alte #27 mit neuen Zahlen und ohne Formel im Tipp) |
| 26 | 5 | Fehler finden | Hypothesentest | MC: Wurzel vergessen – Intervall der Breite 0,002 aus 400 Versuchen |
| 27 | 5 | zwei Verfahren | Stichprobenumfang (jetzt #25, #34) | Konfidenzintervall über die Verträglichkeit, ohne weitere Näherung: quadratische Gleichung für die untere Grenze; nach Prüfer auf drei Stellen und mit dem Faktor in der Frage (auf zwei Stellen ging der Faktor 2 durch) |
| 28 | 5 | Parameter-Argument | Hypothesentest | größte mögliche Breite bei festem \(n\) (ungünstigster Fall \(h = 0{,}5\)) |
| 29 | 5 | zwei Verfahren | Hypothesentest | markierte Fische: aus dem Intervall für den Anteil auf die Gesamtzahl schließen (kleinster Anteil, größte Zahl); nach Prüfer 2500 statt 300 markierte Fische, damit der zweite Fang unter 10 % des Bestands bleibt |
| 30 | 5 | zwei Verfahren | obere Grenze eines Konfidenzintervalls | 20 unabhängige Intervalle: Wahrscheinlichkeit, dass alle den wahren Wert enthalten (KC Z. 2286); die Annahme „jedes Intervall mit 0,95“ steht nach dem Prüfer in der Frage |
| 31 | 6 | Aussage begründet prüfen | Hypothesentest | MC: „\(p\) liegt mit 95 % Wahrscheinlichkeit im Intervall“ beurteilen (Plan; KC Z. 2285–2287) |
| 32 | 6 | Zusammenhang, beurteilen | Hypothesentest | MC: zwei Institute, zwei verschiedene Intervalle – Intervallgrenzen als zufällige Größen |
| 33 | 6 | beurteilen | Hypothesentest | MC: Schlagzeile „32 % vor 30 %“ mit beiden Konfidenzintervallen beurteilen |
| 34 | 6 | Abiturformat, begründen | Konfidenzintervall mit Testsprache im Weg | Stichprobenumfang für eine geforderte Genauigkeit ohne Vorwissen (Plan) |
| 35 | 6 | Grenzen des Verfahrens | Hypothesentest | \(h = 0\): Näherung liefert \([0; 0]\); obere Grenze über die Verträglichkeit |
| 36 | 6 | Zusammenhang herstellen | Hypothesentest | 99 % statt 95 % bei gleicher Breite: auf das Wievielfache wächst \(n\)? (Plan: Einfluss der Sicherheitswahrscheinlichkeit) |

Nachrechnen: `rechne_ki.py` (Scratchpad `w13c`), 36 von 36 ohne Fehler. Prognoseintervalle über die absolute Trefferzahl gerechnet und mit der
exakten Binomialverteilung auf ihre Trefferwahrscheinlichkeit geprüft; „mindestens“-Fragen und Umkehraufgaben durch Suchen über \(n\) bzw.
\(k\); Grenzen über die Verträglichkeit durch Bisektion. Fehlweg-Netz je Intervallaufgabe: σ statt 1,96σ, Faktor 2, falscher Faktor, Varianz
statt Standardabweichung, Wurzel nur im Zähler, absolute statt relative Häufigkeit, andere Grenze, halbe statt ganze Breite. Nicht gerechnet,
nur begrifflich entschieden: MC #1, #23 und je drei Optionen von #3 und #6, je zwei von #31.
Zweiter Prüfdurchgang (alle 36): kein Fehler; fünf Mängel (#21 Daten nicht realisierbar, #25 Tipp nannte den Zwischenwert, #27 Faktor 2 ging
durch, #29 Fang war 80 % des Bestands, #35 Faktor nur im Tipp) und Hinweise (Faktor 1,96 gehört in jede Frage, die mit ihm rechnet;
Rundungsangabe in #8, #10, #12; #1 Kontext auf Stufe 1; #18 sinngleich zu #23; #30 Modellannahme; #32 Rechnung nennen; #36 Toleranz;
„Runde erst am Ende“ in #25, #34). Alle übernommen. Nicht geändert: #36 bleibt auf Stufe 6 (der Prüfer hält sie für die schwächste der sechs,
dieselbe Proportionalität wie #24 mit einem zweiten Faktor) – für den Autor vermerkt. Die halbe Breite 0,0392 kommt weiterhin in #10, #12,
#28 und #29 vor, 0,0196 nur noch in #13.
Nachtrag (sechs Aufgaben mit neuen Zahlen: #16, #18, #19, #21, #27, #29): kein Fehler, kein Mangel; drei Hinweise übernommen – #27 „Runde erst am Ende“ (der auf 0,038 gerundete Zwischenwert führte auf 0,134), #29 Modellannahme im Text (der zweite Fang wird
näherungsweise als Bernoulli-Kette behandelt; er macht knapp 10 % des Bestands aus), #19 fragt die obere Grenze. Stehen gelassen: Das Produkt
\(0{,}36 \cdot 0{,}64\) steht in #11, #16 und #19 unter der Wurzel, und \(n = 400\) ist Lösung von #21 und Umfang in fünf weiteren Aufgaben.
Hinweis für den Block der Kern-Stochastik: `12-stoch-sigma-umgebungen` #21, #22, #24, #28, #30 rechnen σ-Umgebungen für die relative
Häufigkeit (eA, hier #7–#14 mit den Faktoren 1,64 / 1,96 / 2,58); #5 und #36 dort tragen Testsprache („Signifikanzniveau“, „abgelehnt“).
