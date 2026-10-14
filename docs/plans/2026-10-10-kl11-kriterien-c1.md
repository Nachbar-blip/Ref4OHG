# Kriterien Klasse 11 (Einführungsphase), Block C1: Monotonie & Krümmung, Extrem- & Wendepunkte — Level-Durchgang 2026-10

Je Trainer ein Abschnitt (Format: Plan `2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, „Kriterien-Datei“).
KC = Kerncurriculum Mathematik für die gymnasiale Oberstufe, Niedersachsen (`ma_go_kc_2019.txt`), Zeilenangaben dort.
Lesart der Stufen wie in Block A2/B1: Stufe 4 = Verfahren selbst wählen, Umkehraufgabe, Modell aus Text; Stufe 5 = zwei Verfahren verbinden,
Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung finden; Stufe 6 = Abiturformat des hilfsmittelfreien Teils: begründen,
beurteilen, Zusammenhang herstellen, Fallunterscheidung. „Befund“ beschreibt den Stand vor dem Durchgang.

## KC-Befund zu Monotonie, Krümmung, Extrem- und Wendestellen (Einführungsphase, Lernbereich „Ableitungen“, Z. 1700–1777)

- Z. 1702–1703 (Intentionen): „Beschreibung der Graphen … um die Quantifizierbarkeit des Steigungsverhaltens sowie die Extrem- und
  Wendepunkte systematisch erweitert“ — Extrem- **und Wendepunkte** stehen ausdrücklich in der Einführungsphase.
- Z. 1715–1717: „Notwendige und hinreichende Kriterien für lokale Extrem- und für Wendestellen werden anschaulich aus der Betrachtung
  der Graphen zur Ausgangsfunktion und zu den **Ableitungsfunktionen** gewonnen.“ Plural: Graph von \(f\), \(f'\) **und** \(f''\) —
  die zweite Ableitung ist damit in der Einführungsphase gedeckt, aber als anschaulich gewonnenes Kriterium, nicht als Kalkül.
- Z. 1767–1768 (Kern, „Verwendung von Ableitungen“): „Funktionen und ihre Graphen auf Monotonie untersuchen“ und „Kriterien für
  lokale Extrem- und Wendestellen entwickeln und anwenden“.
- **Nicht im KC-Wortlaut** (ganze Datei): „Krümmung“, „zweite Ableitung“, „dritte Ableitung“/\(f'''\). Krümmung ist in der Sache gedeckt
  (Wendestelle = Krümmungswechsel, Kriterium über den Graphen von \(f''\)); der Abgleich (Z. 154, 366) wertet das gleich. Beibehalten,
  als Autorenfrage vermerkt. \(f'''(x_0) \neq 0\) als hinreichende Bedingung ist kein KC-Inhalt — in beiden Trainern wird deshalb der
  **Vorzeichenwechsel von \(f''\)** (gleichbedeutend: \(f'\) hat dort eine Extremstelle) als hinreichendes Wendestellen-Kriterium
  verwendet; \(f'''\) kommt in Frage, Optionen, Tipp und Lösungsweg nicht mehr vor.
- Qualifikationsphase (G4/G5) bleibt außen vor: keine \(e\)-Funktion, kein \(\ln\), keine Produkt-/Kettenregel, keine Funktionenscharen
  mit vollständiger Diskussion; Parameter nur als einzelne Bedingung (Umkehraufgabe) oder als Paar von Bedingungen.

## Zuschnitt der zwei Trainer des Blocks 11C1 (gegen 11B1/11B2 und gegen 11C2 abgegrenzt)

- **`11-monotonie-kruemmung` („Monotonie und Krümmung“)** — Monotoniesatz (Vorzeichen von \(f'\) auf einem Intervall), Monotonieintervalle
  **berechnen** (\(f'\) selbst bilden, Nullstellen, Vorzeichen), strenge Monotonie trotz einzelner Nullstelle von \(f'\) ohne
  Vorzeichenwechsel, Parameterbedingung für Monotonie auf ganz \(\mathbb{R}\) (Diskriminante von \(f'\)); Krümmung als Monotonie von \(f'\)
  (\(f'' \gt 0\) linksgekrümmt, \(f'' \lt 0\) rechtsgekrümmt), Krümmungsintervalle, Krümmungswechsel als Grenze eines Krümmungsintervalls,
  Stelle größter/kleinster Steigung (Extremstelle von \(f'\)), Sachkontext („nimmt zu, aber immer langsamer“), Fehlersuche an
  Vorzeichentabellen, Aussagen über Monotonie/Krümmung beurteilen. Hoch-/Tiefpunkt und Wendestelle kommen nur als **Folge** im Lösungsweg
  vor („dort wechselt \(f'\) das Vorzeichen“), nie als gesuchte Größe mit Koordinaten.
  **Nicht hier:** Koordinaten von Hoch-, Tief- oder Wendepunkten, Art eines Extrempunkts mit hinreichendem Kriterium, Parameter aus
  Extrem-/Wendebedingungen, globale Extrema, Randextrema.
- **`11-extrempunkte-wendepunkte` („Extrempunkte und Wendepunkte“)** — notwendige Bedingung \(f'(x_0) = 0\); hinreichend:
  Vorzeichenwechsel von \(f'\) (anschaulich, KC-nah) **oder** \(f''(x_0) \neq 0\); Koordinaten von Hoch- und Tiefpunkten; Sattelpunkt
  (\(f' = 0\) ohne Vorzeichenwechsel); Wendestelle: \(f''(x_0) = 0\) **und** Vorzeichenwechsel von \(f''\); Wendepunkt-Koordinaten;
  lokal gegen global, Randextrema auf einem Intervall; Wendestelle als Stelle stärkster Änderung im Sachkontext; Parameter aus einer oder
  zwei Extrem-/Wendebedingungen; Stufe 6: Aussagen über die Kriterien beurteilen (Umkehrung der hinreichenden Bedingung, \(f'' = 0\)
  entscheidet nichts), Fallunterscheidung nach einem Parameter, Anzahl der Wendestellen aus der Anzahl der Extremstellen begründen.
  **Nicht hier:** Monotonie- und Krümmungsintervalle als Ziel, Extremwertaufgaben mit Nebenbedingung, vollständige Kurvendiskussion,
  Nullstellen von \(f\), Polynomdivision.
- Abgrenzung gegen 11B1 („Ableitungsfunktion“, `11-grenzwerte`): dort wird aus dem Vorzeichen von \(f'\) nur auf Steigen/Fallen und
  anschaulich auf Hoch-/Tiefpunkt geschlossen (ohne Monotoniesatz als Begriff, ohne \(f''\)); `11-grenzwerte` #15 gibt \(f'\) als Term vor,
  hier wird \(f'\) stets selbst gebildet. `11-grenzwerte` #1 und `11-monotonie-kruemmung` #5 tragen dieselbe Grundidee (\(f' \gt 0\) auf einem
  Intervall) — hier mit dem Fachbegriff „streng monoton steigend“ als Stufe-1-Grundlage belassen (Autorenhinweis).
- Abgrenzung gegen 11C2 (`11-kurvendiskussion`, `11-extremwertaufgaben`; noch nicht bearbeitet): keine Extremwertaufgaben mit Nebenbedingung,
  keine vollständigen Diskussionen. Für 11C2 vermerkt: `11-kurvendiskussion` #24 (Differenz der \(y\)-Werte von Hoch- und Tiefpunkt) und
  #22 (\(c\): Tiefpunkt auf der \(x\)-Achse) sind sinngleich zu den **alten** Aufgaben #28/#35 hier (beide hier ersetzt); #30 dort
  (\(x^3 + ax^2 + 3x\), waagerechte Tangente ohne Extrempunkt) ist der Grenzfall von `11-monotonie-kruemmung` #25 (gleiche Funktion!),
  #32 dort (Wendepunkt + waagerechte Tangente → \(a\)) ist nahe an `11-extrempunkte-wendepunkte` #27, #26 dort (\(f'\)-Graph mit Minimum
  → \(f\)) bleibt laut Abgleich in der Kurvendiskussion — hier gibt es keine Aufgabe „Extremstelle von \(f'\) → Wendestelle von \(f\)“ als MC.
- Abgrenzung gegen Block A2: `11-funktionen-ganzrational` #29/#35/#36 und `10-ganzrationale-funktionen` #19/#36 (Verlauf aus faktorisierter
  Form, Vorzeichenbereiche von \(f\)) kommen nicht vor; Vorzeichenuntersuchungen gelten hier nur \(f'\) und \(f''\).
- Funktionen, die in den Nachbarn stehen und hier nicht mehr wiederkehren: \(x^3 - 6x^2 + 9x (+k)\) (alt in beiden Trainern und in der
  Kurvendiskussion), \(x^3 - 3x^2 (+2, +4)\) (Kurvendiskussion #17/#18/#21), \(x^3 - 3x (+2)\) (Kurvendiskussion #13–#15, #31),
  \(x^3 - 12x (+2, +c)\) (Kurvendiskussion #16/#22), \(x^3 + ax^2 + 3x\) (Kurvendiskussion #30) — bis auf die belassenen Altaufgaben
  `11-monotonie-kruemmung` #13 (\(x^3 - 3x^2 + 2\)), #16 (\(x^3 - 3x\)) und #25 (\(x^3 + ax^2 + 3x\)), die 11C2 beim Durchgang der
  Kurvendiskussion kennen muss.

## Stand (2026-10-14, Sitzungsabbruch auf Anweisung des Auftraggebers)

**Nichts gesetzt, nichts committet.** Beide Trainer stehen im Arbeitsverzeichnis wieder auf dem Git-Stand (`git checkout` nur auf die
zwei Pfade). Die unten tabellierten Änderungen sind als Datenmodule `d_mk.py` (20 Aufgaben) und `d_ew.py` (26 Aufgaben) im Scratchpad
`w11c1` des Blocks vorbereitet, waren probeweise gesetzt, nachgerechnet (`rechne_mk.py`, `rechne_ew.py`: je 36/36 ohne Fehler),
durch alle Gates (level_check, lehrplan_check, katex_check, pytest, test_trainer) und die Sichtprüfung (`sicht/mk_00..03`, `ew_00..04`)
gelaufen. Der zweite Prüfer für `11-monotonie-kruemmung` hat berichtet (0 FEHLER, 10 MANGEL, 8 HINWEIS); die daraus beschlossenen
Nachbesserungen stehen in `STAND.md` des Scratchpads und sind **noch nicht** in `d_mk.py` eingearbeitet. Für
`11-extrempunkte-wendepunkte` war der zweite Prüfdurchgang gerade gestartet (nur lesend) und ist noch nicht ausgewertet.
Die Tabellen unten beschreiben also den vorbereiteten, nicht den eingesetzten Zustand.

## 11-monotonie-kruemmung — Monotonie und Krümmung (Durchgang)
KC: EP „Ableitungen“, G3 (GO Z. 1702–1703, 1715–1717, 1767–1768). Gelesen: alle 36 Aufgaben. Urteil Lehrplan: passt; „Krümmung“
und \(f''\) als anschaulich gewonnenes Kriterium (Z. 1716 „Ableitungsfunktionen“), Monotoniesatz als Begriff (Z. 1767). Keine QP-Inhalte.
Abgleich Z. 154 („passt in der Sache; Krümmung nicht im KC“): belassen, Begriff als Autorenfrage. Geändert: 20 Aufgaben (3 Wortlaut, 17 inhaltlich).

| id | Stufe | Kriterium laut Rubrik | Befund | Änderung |
|---|---|---|---|---|
| 1, 2, 4 | 1 | ein Schritt | „\(f\) ist an der Stelle streng monoton steigend“ – Monotonie ist eine Intervalleigenschaft | Wortlaut: „Der Graph steigt/fällt in der Umgebung der Stelle“ |
| 11 | 2 | Standardverfahren | war \(f'(1)\) berechnen – Ableitungsregel, kein Monotonie-/Krümmungsinhalt | neu: Krümmung von \(x^2 + 4x\) (MC, \(f'' = 2\)) |
| 14 | 3 | Zwischenergebnis | war \(f''(0)\) von \(x^3 - 6x^2 + 9x + 1\) – reines Ableiten, gleiche Funktion wie alt in `11-extrempunkte-wendepunkte` #11/#15/#16 | neu: Stelle des Krümmungswechsels von \(x^3 - 9x^2 + 4x\) (3) |
| 17 | 3 | Zwischenergebnis | war „größere Nullstelle von \(f'\)“ (keine Monotonie-Frage); Funktion = \(2(x^3 - 6x^2 + 9x)\), Echo zu EW alt #35 | neu: Übergang fallend → steigend bei \(2x^3 - 15x^2 + 24x\) (4) |
| 19 | 4 | Verfahren wählen / Umkehr | war Monotonieintervall von \(x^3 - 3x^2\) als MC – sinngleich zu #13 (Stufe 3) und zu alt #26 | neu: Länge des Fallintervalls von \(x^3 + 3x^2 - 9x + 8\) (4) |
| 20 | 4 | Modell aus Text | trägt (\(f'\)-Graph in Worten → Tiefpunkt; laut B1 hier zu belassen) | — |
| 21 | 4 | Verfahren wählen | war Wendestelle von \(\frac14 x^4 - 2x^2 + 1\) über \(f''\) und \(f'''\) – gehört in EW-Trainer, \(f'''\) nicht im KC | neu: Länge des rechtsgekrümmten Bereichs von \(x^4 - 54x^2 + 1\) (6) |
| 22 | 4 | Modell aus Text | trägt (Baumbestand: steigend, rechtsgekrümmt) | — |
| 23 | 4 | Verfahren wählen | trägt in der Form; Funktion \(x^3 - 3x^2\) war dreimal im Trainer | Zahlen neu: \(2x^3 - 27x^2 + 4x\), Stelle 4,5 (Dezimalzahl, Toleranz 0,01) |
| 24 | 4 | Verfahren wählen | war „\(f''\) gegeben → Krümmungsbereiche“: ein Schritt, Stufe 2 | neu: Monotonie von \(f'\) in Worten → Krümmung von \(f\) (MC, Distraktoren: Verwechslung \(f'\)/\(f\), waagerechte Tangente) |
| 25 | 5 | Parameter | trägt (\(-3 \leq a \leq 3\), Diskriminante); gleiche Funktion wie `11-kurvendiskussion` #30 (für 11C2 vermerkt) | — |
| 26 | 5 | zwei Verfahren | war Intervalllänge von \(x^3 - 3x^2 + 2\) (ein Verfahren, Stufe 4; Idee nach #19 gewandert) | neu: Schnitt von Fall- und Rechtskrümmungsintervall bei \(x^3 - 9x^2 + 15x\) (Länge 2) |
| 27 | 5 | Modell aus Text | Modellfehler: \(V'(4) = -3\), das Becken lief zwischen Minute 3 und 5 leer, obwohl es sich „füllt“; Lösung 4 = 12 : 3 | Zahlen neu: \(V(t) = 2t^3 - 24t^2 + 100t\) (\(V' \gt 0\) auf \([0; 10]\)), Antwort 4 |
| 28 | 5 | Fehler finden | trägt (\(f' = (x-3)^2\): Schritt 3) | — |
| 29 | 5 | zwei Verfahren | war Wendestelle aus linearem \(f''\) – ein Schritt, Stufe 2, Wendestelle gehört in EW | neu: \(f'\) aus Scheitelpunkt \((2 \mid 9)\) aufstellen, Ungleichung lösen → Länge 6 |
| 30 | 5 | Fehler finden | war Länge des Rechtskrümmungsbereichs (ein Verfahren; Idee nach #21) | neu: Fehler in einer Vorzeichentabelle (Probestelle gilt nur zwischen benachbarten Nullstellen) |
| 31 | 6 | Aussage beurteilen | Option „Beide obigen Ansätze“ verweist auf andere Optionen (werden gemischt); Ansatz B (\(f' = 0\) ⇒ Minimum) war selbst fehlerhaft | neu: Behauptung „\(f' \geq 0\) ⇒ streng monoton“ beurteilen (Gegenbeispiel: \(f'\) auf einem Teilintervall null) |
| 32 | 6 | Abiturformat | Option „Alle Angaben in A und B“ verweist auf Buchstaben; Tipp nannte \(f'\) und \(f''\) fertig | neu: \(x^4 + bx^2\), rechtsgekrümmter Bereich der Länge 4 → \(b = -24\) (Fallunterscheidung \(b \geq 0\) / \(b \lt 0\)) |
| 33 | 6 | Parameter aus zwei Bedingungen | trägt in der Form; \(x^3 + ax^2 + bx\) mit Wendestelle 1 war identisch zu EW #27 | Zahlen neu: Krümmungswechsel bei 2, \(b \geq 12\); „Wendepunkt“ → „wechselt von Rechts- zu Linkskrümmung“ |
| 34 | 6 | Abiturformat | war Abstand der Wendestellen von \(x^4 - ax^2\) → \(a\): Wendepunkt-Koordinaten, gehört in EW (Idee als Krümmungsaufgabe in #32) | neu: „\(f'' \gt 0\) überall – was folgt zwingend?“ (Monotoniesatz auf \(f'\); \(x^2\) widerlegt die Distraktoren) |
| 35 | 6 | Aussage begründet prüfen | trägt; Tipp nannte \(f'\) faktorisiert (fertige Gleichung) | Tipp neu (Weg: faktorisieren, Vorzeichenwechsel prüfen); Lösungsweg um die Fehler der Distraktoren ergänzt |
| 36 | 6 | Abiturformat | trägt in der Sache (\(f' \geq 0\), zwei Sattelstellen); Tipp nannte \(f'\) faktorisiert; „Sattelpunkt“ als Begriff ist EW | Frage als Monotonie-Aussage gefasst, Tipp nennt nur den Weg; Lösung 3 fällt mit dem Exponenten 3 zusammen (ohne Rechnung nicht naheliegend; belassen) |

Stufe 1–3 ohne weiteren Befund; #5 trägt dieselbe Grundidee wie `11-grenzwerte` #1 (dort anschaulich, hier mit dem Begriff „streng monoton“).
Nachrechnen: `rechne_mk.py` (Scratchpad w11c1), 36/36 ohne Fehler; Zufallshinweise #9 (3 = 6 : 2, Stufe 2, Altaufgabe), #14 (3 = 9 : 3 –
das ist der richtige Rechenweg \(18 : 6\)), #36 (s. o.).

## 11-extrempunkte-wendepunkte — Extrempunkte und Wendepunkte (Durchgang)
KC: EP „Ableitungen“, G3 (GO Z. 1702–1703, 1715–1717, 1768). Gelesen: alle 36 Aufgaben. Urteil Lehrplan: passt; \(f'''\) als
hinreichende Bedingung (alt #18, #21, #26, #31) ist kein KC-Inhalt → überall durch den Vorzeichenwechsel von \(f''\) ersetzt.
Abgleich Z. 155 („passt“): bestätigt. Geändert: 26 Aufgaben (2 nur Tipp/Lösungsweg, 24 inhaltlich oder mit neuen Zahlen).

| id | Stufe | Kriterium laut Rubrik | Befund | Änderung |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | \(x^2 - 6x + 5\) auch in `11-monotonie-kruemmung` #9; #1, #3, #5 waren dreimal „\(f' = 0\) bei einer Parabel“ | neu: \(2x^2 - 14x + 3\), Stelle 3,5 als Dezimalzahl |
| 2 | 1 | ein Schritt | Tipp nannte die Antwort („genau eine Stelle“) | Tipp neu |
| 3 | 1 | ein Schritt | Dublette zu #1/#5 | neu: Begriffs-MC „Tiefpunkt: \(f'\) wechselt von − nach +“ |
| 5 | 1 | ein Schritt | Dublette zu #1/#3, Tipp nannte \(f'\) | neu: „Hat \(x^3\) bei 0 einen Extrempunkt?“ (MC) |
| 7, 9 | 2 | Standardverfahren | \(x^3 - 3x\) stand in #7, #9, #17 (und in `11-kurvendiskussion` #13–#15) | #7: \(x^3 - 27x + 1\) (Anzahl 2); #9: \(-x^3 + 3x\), Art bei 1 (Hochpunkt) |
| 8 | 2 | Standardverfahren | Lösung 2 = Konstante 2 im Term (Zufallstreffer) | Konstante 7 |
| 11 | 2 | Standardverfahren | war \(f''(1)\) berechnen (reines Ableiten; gleiche Funktion wie MK alt #14) | neu: Anzahl der Extremstellen von \(x^4 - 18x^2\) (3) |
| 13, 14 | 3 | Zwischenergebnis | gleiche Funktion, gleicher Weg (nur HP/TP getauscht); \(x^3 - 3x^2 + 4\) auch in `11-kurvendiskussion` #21 | #13: \(x^3 - 3x^2 - 9x + 5\), HP-Wert 10; #14: \(-x^3 + 3x^2 + 9x\), TP-Wert −5 |
| 15, 16 | 3 | Zwischenergebnis | gleiche Funktion (WP-\(x\) / WP-\(y\)), Echo zu MK alt #14 | #15: \(4x^3 - 60x^2 + 3x\), Wendestelle 5; #16: \(x^3 + 3x^2 - 4\), WP-\(y\) = −2 |
| 17 | 3 | Zwischenergebnis | \(x^3 - 3x + 2\) auch in #19 und `11-kurvendiskussion` #31 | neu: \(-x^3 + 12x\): HP \((2 \mid 16)\), TP \((-2 \mid -16)\) |
| 18 | 3 | Begriff | Option „\(f'''(x_0) \neq 0\) (oder VZW von \(f''\))“ – \(f'''\) nicht im KC, Doppeloption | Optionen neu: VZW von \(f''\) richtig; Distraktoren \(f' = 0\), \(f = 0\), VZW von \(f'\) |
| 19 | 4 | Verfahren wählen | trägt (globales Maximum auf \([-2; 3]\), Rand) | — |
| 20 | 4 | Modell aus Text | trägt in der Form; Lösung 4 = 12 : 3 (Zufallstreffer) | Zahlen neu: \(N(t) = -2t^3 + 24t^2 + 30t\), Antwort 4, \(N'(4) = 126\) |
| 21 | 4 | Umkehraufgabe | war WP-\(y\) von \((x-2)^3\) (Stufe 3, mit \(f'''\)) | neu: \(b\) aus Wendestelle 4 bei \(x^3 + bx^2 + 5x\) (−12) |
| 22 | 4 | Modell / Deutung | war „\(f'(0) = 0\), \(f''(0) = -4\) ⇒ Maximum“: ein Schritt, Stufe 2 (= #10) | neu: Sachdeutung \(c'(3) = 0\), \(c''(3) \lt 0\) (Wirkstoffkonzentration) |
| 23 | 4 | Umkehraufgabe | trägt (\(b = -2\)) | — |
| 24 | 4 | Aussage prüfen | trägt (kein globales Maximum bei Grad 3) | — |
| 25 | 5 | Sonderfall | trägt (\(x^5\): Sattelpunkt trotz \(f'' = 0\)) | — |
| 26 | 5 | zwei Bedingungen | war Wendestelle \(x \gt 0\) (ein Verfahren, Stufe 3, mit \(f'''\)) | neu: \(ax^3 + bx\) mit Tiefpunkt \((1 \mid -4)\) → \(b = -6\) |
| 27 | 5 | zwei Bedingungen | trägt; nahe an `11-kurvendiskussion` #32 (für 11C2 vermerkt) | — |
| 28 | 5 | zwei Verfahren | war Differenz der \(y\)-Werte von HP/TP bei \(x^3 - 12x\) = `11-kurvendiskussion` #24 | neu: \(x^4 - 8x^3 + c\), Tiefpunkt auf der \(x\)-Achse (Sattelstelle 0 ausschließen) → \(c = 432\) |
| 29 | 5 | Aussage prüfen | trägt (Wendepunkt ⇒ VZW von \(f''\)) | — |
| 30 | 5 | Parameter | trägt in der Form; Lösung 4 = Exponent 4 = Betrag von −4 | \(y\)-Wert −25 → \(a = 10\) |
| 31 | 6 | Abiturformat | war \(a\) aus \(f''(2) = 0\): ein Schritt (Stufe 2), Tipp mit fertiger Gleichung | neu: Umkehrung des hinreichenden Kriteriums beurteilen (\(-x^4\) als Gegenbeispiel) |
| 32 | 6 | Parameter | trägt in der Form; Tipp nannte Hochstelle und Ansatz; Lösung 1 = 3 : 3 | Tipp neu (nur Weg), \(y\)-Wert 16 → \(a = 4\) |
| 33 | 6 | Fallunterscheidung | war \(c\) für Wendepunkt auf der \(x\)-Achse (Stufe 4), Tipp mit fertiger Gleichung | neu: \(x^4 - 2tx^2\): für welche \(t\) genau ein Extrempunkt (größtes ganzzahliges \(t\): 0) |
| 34 | 6 | Zusammenhang herstellen | Option „Sowohl B als auch C“ verweist auf Buchstaben | neu: Grad 4 mit drei Extrempunkten → genau 2 Wendepunkte (Begründung über \(f'\) und Grad von \(f''\)) |
| 35 | 6 | Aussage begründet prüfen | war \(k\) für Hochpunkt auf der \(x\)-Achse (= `11-kurvendiskussion` #22, Tipp mit allem) | neu: \(f' = (x-1)^2(x+2)\) → Tiefpunkt bei −2, Sattelpunkt bei 1 (MC, 2×2-Raster) |
| 36 | 6 | Aussage für alle \(t\) | trägt; Tipp nannte \(f''\) und \(x_W\); Distraktor „für \(t \lt 0\)“ passte nicht zur Frage „für alle \(t \gt 0\)“ | Tipp neu, Distraktor „Wendepunkt auf der \(x\)-Achse“; Lösungsweg um Extremstellen ergänzt |

Stufe 1–3: #4, #6, #10, #12 tragen. Nachrechnen: `rechne_ew.py`, 36/36 ohne Fehler; Zufallshinweise nur Kleinzahlen der Stufen 1–4
(#2: 1, #7: 2, #12: −1, #23: −2 – Altaufgaben mit Begriffs- bzw. Vorzeichencharakter, belassen).
