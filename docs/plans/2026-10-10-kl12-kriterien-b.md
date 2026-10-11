# Kriterien Qualifikationsphase Kern (Spalte 12), Block B: Analytische Geometrie — Level-Durchgang 2026-10

Stand: 12-vektoren-grundlagen fertig (Commit 1). Die Abschnitte zu 12-geraden-raum und 12-skalarprodukt folgen mit deren Commits; bis dahin beschreiben KC-Befund und Zuschnitt für diese beiden Trainer den Zielzustand.

Je Trainer ein Abschnitt (Format: Plan `2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, „Kriterien-Datei“).
KC = Kerncurriculum Mathematik für die gymnasiale Oberstufe Niedersachsen (`ma_go_kc_2019.txt`), Zeilenangaben dort.
Lesart der Stufen: Stufe 4 = Verfahren selbst wählen, Umkehraufgabe, Modell aus Text; Stufe 5 = zwei Verfahren verbinden, Parameter aus
zwei Bedingungen, Fehler in vorgelegter Rechnung finden; Stufe 6 = Fallunterscheidung, Aussage begründet prüfen, Format des
hilfsmittelfreien Abiturteils (begründen, beurteilen, Zusammenhang herstellen). „Befund“ beschreibt den Stand vor dem Durchgang.

## KC-Befund am Wortlaut

Lernbereich „Raumanschauung und Koordinatisierung“, grundlegendes Anforderungsniveau (G8, Z. 1909–1941). Kern:

| Kürzel | KC-Zeile | Wortlaut | Trainer |
|---|---|---|---|
| K1 | 1921 | Punkte und Vektoren in Ebene und Raum durch Tupel beschreiben | vektoren-grundlagen |
| K2 | 1922–1923 | die bildliche Darstellung und Koordinatisierung zur Beschreibung von Punkten, Strecken, ebenen Flächen und einfachen Körpern nutzen | alle drei (Quader, Pyramide, Würfel, Vierecke) |
| K3 | 1924–1925 | Addition, Subtraktion und skalare Multiplikation von Vektoren anwenden und geometrisch veranschaulichen | vektoren-grundlagen |
| K4 | 1926 | Kollinearität zweier Vektoren überprüfen | vektoren-grundlagen; als Werkzeug in geraden-raum |
| K5 | 1927 | Geraden- und Ebenengleichungen in Parameterform verwenden | geraden-raum |
| K6 | 1929 | Abstände zwischen Punkten bestimmen | vektoren-grundlagen; als Werkzeug in geraden-raum |
| K7 | 1930 | Skalarprodukt geometrisch als Ergebnis einer Projektion deuten und verwenden | skalarprodukt |
| K8 | 1931 | Orthogonalität zweier Vektoren überprüfen | skalarprodukt |
| K9 | 1932 | Winkelgrößen zwischen Strecken und Geraden bestimmen | skalarprodukt |
| K10 | 1933 | Lagebeziehungen von Geraden untersuchen und Schnittpunkte bestimmen | geraden-raum |

Fakultativ für gA (Z. 1935–1936): Lagebeziehung zwischen Geraden und Ebenen; Ebenengleichungen in Normalenform; Kreis- und
Kugelgleichung. Nur eA (Z. 2147–2165): Projektion mit Matrizen, Normalen- und Koordinatenform samt Formwechsel, Abstände zwischen
Punkten, Geraden und Ebenen, Winkelgrößen allgemein, Lagebeziehungen mit Ebenen, Gauß-Algorithmus. Das Vektorprodukt steht im KC nur
für das Berufliche Gymnasium (G15).

Was daraus folgt:

- **Ebenen in Parameterform sind gA-Kern** (K5), nicht nur Geraden. Nach dem Umzug von `12-ebenen` in die eA-Spalte gab es dafür in der
  Kernspalte keine Aufgabe; `12-geraden-raum` trägt jetzt 14 Ebenen-Aufgaben auf allen sechs Stufen (Plan: „aufstellen aus drei
  Punkten, Punktprobe, Spurpunkte“; dazu Parameter festhalten, Parameterbereich deuten, gleiche Ebene in anderer Darstellung, drei
  Punkte auf einer Geraden).
- **Lage Gerade–Ebene bleibt draußen** (fakultativ). Die „Spurpunkte“ der Ebene aus dem Plan sind als Schnittpunkt mit einer
  Koordinatenachse über die Parameterform gestellt (zwei Koordinaten null setzen, `12-geraden-raum` #21); ein Durchstoßpunkt einer
  beliebigen Geraden durch eine Ebene (3×3-System) kommt nicht vor. Das ist eine Auslegung des Plans, siehe „Für den Autor“ im Bericht.
- **Abstände nur zwischen Punkten** (K6): Abstand paralleler Geraden und Punkt–Gerade (`12-geraden-raum` alt #27, #35) sind entfallen.
  Die Projektion (K7) wird als Länge und als Zerlegung eines Vektors geübt, nicht als Lotfußpunkt- oder Abstandsverfahren.
- **Winkel nur zwischen Strecken und Geraden** (K9): Winkel „mit der Grundfläche“ oder „mit der \(x_1x_2\)-Ebene“ (alt in allen drei
  Trainern) sind als Winkel zwischen einer Strecke und ihrem Grundriss gestellt oder entfallen.
- **Die Projektion (K7) fehlte ganz.** `12-skalarprodukt` hat sie jetzt auf Stufe 3 bis 5.
- **Kollinearität (K4) fehlte ganz** – in `12-vektoren-grundlagen` gab es keine Aufgabe dazu; jetzt auf Stufe 2 bis 6.

## Zuschnitt der drei Trainer

Vorher überschnitten sich die Trainer stark: `12-vektoren-grundlagen` rechnete auf Stufe 4 bis 6 Skalarprodukte, Winkel und
Orthogonalität (dieselbe Aufgabe „für welches \(t\) orthogonal“ stand in beiden Trainern, alt vg #34 und sp #23); `12-geraden-raum`
rechnete Schnittwinkel und Orthogonalität; die Koordinaten hießen \(x, y, z\), \(x_1, x_2, x_3\) oder „erste Komponente“.

- `12-vektoren-grundlagen`: K1, K3, K4, K6 und K2 über Längen und Parallelität – Tupel, Rechnen mit Vektoren und seine geometrische
  Deutung (Verschiebung, Gegenvektor, Vektorzug), Verbindungsvektor, Mittel- und Teilpunkt, Kollinearität von Vektoren, Länge, Abstand,
  Einheitsvektor, Dreiecke und Vierecke über Seitenlängen und parallele Seiten, Quader in Koordinaten. **Kein** Skalarprodukt, **keine**
  Winkel und rechten Winkel, **keine** Geradengleichung.
- `12-geraden-raum`: K5, K10 – Geraden und Ebenen in Parameterform aufstellen und verwenden, Punktprobe, Spurpunkte, Lage zweier
  Geraden, Schnittpunkt, geradlinige Bewegungen (Parameter als Zeit). **Kein** Skalarprodukt. „Liegen drei Punkte auf einer Geraden“
  und „Punkt auf der Geraden durch zwei Punkte mit Parameter“ stehen nur hier (Punktprobe), nicht im Vektoren-Trainer.
- `12-skalarprodukt`: K7, K8, K9 – Skalarprodukt, Projektion, Orthogonalität, Winkel zwischen Vektoren, Strecken und Geraden, rechte
  Winkel in Figuren und Körpern (Rechteck, Quadrat, Raute, Würfel, Pyramide). Geradengleichungen kommen nur für Schnittwinkel vor.

Abgrenzung zu den Nachbarn: `12-ebenen`, `13-eA-ebenen-lagebeziehungen`, `13-eA-abstaende` (eA) behalten Koordinaten- und Normalenform,
Normalenvektor, Lage Gerade–Ebene und Ebene–Ebene, alle Abstände außer Punkt–Punkt. `9-pythagoras` rechnet die Raumdiagonale des
Quaders aus Kantenlängen; hier ist der Quader in Koordinaten gegeben und gefragt ist nie die Raumdiagonale selbst.

## Gemeinsame Regeln dieses Blocks

- **Koordinaten** heißen überall \(x_1, x_2, x_3\), auch bei Vektoren („die \(x_3\)-Koordinate von \(\overrightarrow{AB}\)“) und Ebenen
  („\(x_1x_2\)-Ebene“). Punkte stehen als \(A(1\mid-2\mid3)\), Vektoren immer als Spaltenvektoren. Parameter: \(t\) (und \(s\) für die
  zweite Gerade), bei Ebenen \(r\) und \(s\).
- **Eine Zahl je Antwort:** Vektoren, Punkte und Gleichungen werden über eine Koordinate oder als MC abgefragt. Gefragt wird nie eine
  Koordinate, die mit einer anderen Koordinate desselben Ergebnisses übereinstimmt (Befund des Prüfers an vg #9; seither im Fehlweg-Netz
  jeder Aufgabe: „\(x_1\) / \(x_2\) / \(x_3\) verwechselt“).
- **Textgeometrie ohne Bilder:** Körper sind mit allen Eckpunkten oder mit „\(E\) liegt über \(A\), …“ beschrieben, Vierecke mit
  „Eckpunkte in dieser Reihenfolge umlaufend“. Die Lagebeschreibung des Quaders steht als Konstante im Datenmodul.
- **Nachrechnen** (`vlib.py`, `rechne_vg.py`, `rechne_gr.py`, `rechne_sp.py` im Scratchpad `w12b`, ohne sympy): Jede Lösung entsteht
  unabhängig vom Lösungsweg – Gleichungssysteme über ein allgemeines Gauß-Verfahren mit Brüchen, Lagen über Kreuz- und Spatprodukt,
  Winkel über \(\operatorname{atan2}(|\vec a \times \vec b|, \vec a \cdot \vec b)\) statt über den Arkuskosinus, Umkehr- und
  Parameteraufgaben durch Einsetzen aller Kandidaten eines Rasters, Bewegungsaufgaben durch Abtasten der Zeit, Allgemeinaussagen an
  Zufallsbeispielen. Bei MC wird jede Option einzeln ausgewertet. Gegen die Toleranz laufen je Aufgabe die Fehlwege (Vorzeichen,
  vertauschte Punkte, falsche Koordinate, Betrag ohne Wurzel, Parameterwert statt Koordinate, nur ein Teilschritt, Bogenmaß,
  Ergänzungswinkel, Sinus statt Kosinus). Das Zufallsnetz liest die Zahlen aus dem Fragetext und meldet: Lösung gleich einer gegebenen
  Zahl (nirgends stehen gelassen), Summe/Differenz/Produkt/Quotient/Mittel zweier gegebener Zahlen (bei sechs bis zwölf kleinen
  Koordinaten unvermeidlich; stehen gelassen, wo kein Rechenweg dahintersteht).
- **Nicht vom Skript geprüft** sind die Zwischenzahlen in den Lösungswegen; die hat der zweite Prüfer nachgerechnet (Befund vg #2).

## 12-vektoren-grundlagen — Vektoren — Grundlagen
KC: QP gA „Raumanschauung und Koordinatisierung“ (G8): K1 (Z. 1921), K2 (Z. 1922–1923), K3 (Z. 1924–1925), K4 (Z. 1926), K6 (Z. 1929).
Gelesen: alle 36 Aufgaben. Urteil Lehrplan: Der Stoff lag im Lernbereich (Abgleich: „passt“), aber nicht im Zuschnitt und mit zwei Lücken. Aus dem Abgleich: #35 Kreuzprodukt im Tipp und im Lösungsweg – **erledigt** (Aufgabe ersetzt). Eigene Funde: Das Kreuzprodukt stand auch im Lösungsweg von #30 (das Gate meldete es); Kollinearität (K4, Kern) kam in keiner Aufgabe vor; die geometrische Deutung der Rechenoperationen (K3) nur in #32; Körper (K2) nur in #36, und dort als Trigonometrie aus Klasse 10. Stufe 4 bis 6 bestanden zu zwei Dritteln aus Skalarprodukt, Orthogonalität und Winkeln (#19–#25, #29, #30, #33, #34) – Stoff des Schwestertrainers, #34 war dort #23 mit anderen Zahlen.
Titel: bleibt in diesem Block unverändert (Parallelbetrieb; an den drei Stellen stehen heute „Vektoren Wiederholung“ und „Vektoren — Grundlagen“). Empfehlung an allen drei Stellen: „Vektoren: Rechnen, Länge, Kollinearität“ – nennt, was geübt wird, und grenzt gegen „Skalarprodukt“ ab; „Wiederholung“ stimmt nicht, weil Vektoren in Niedersachsen erst in der Qualifikationsphase beginnen.

Befund zum Aufbau: Stufe 1 = sechsmal Addieren/Subtrahieren in der Ebene (#1/#2 sinngleich), Stufe 2 = Einschritt-Rechnungen im Raum, Stufe 3 = dreimal Betrag (#13–#15 sinngleich, zweimal das Ergebnis 3) und eine Formel-MC, Stufe 4 = sechsmal Skalarprodukt oder Winkel in einem Schritt mit der fertigen Formel oder Rechnung im Tipp (Niveau Stufe 1 bis 2 des Schwestertrainers), Stufe 5 und 6 gemischt, darunter drei Aufgaben auf dem Niveau von Stufe 3 (#27 „Länge der Seite \(\overline{AB}\)“ im Parallelogramm, #28 Teilpunkt vom Ursprung aus, #31 vierter Parallelogrammpunkt). In fünf Aufgaben war die Lösung eine gegebene Zahl (#1, #3, #6, #12, #31). Punkte standen in Stufe 1 bis 4 als \(A(1, 3)\), Koordinaten hießen „erste Komponente“. Neuer Aufbau: Stufe 1 ein Schritt in der Ebene; Stufe 2 zwei Schritte im Raum und Kollinearität erkennen; Stufe 3 Länge, Abstand, Einheitsvektor, Kollinearität mit Begründung, Seitenlängen; Stufe 4 Umkehraufgaben und Modelle; Stufe 5 zwei Verfahren, Bedingungen, Fehlersuche; Stufe 6 Aussagen prüfen, Fallunterscheidungen, Begründungen. Alle 36 Aufgaben sind neu gesetzt (einheitliche Schreibweise); die Spalte „Änderung“ nennt, was aus dem Altbestand stammt.

| id | Stufe | Kriterium laut Rubrik | Befund | Änderung |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | Lösung 5 = gegebene Zahl | Zahlen neu (\(3+4\)); Frage nach der \(x_1\)-Koordinate |
| 2 | 1 | ein Schritt | zweite Addition, sinngleich mit #1 | jetzt Subtraktion mit negativem Ergebnis (alt #3) |
| 3 | 1 | ein Schritt | Lösung 3 = gegebene Zahl | neu: Punkt um einen Vektor verschieben (K3, geometrische Deutung), MC |
| 4 | 1 | ein Schritt | dritte Addition als MC | jetzt Gegenvektor (alt #5) |
| 5 | 1 | ein Schritt | (alt #5 steht als #4) | Verbindungsvektor in der Ebene (alt #6), Zahlen neu |
| 6 | 1 | ein Schritt | Lösung 3 = gegebene Zahl | neu: Vektor mal Zahl in der Ebene |
| 7 | 2 | Standardverfahren, zwei Schritte | \(3\vec a\): ein Schritt | \(2\vec a - \vec b\) (alt #9), gefragt die Koordinate mit doppeltem Minus |
| 8 | 2 | zwei Schritte | Addition im Raum: ein Schritt | \(\overrightarrow{AB} + \overrightarrow{AC}\) aus drei Punkten (nach dem Prüfdurchgang; die erste Fassung „\(\overrightarrow{AB}\) im Raum“ war #5 in 3D) |
| 9 | 2 | zwei Schritte | (alt #9 steht als #7) | Mittelpunkt (alt #12); Zahlen so, dass \(x_2\) und \(x_3\) von \(M\) verschieden sind (Prüfer) |
| 10 | 2 | zwei Schritte | \(-2 \cdot \vec a\) als MC: ein Schritt | Gegenvektor von \(2 \cdot \vec a\) (Prüfer); Optionen unverändert |
| 11 | 2 | zwei Schritte | (alt #11 steht in #8) | neu: Welcher Vektor ist kollinear? (K4) |
| 12 | 2 | zwei Schritte | Lösung 2 = gegebene Zahl (jetzt #9) | neu: von \(A\) über zwei Vektoren zu \(C\) (Vektorzug; nach dem Prüfdurchgang zwei statt ein Vektor) |
| 13 | 3 | Zwischenergebnis | Betrag \((3;4)\) | Betrag im Raum, \((2;-6;3)\) |
| 14 | 3 | Zwischenergebnis | sinngleich mit #13, #15 | Abstand zweier Punkte (alt #16), jetzt mit drei verschiedenen Koordinaten |
| 15 | 3 | Zwischenergebnis | sinngleich mit #14 | Einheitsvektor (alt #18), negative Koordinate; Tipp ohne die Rechnung |
| 16 | 3 | Zwischenergebnis | (alt #16 steht als #14) | neu: kollinear mit Faktor \(-1{,}5\), Begründung wählen (K4) |
| 17 | 3 | keine Formel im Text | Formel des Einheitsvektors als MC, Distraktor „\(\vec a / \vec a\)“ sinnlos | neu: Welche Seiten des Dreiecks sind gleich lang? |
| 18 | 3 | Zwischenergebnis | (alt #18 steht als #15) | neu: \(|\vec a + \vec b|\); der Fehlweg \(|\vec a| + |\vec b|\) fällt |
| 19 | 4 | Umkehraufgabe | Skalarprodukt in einem Schritt, Formel im Tipp | neu: \(B\) aus \(A\) und Mittelpunkt |
| 20 | 4 | Modell aufstellen | wie #19 | vierter Punkt des Parallelogramms (alt #31, dort Stufe 6); Zahlen so, dass \(A + C\) und die anderen Reihenfolgen fallen |
| 21 | 4 | Umkehraufgabe | Orthogonalitätskriterium als MC (jetzt sp #5) | neu: Parameter \(a\) für Kollinearität |
| 22 | 4 | Modell aus Text | Winkel zwischen \((1;0;0)\) und \((0;1;0)\) | neu: Quader in Koordinaten, Strecke von \(A\) zur Mitte der Kante \(\overline{GH}\) (K2) |
| 23 | 4 | Umkehraufgabe | Winkel 45°, Rechnung im Tipp | neu: \(t\) aus der Länge 9 (nach dem Prüfdurchgang andere Zahlen: das Tripel 2-3-6 trug vier Aufgaben) |
| 24 | 4 | Modell aus Text | Winkel 60° | Teilpunkt (alt #28), jetzt nicht vom Ursprung aus und in Worten („dreimal so lang“) |
| 25 | 5 | zwei Verfahren | Orthogonalität mit \(t\) (Schwestertrainer) | aus alt #26: 15 Längeneinheiten in Richtung \(\vec v\) von einem Punkt aus |
| 26 | 5 | Bedingungen verbinden | (alt #26 steht als #25) | neu: Eckpunkt aus den drei Seitenmitten eines Dreiecks |
| 27 | 5 | Fehler finden | Seitenlänge im Parallelogramm: Niveau Stufe 3 | neu: Kollinearität nur an zwei Koordinaten geprüft – beurteilen |
| 28 | 5 | zwei Verfahren | Teilpunkt (jetzt #24) | neu: Abstand des Diagonalenschnittpunkts von \(A\) im Parallelogramm; Tipp fragt nach der Eigenschaft, statt sie zu nennen (Prüfer) |
| 29 | 5 | Modell aufstellen | Winkelbedingung mit \(t\) (Schwestertrainer) | neu: \(\overrightarrow{MN}\) im Quader durch die Kantenvektoren ausdrücken (K3); stand zuerst auf Stufe 6, nach dem Prüfdurchgang hierher |
| 30 | 5 | zwei Bedingungen | MC „Schritt 1/Schritt 2“ zum Skalarprodukt, Lösungsweg mit Kreuzprodukt | neu: Vektor als \(r \cdot \vec u + s \cdot \vec v\) schreiben (zwei Gleichungen) |
| 31 | 6 | Aussage begründet prüfen | vierter Parallelogrammpunkt (jetzt #20) | neu: „\(|\vec a + \vec b| = |\vec a| + |\vec b|\)“ beurteilen; Lösungsweg nennt auch den Fall entgegengesetzter Richtung (Prüfer) |
| 32 | 6 | Aussage begründet prüfen | „\(\overrightarrow{AB} + \overrightarrow{BC} + \overrightarrow{CA}\)“: Wissensfrage | neu: „Parallelogramm, denn \(\overline{AB}\) und \(\overline{DC}\) sind parallel“ beurteilen (Trapez). Optionen als 2×2-Raster; Tipp nach dem Nachtrag ohne die Unterscheidung „kollinear – gleich“ |
| 33 | 6 | Fallunterscheidung | Innenwinkel (Schwestertrainer) | neu: zwei Punkte der \(x_3\)-Achse mit Abstand 7 von \(A\) – wie weit auseinander? |
| 34 | 6 | Fallunterscheidung | Orthogonalität mit \(t\): dieselbe Aufgabe wie sp #23 | neu: zwei Werte von \(a\), für die Vektoren kollinear sind (quadratische Bedingung) |
| 35 | 6 | Begründung (Abiturformat) | Dreiecksfläche mit Kreuzprodukt | neu: Warum bilden die Seitenmitten jedes (auch räumlichen) Vierecks ein Parallelogramm? Vier Gleichungspaare, drei mit je einem falschen Schritt |
| 36 | 6 | Fallunterscheidung | Winkel Raumdiagonale–Grundfläche mit Tangens (Klasse 10, und Winkel Gerade–Ebene ist eA) | neu: drei Punkte zum Parallelogramm ergänzen, Reihenfolge offen – größte \(x_2\)-Koordinate von \(D\) (der Standardfall liefert sie nicht) |

Nachrechnen (`rechne_vg.py`): 36 Aufgaben, 154 Fehlwege, 0 Fehler. Beim Schreiben gefunden und geändert: #20 (mit \(B_2 = 0\) lieferte der falsche Ansatz \(A + C\) die Lösung), #36 (mit \(A_2 = 0\) war die Summe der \(x_2\)-Koordinaten die Lösung), #22 (Kante plus Höhe traf die Lösung 7). Nicht rechnerisch, sondern am Begriff entschieden: #27 Option „Mit einem negativen Faktor sind Vektoren nie kollinear“ (falsche Allgemeinaussage). Stehen gelassen: Paarsummen ohne Rechenweg (z. B. #22: \(11 = 2 + 9\), #26: \(9 = 4 + 5\), #30: \(5 = 2 + 3\)); #28: die Lösung 3 ist zugleich die \(x_1\)-Koordinate des Zwischenpunkts \(M\) (gefragt ist ein Abstand).
Zweiter Prüfdurchgang (alle 36): 1 Fehler (#2: im Lösungsweg stand \(9 - 2 = 5\); der Lösungswert stimmte), 4 Mängel (#9: \(x_2\) und \(x_3\) des Mittelpunkts gleich; #8, #12: ein Schritt, sinngleich mit Stufe 1; #32: Vektorzug im Quader verfehlt Stufe 6), 5 Hinweise (#10, #23, #28, #31, #26/#36). Alles eingearbeitet wie in der Tabelle; statt des vorgeschlagenen bloßen Stufentauschs #29/#32 ist die Trapez-Aufgabe für Stufe 6 als Beurteilung einer Behauptung neu gefasst.
Nachtrags-Prüfer (#2, #8, #9, #10, #12, #23, #28, #29, #32): kein Fehler, kein Mangel; ein Hinweis zum Tipp von #32 – übernommen. Danach nichts mehr geändert.
Sichtprüfung: alle 36 mit Tipp und Lösungsweg am Bildbogen (700 px), die zwölf geänderten in der Endfassung noch einmal, sechs mit den längsten Formeln bei 360 px (#7, #12, #20, #21, #26, #34): keine zerbrochene Formel, kein Überlauf; lange Vektorketten brechen hinter dem Rechenzeichen um. Nach dem ersten Bogen geändert: Brüche im Fließtext (#9, #19) als Division geschrieben, weil die Zähler unlesbar klein waren.
