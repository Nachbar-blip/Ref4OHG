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
