# Kriterien Qualifikationsphase Kern (Spalte 12), Block B: Analytische Geometrie — Level-Durchgang 2026-10

Stand: alle drei Trainer des Blocks fertig (Commits f34e365, f6d150e und der Commit zu 12-skalarprodukt). Die Titel sind in diesem Block nicht geändert (Parallelbetrieb); Empfehlungen stehen je Trainer unter „Titel“.

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

## 12-geraden-raum — Geraden im Raum (empfohlen: Geraden & Ebenen in Parameterform)
KC: QP gA „Raumanschauung und Koordinatisierung“ (G8): K5 (Z. 1927 „Geraden- und Ebenengleichungen in Parameterform verwenden“), K10 (Z. 1933 „Lagebeziehungen von Geraden untersuchen und Schnittpunkte bestimmen“); als Werkzeug K4 und K6.
Gelesen: alle 36 Aufgaben. Urteil Lehrplan: Geraden passten, Ebenen fehlten ganz. Aus dem Abgleich: #27 (Abstand paralleler Geraden) und #35 (nächster Punkt einer Geraden zu \(P\), Lotfußpunkt) sind eA (Z. 2158) – **beide ersetzt** durch Ebenen-Aufgaben. Eigene Funde: #20, #28, #33 rechneten mit dem Skalarprodukt (Orthogonalität, Schnittwinkel) – nach dem Zuschnitt in `12-skalarprodukt` (dort #19); #36 (Steigungswinkel einer Seilbahn „gegenüber der Horizontalen“) ist ein Winkel Gerade–Ebene mit dem Tangens aus Klasse 10; #5 hatte den Distraktor „Normalenvektor“ (eA-Wort); #17 „R³“; #9 ließ den Richtungsvektor „durch den GGT teilen“.
Titel: bleibt in diesem Block unverändert („Geraden im Raum“ an allen drei Stellen). Empfehlung laut Plan und nach dem Inhalt: „Geraden & Ebenen in Parameterform“ – 14 der 36 Aufgaben sind Ebenen-Aufgaben, und „im Raum“ grenzt nicht gegen die eA-Trainer ab, „in Parameterform“ schon.

Befund zum Aufbau: Stufe 1 bis 3 trugen (Punkt zum Parameter, Punktprobe, Gerade aus zwei Punkten, Lage zweier Geraden), aber die Tipps der Stufen 1 bis 3 enthielten die fertigen Gleichungen samt Rechnung. Stufe 4 war Stufe 2/3 noch einmal: #19 Parameter eines Punktes, #21 „echt parallel“ wie #14, #22 Spurpunkt wie #11, #24 Schnittparameter wie #16 mit leichteren Zahlen. Stufe 5 und 6: drei Aufgaben außerhalb des Zuschnitts (s. o.), zwei eA, zwei Begriffs-MC auf dem Niveau von Stufe 2 (#26 „nicht parallel und kein gemeinsamer Punkt – welche Lage?“, #34 „linear abhängige Richtungsvektoren“), zwei Bewegungsaufgaben, deren Rechnung eine Zeile war (#29: \(2t = 8\); #31: \((t-6)^2 + 1\) minimal), und #32 mit der Lösung als gegebener Zahl. Neuer Aufbau: Stufe 1 ein Schritt an Gerade und Ebene; Stufe 2 Punktprobe, Gerade aus zwei und Ebene aus drei Punkten; Stufe 3 Lage zweier Geraden, Schnittpunkt, Punktprobe in der Ebene mit Gleichungssystem, Spurpunkt; Stufe 4 Umkehraufgaben und Modelle; Stufe 5 zwei Verfahren, Bedingungen, Fehlersuche; Stufe 6 Fallunterscheidung, Aussagen und Zusammenhänge. Alle 36 Aufgaben sind neu gesetzt.

Ebenen in Parameterform (K5), 14 Aufgaben: #4, #6 (Stufe 1), #10, #11 (2), #16, #17 (3), #21, #22, #24 (4), #27, #28, #29 (5), #32, #35 (6). Inhalte: Punkt zu Parameterwerten, Begriffe, Ebene aus drei Punkten, Punktprobe, Schnittpunkt mit einer Koordinatenachse, Gerade in der Ebene bei festem Parameter, drei Punkte auf einer Geraden, Parameterbereich (Parallelogramm, Dreieck), Ebene aus zwei parallelen Geraden, dieselbe Ebene in anderer Darstellung.

| id | Stufe | Kriterium laut Rubrik | Befund | Änderung |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | Punktprobe mit drei Gleichungen im Tipp (jetzt #7) | Punkt zum Parameterwert (alt #4) |
| 2 | 1 | ein Schritt | zweite Punktprobe | Begriff Richtungsvektor (alt #5), Distraktoren ohne „Normalenvektor“ |
| 3 | 1 | ein Schritt | trägt | Zahlen neu (Richtungskoordinate 2 statt 1) |
| 4 | 1 | ein Schritt | (alt #4 steht als #1) | neu: Punkt der **Ebene** zu \(r = 2\), \(s = 3\) (nach dem Prüfdurchgang verschiedene Werte, damit Vertauschen auffällt) |
| 5 | 1 | ein Schritt | (alt #5 steht als #2) | neu: Welcher Punkt liegt auf \(g\)? (Stützpunkt, \(t = 0\)); Optionen ohne Punktnamen, weil die Engine selbst A) bis D) vergibt |
| 6 | 1 | ein Schritt | dritte Einsetzaufgabe | neu: Begriff Spannvektoren |
| 7 | 2 | Standardverfahren | Richtungsvektor aus zwei Punkten: Stoff des Vektoren-Trainers | Punktprobe (alt #1), Tipp ohne die Gleichungen |
| 8 | 2 | Standardverfahren | trägt | Schreibweise \(A(2\mid-1\mid3)\) |
| 9 | 2 | Standardverfahren | „durch den GGT teilen“ | Punkt mit \(x_2 = 0\) (alt #10), gefragt die \(x_3\)-Koordinate |
| 10 | 2 | Standardverfahren | (alt #10 steht als #9) | neu: **Ebene aus drei Punkten** auswählen; Distraktoren: Ortsvektoren als Spannvektoren, Stütz- und Spannvektor vertauscht, Summen |
| 11 | 2 | Standardverfahren | Spurpunkt (jetzt #18) | neu: Punkt der Ebene mit gegebener \(x_1\)- und \(x_2\)-Koordinate, gesucht \(x_3\) (entkoppeltes System; nach dem Prüfdurchgang ohne den Buchstaben \(p\)) |
| 12 | 2 | Standardverfahren | „gleicher Stützpunkt, nicht kollinear“ | aus alt #34 (dort Stufe 6): kollineare Richtungsvektoren – parallel oder identisch; „linear abhängig“ ersetzt durch „kollinear“ (KC-Wort); Zahlen nach dem Prüfdurchgang anders als im Vektoren-Trainer #11 |
| 13 | 3 | Zwischenergebnis | identisch | echt parallel (alt #14), Punktprobe mit \(t = 1{,}5\) |
| 14 | 3 | Zwischenergebnis | (alt #14 steht als #13) | windschief (alt #15), Zahlen ohne Nullen |
| 15 | 3 | Zwischenergebnis | (alt #15 steht als #14) | Schnittpunkt (alt #16), gefragt eine Koordinate statt des Parameters; \(x_1 \neq x_3\) |
| 16 | 3 | Zwischenergebnis | (alt #16 steht als #15) | neu: **Punktprobe in der Ebene** (MC mit Parameterwerten) |
| 17 | 3 | Zwischenergebnis | „vier Lagen im R³“ aufzählen | neu: fehlende Koordinate eines Punktes der Ebene, gekoppeltes System |
| 18 | 3 | Zwischenergebnis | „Wie erkennt man parallele Geraden?“ (jetzt #12) | Spurpunkt (alt #11) mit Gerade aus zwei Punkten, \(t = 1{,}5\); „einer ihrer Spurpunkte“ (Prüfer) |
| 19 | 4 | Umkehraufgabe | Parameter eines Punktes (Stufe 2) | neu: \(b\) in \(B(3\mid b\mid2)\) so, dass die Gerade \(AB\) durch \(P\) geht. Die erste Fassung (\(P(7\mid a\mid5)\) auf der Geraden durch \(A\), \(B\)) war nach dem Prüfdurchgang #18 noch einmal |
| 20 | 4 | Modell aus Text | Orthogonalität mit \(a\) (Schwestertrainer) | neu: Drohne, Parameter als Zeit – wann ist sie 29 m hoch? Die erste Fassung fragte nach der Geschwindigkeit (nur Abstand zweier Punkte, Prüfer) |
| 21 | 4 | Verfahren wählen | „echt parallel“ wie #14 | neu: Schnittpunkt der **Ebene** mit der \(x_1\)-Achse („Spurpunkte“ des Plans über die Parameterform) |
| 22 | 4 | Umkehraufgabe | Spurpunkt wie #11 | neu: Für welchen festen Wert von \(s\) wird aus der Ebenengleichung die Gerade \(g\)? Die erste Fassung („setze \(s = 2\), welche Gerade?“) sagte den Rechenweg an (Prüfer) |
| 23 | 4 | Verfahren wählen | Boot in der Ebene, Länge des Richtungsvektors | neu: Welche Gleichung beschreibt **dieselbe Gerade**? (Richtung und Punkt prüfen); Zahlen nach dem Prüfdurchgang anders als in #13 |
| 24 | 4 | Modell aufstellen | Schnittparameter wie #16 | neu: Ebene durch drei Punkte, \(d\) in \(D(1\mid3\mid d)\); Zahlen so, dass der vierte Parallelogrammpunkt nicht dieselbe Koordinate hat |
| 25 | 5 | Parameter aus Bedingung | trägt der Form nach (alt: sehr einfache Zahlen) | \(a\) im Stützvektor so, dass sich die Geraden schneiden; neue Zahlen ohne Nullen |
| 26 | 5 | zwei Verfahren | Begriffs-MC (Stufe 2) | aus alt #29: Bahnen kreuzen sich, aber zu verschiedenen Zeiten – wie viele Sekunden liegen dazwischen? |
| 27 | 5 | Fehler finden | Abstand paralleler Geraden (**eA**) | neu: „Ebene“ durch drei Punkte, die auf einer Geraden liegen – beurteilen (Spannvektoren kollinear) |
| 28 | 5 | zwei Verfahren | Schnittwinkel (Schwestertrainer) | neu: Welcher Punkt liegt im Inneren des Parallelogramms? (Punktprobe und Parameterbereich); \(P\) nach dem Prüfdurchgang nicht mehr der Mittelpunkt |
| 29 | 5 | zwei Verfahren | (alt #29 steht als #26) | neu: Ebene durch zwei **parallele** Geraden, fehlende Koordinate eines Punktes. Die erste Fassung (zwei sich schneidende Geraden) war die vierte Punktprobe derselben Form (Prüfer) |
| 30 | 5 | zwei Verfahren | Punkt mit Abstand 6 vom Stützpunkt | neu: Abstand zweier Spurpunkte einer Geraden. (Die alte Idee steht im Vektoren-Trainer als #25.) |
| 31 | 6 | Fallunterscheidung | kleinster Abstand, Rechnung eine Zeile (jetzt #33) | neu: \(g\) und \(h_a\) – echt parallel für \(a = 2\), schneidend für \(a = 4\), sonst windschief; Optionen als Raster |
| 32 | 6 | Aussage begründet prüfen | Lösung 5 = gegebene Zahl (Idee jetzt #19) | neu: Punkt in der Ebene des Dreiecks, aber außerhalb (\(r + s\) größer als 1) |
| 33 | 6 | Zusammenhang (Abiturformat) | Schnittwinkel (Schwestertrainer) | aus alt #31: kleinster Abstand zweier Schiffe als Minimum einer quadratischen Funktion, jetzt mit zwei bewegten Koordinaten; Seemeilen und Stunden statt Kilometer und Minuten (Prüfer: 216 km/h) |
| 34 | 6 | Zusammenhang (Abiturformat) | Begriffs-MC (jetzt #12) | neu: Punkt der Geraden, der von \(A\) und \(B\) gleich weit entfernt ist |
| 35 | 6 | Aussage begründet prüfen | Lotfußpunkt (**eA**) | neu: Welche Gleichung beschreibt **dieselbe Ebene**? (Stützpunkt in der Ebene, Spannvektoren kombinierbar) |
| 36 | 6 | Zusammenhang (Abiturformat) | Steigungswinkel mit Tangens | neu: Diagonalenschnittpunkt eines Vierecks, Parameter als Bruchteil der Diagonale; \(D\) nach dem Prüfdurchgang so, dass die Parameter der beiden Diagonalen verschieden sind |

Nachrechnen (`rechne_gr.py`): 36 Aufgaben, 128 Fehlwege, 0 Fehler. Beim Schreiben gefunden und geändert: #15 (\(x_1 = x_3\) im Schnittpunkt), #24 (der vierte Parallelogrammpunkt hatte dieselbe \(x_3\)-Koordinate wie die Lösung). Nicht rechnerisch, sondern am Begriff entschieden: #2, #6 (Namen der Vektoren); #12 Option „mit Sicherheit identisch“; #27 Optionen „muss \(\overrightarrow{BC}\) sein“ und „Ortsvektor von \(B\)“ (beides behebt nichts, nachgerechnet: auch \(\overrightarrow{BC}\) ist kollinear). Stehen gelassen: #20 hat einen zweiten richtigen Weg (ab \(B\): \((29 - 13) : 4 + 3\)); Paarsummen ohne Rechenweg wie in #1 (\(9 = 4 + 5\)).
Zweiter Prüfdurchgang (alle 36, mit `12-vektoren-grundlagen` als Vergleich): kein Fehler, 4 Mängel (#19, #22, #29 Stufe; #36 Fehlweg trifft), 9 Hinweise (#4, #12, #18, #20, #23, #26, #28, #33, #35). Alle eingearbeitet wie in der Tabelle; zu #35 nur der Wortlaut („andere Ebene“ statt „parallele Ebene“), die Aufgabe selbst bleibt (siehe unten). Die Zahlen der Vorschläge hat der Prüfer gerechnet, `rechne_gr.py` hat sie unabhängig bestätigt; ein Nachtrags-Prüfer ist deshalb nicht gelaufen. Eigene neue Zahlen nach dem Prüfdurchgang: nur #12.
Sichtprüfung: alle 36 am Bildbogen, die 14 geänderten in der Endfassung, sechs bei 360 px. Im Bild gefunden: \(P(5\mid-1\mid p)\) erschien als roter Befehl „\midp“ (fehlendes Leerzeichen im Baustein; `katex_check` meldet das nicht) – behoben; „\(2{,}5 \neq 2\) – \(T\)“ las sich als Minus – umgestellt. Ebenengleichungen stehen eine Stufe kleiner (`\small`): im Lösungsweg und ab etwa 400 px auch in der Frage einzeilig; bei 360 und 390 px bricht die Engine in der Frage hinter dem letzten Malpunkt um, der dritte Vektor steht dann als Ganzes in der Folgezeile (kein Überlauf, kein einzelnes Zeichen). Geradengleichungen bleiben einzeilig.

Offen für den Autor: #35 („dieselbe Ebene“) und #21 (Achsenschnittpunkt) berühren der Sache nach Lagebeziehungen mit Ebenen, benutzen aber nur Punktprobe und Spannvektoren; #22 und #29 lassen eine Gerade in einer Ebene liegen. Wenn der gA-Kern enger gelesen werden soll, sind das die vier Aufgaben, die zu ersetzen wären.

## 12-skalarprodukt — Skalarprodukt & Orthogonalität
KC: QP gA „Raumanschauung und Koordinatisierung“ (G8): K7 (Z. 1930 „Skalarprodukt geometrisch als Ergebnis einer Projektion deuten und verwenden“), K8 (Z. 1931 „Orthogonalität zweier Vektoren überprüfen“), K9 (Z. 1932 „Winkelgrößen zwischen Strecken und Geraden bestimmen“); K2 in den Figuren und Körpern.
Gelesen: alle 36 Aufgaben. Urteil Lehrplan: passt im Stoff (Abgleich: „passt“), mit einer Lücke und zwei Grenzfällen. Eigene Funde: Die **Projektion (K7) kam nicht vor** – kein Wort, keine Aufgabe; #22 fragte nach dem Winkel einer Rampe „mit der \(xy\)-Ebene“ (Winkel Gerade–Ebene ist eA, und die Koordinaten hießen \(x, y, z\)); #25 nannte den gesuchten Vektor \(\vec n\) (Normalenvektor-Technik des eA-Trainers `12-ebenen`); #16 hatte den Distraktor „Ja, denn sie sind gleich lang“ – die Vektoren \((3;4)\) und \((4;-3)\) **sind** gleich lang und orthogonal, also richtige Antwort mit falscher Begründung; in #28, #35 hießen die Koordinaten \(x\) und \(y\).
Titel: bleibt in diesem Block unverändert (heute `<title>` und Kopfzeile „Skalarprodukt & Winkel“, Index „Skalarprodukt & Orthogonalität“). Empfehlung an allen drei Stellen: „Skalarprodukt: Orthogonalität & Winkel“ – beide Anwendungen stehen im KC nebeneinander und im Trainer zu gleichen Teilen.

Befund zum Aufbau: Stufe 1 = fünfmal dieselbe Rechnung in der Ebene (#1, #2, #3, #5, #6 sinngleich), Stufe 2 = sechsmal dieselbe Rechnung im Raum, Stufe 3 = dreimal „für welches \(x\) orthogonal“ (#13–#15 sinngleich) und zwei Winkel; Stufe 4 = ein Winkel wie #18 (#19), zweimal Innenwinkel bei \(A\) (#20, #24 sinngleich), dazu drei tragende Aufgaben. Stufe 5 und 6 waren der beste Teil des Trainers und sind größtenteils geblieben; #36 war #28 im Raum (orthogonal und Länge gegeben), #34 lag auf dem Niveau von Stufe 4/5. Winkel hatten die Toleranz 0,05 – wer den Kosinus auf drei Stellen rundete, fiel durch. Neuer Aufbau: Stufe 1 Skalarprodukt in Ebene und Raum, Kriterium, \(\vec a \cdot \vec a\); Stufe 2 Orthogonalität prüfen, Verbindungsvektoren, Klammer, Winkel aus gegebenen Größen, Vorzeichen deuten; Stufe 3 Winkel zweier Vektoren und im Dreieck, Parameter, Projektion; Stufe 4 Schnittwinkel von Geraden, Winkel an Strecken und Körpern, Vierecke, Projektion einer Strecke; Stufe 5 zwei Bedingungen, Fehlersuche, Würfel, Zerlegung; Stufe 6 Aussagen prüfen und Begründungen. Alle 36 Aufgaben sind neu gesetzt (einheitliche Schreibweise); die Spalte „Änderung“ nennt, was aus dem Altbestand stammt.

| id | Stufe | Kriterium laut Rubrik | Befund | Änderung |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | trägt | Wortlaut („Skalarprodukt ist eine Zahl“) |
| 2 | 1 | ein Schritt | sinngleich mit #1, #3, #5, #6 | eine zweite Rechnung in der Ebene, jetzt mit negativem Summanden |
| 3 | 1 | ein Schritt | (alt #3 steht in #2) | MC mit dem Wert 0 (alt #4), Lösungsweg mit der Lage der Vektoren |
| 4 | 1 | ein Schritt | (alt #4 steht als #3) | Skalarprodukt im Raum (alt #7) |
| 5 | 1 | ein Schritt | sinngleich mit #1 | Kriterium für Orthogonalität als MC (stand im Vektoren-Trainer als #21 auf Stufe 4) |
| 6 | 1 | ein Schritt | sinngleich mit #1 | neu: \(\vec a \cdot \vec a\) als Quadrat der Länge |
| 7 | 2 | Standardverfahren, zwei Schritte | (alt #7 steht als #4) | \((3 \cdot \vec a) \cdot \vec b\) mit zwei negativen Produkten (Zahlen aus alt #9). Die erste Fassung – nur \(\vec a \cdot \vec b\) – war nach dem Prüfdurchgang #4 mit anderen Zahlen |
| 8 | 2 | Standardverfahren | sinngleich mit #7 | Orthogonalität prüfen (alt #16), im Raum; alle Distraktoren nennen ein falsches Skalarprodukt (alt: „Ja, denn sie sind gleich lang“ war eine wahre Aussage) |
| 9 | 2 | Standardverfahren, kein Parameter | sinngleich mit #7 | neu: \(\overrightarrow{AB} \cdot \overrightarrow{AC}\) aus drei Punkten (Vorstufe zum Innenwinkel) |
| 10 | 2 | Standardverfahren | sinngleich mit #7 | neu: \(\vec a \cdot (\vec b + \vec c)\) |
| 11 | 2 | Standardverfahren | MC, sinngleich mit #7 | neu: Winkel aus gegebenem Skalarprodukt und gegebenen Längen (60°) |
| 12 | 2 | Standardverfahren | sinngleich mit #7 | neu: negatives Skalarprodukt – was folgt für den Winkel? |
| 13 | 3 | Zwischenergebnis | Parameter für Orthogonalität (dreimal) | Winkel zweier Vektoren im Raum (alt #18), Zahlen \(\tfrac{11}{15}\) |
| 14 | 3 | Zwischenergebnis | wie #13 | Innenwinkel im Dreieck (alt #20, dort Stufe 4), Tipp erklärt, welche Vektoren |
| 15 | 3 | Zwischenergebnis | wie #13 | Parameter, der zweimal vorkommt (alt #23, dort Stufe 4), Zahlen neu |
| 16 | 3 | Zwischenergebnis | (alt #16 steht als #8) | neu: **Länge der Projektion** eines Vektors auf einen anderen (K7) |
| 17 | 3 | keine Formel im Text | Winkel in der Ebene | neu: geometrische Bedeutung von \(\vec a \cdot \vec b\) (K7), Distraktoren Flächeninhalt, Diagonale, „plus“ |
| 18 | 3 | Zwischenergebnis | (alt #18 steht als #13) | neu: An welcher Ecke des Dreiecks liegt der rechte Winkel? |
| 19 | 4 | Verfahren wählen | Winkel wie #18 (Stufe 3) | neu: **Schnittwinkel zweier Geraden** – die Richtungsvektoren schließen einen stumpfen Winkel ein (aus `12-geraden-raum` alt #28, #33) |
| 20 | 4 | Modell aus Text | (alt #20 steht als #14) | Rampe (alt #22): Winkel zwischen der Rampe und der Strecke zum Punkt \(Q'\) senkrecht unter \(Q\) statt „mit der \(xy\)-Ebene“; \(Q'\) ist nur beschrieben, die Koordinaten findet man selbst (Prüfer); \(P\) nicht im Ursprung |
| 21 | 4 | Verfahren wählen | trägt | Schreibweise; Tipp nennt die drei Fragen, nicht die Rechnungen |
| 22 | 4 | Umkehraufgabe | (alt #22 steht als #20) | rechter Winkel bei \(B\) mit \(t\) (alt #29, dort Stufe 5), ganzzahlige Lösung |
| 23 | 4 | Modell aufstellen | (alt #23 steht als #15) | neu: **Projektion einer Strecke** auf eine Gerade (K7); Tipp nach dem Prüfdurchgang ohne die Beziehung „Länge der Projektion mal Länge“ |
| 24 | 4 | Modell aufstellen | sinngleich mit #20 | aus alt #34 (dort Stufe 6): Pyramide in Koordinaten, Winkel an der Spitze – jetzt zwischen den **gegenüberliegenden** Seitenkanten \(\overline{AS}\) und \(\overline{CS}\); die Vektoren müssen in \(S\) beginnen. Die erste Fassung (Grundkante gegen Seitenkante bei \(A\)) war mit #20 sinngleich (Prüfer) |
| 25 | 5 | zwei Bedingungen | trägt | Vektor heißt \(\vec w\) statt \(\vec n\), Unbekannte \(a\), \(b\) statt \(x\), \(y\) (Prüfer: „\(x\)“ liest sich wie eine Koordinate), Zahlen neu (Lösung war gegebene Zahl) |
| 26 | 5 | Fehler finden | Optionen „Schritt 1 … 4“; der falsche Kosinus \(\tfrac{4}{3}\) verriet sich selbst | Zahlen so, dass der Fehlwert \(\tfrac{2}{3}\) ein möglicher Kosinus ist; Optionen nennen den Fehler; Tipp nennt nach dem Prüfdurchgang keine Zeile mehr |
| 27 | 5 | zwei Verfahren | trägt | Wortlaut („Diagonalenvektoren“, Reihenfolge der Eckpunkte) |
| 28 | 5 | zwei Bedingungen | trägt | Koordinaten \(x_1, x_2\) |
| 29 | 5 | Modell aufstellen | (alt #29 steht als #22) | Würfel (alt #30), Lösungsweg begründet die freie Kantenlänge |
| 30 | 5 | zwei Verfahren | (alt #30 steht als #29) | neu: **Zerlegung** eines Vektors in einen Anteil längs \(\vec b\) und einen senkrecht dazu (K7); der Tipp gibt nach dem Prüfdurchgang den Ansatz nicht mehr als Gleichungen |
| 31 | 6 | Aussage begründet prüfen | „\(\vec a \cdot \vec b = 0\), also ein Nullvektor“ – Begriffsfrage (Stufe 3) | neu: „aus \(\vec a \cdot \vec b = \vec a \cdot \vec c\) folgt \(\vec b = \vec c\)“ beurteilen |
| 32 | 6 | Fallunterscheidung | MC „stumpf für \(t < 1\)“ | neu: Für wie viele ganze Zahlen \(t\) ist der Winkel stumpf? (quadratischer Term, Randwerte sind rechte Winkel). Die erste Fassung fragte nach der Schwelle \(k\) – das war „Skalarprodukt gleich null“ wie #15 (Prüfer) |
| 33 | 6 | Aussage begründet prüfen | trägt | Optionen im Wortlaut angeglichen |
| 34 | 6 | Zusammenhang (Abiturformat) | Pyramide, Winkel an der Spitze (jetzt #24) | neu: Flächeninhalt eines Dreiecks im Raum – dass es rechtwinklig ist, steht nicht mehr in der Frage (Prüfer), nur der Tipp lenkt darauf |
| 35 | 6 | Zusammenhang (Abiturformat) | Quadrat aus einer Seite: \(\overrightarrow{AB} = (3;4)\), senkrecht und gleich lang – dieselbe Rechnung wie #28 | neu: Quadrat aus der **Diagonale** \(\overline{AC}\) (Diagonalen halbieren sich, sind orthogonal und gleich lang) |
| 36 | 6 | Begründung (Abiturformat) | orthogonal und Länge gegeben: #28 im Raum | neu: Welche Rechnung begründet, dass die Diagonalen jeder Raute senkrecht aufeinander stehen? Der erste Distraktor „\(= \vec a \cdot \vec b - \vec b \cdot \vec a = 0\)“ war in der Raute als Gleichungskette wahr (Prüfer); jetzt „\(= 2 \cdot \vec a \cdot \vec b = 0\)“, in der Raute falsch außer im Quadrat. Tipp ohne Hinweis auf \(|\vec a|\), \(|\vec b|\) |

Nachrechnen (`rechne_sp.py`): 36 Aufgaben, 177 Fehlwege, 0 Fehler. Winkel sind über \(\operatorname{atan2}(|\vec a \times \vec b|, \vec a \cdot \vec b)\) gemessen, Projektionen über den Lotfußpunkt als Minimum des Abstands, die Allgemeinaussagen (#5, #12, #17, #31, #36) an Zufallsvektoren. **Winkeltoleranz 0,15** (hinterlegt der Wert auf zwei Dezimalstellen): angenommen wird das richtig gerundete Ergebnis auch bei einem auf drei oder vier Stellen gerundeten Kosinus; abgewiesen werden Ergänzungswinkel, Bogenmaß, Sinus statt Kosinus, addierte Längen, falscher Eckpunkt und Ortsvektoren statt Verbindungsvektoren. Ein nur auf zwei Stellen gerundeter Kosinus fällt bei allen sechs Winkelaufgaben mit Rundung heraus (#13, #14, #20, #24, #27, #29: Abweichung 0,2 bis 0,4 Grad) – das ist zu grob gerundet und soll nicht durchgehen. Nicht rechnerisch, sondern am Begriff entschieden: #12 Option „ein Skalarprodukt ist nie negativ“; #31 Optionen „durch \(\vec a\) teilen“ und „kann gar nicht gelten“. Stehen gelassen: #20 lässt sich auch mit dem Tangens aus Klasse 10 lösen (\(2 : 5\), gleicher Wert); #19 setzt voraus, dass „Schnittwinkel“ den Winkel bis \(90^\circ\) meint – das steht im Tipp, nicht in der Frage (die Unterscheidung ist die Hürde der Aufgabe).
Zweiter Prüfdurchgang (alle 36, mit beiden Schwestertrainern als Vergleich): kein Fehler, 9 Mängel (#7, #20, #24, #32, #35 Stufe oder sinngleich; #23, #26, #30 Tipp verrät; #36 Distraktor in der Raute wahr), 2 Hinweise (#25, #34). Alle eingearbeitet wie in der Tabelle; bei #36 nicht der vorgeschlagene Wortlaut („… das gilt in jedem Parallelogramm“ – der Rechenteil bliebe in der Raute wahr), sondern eine Kette, die in der Raute selbst falsch ist. Vor dem Prüfdurchgang selbst geändert: #9 war „für welches \(a\) orthogonal“ (ein Parameter auf Stufe 2, den die Rubrik dort ausschließt). Die Zahlen der Vorschläge (#7, #24, #32, #35) hat der Prüfer gerechnet, `rechne_sp.py` hat sie unabhängig bestätigt; ein Nachtrags-Prüfer ist deshalb nicht gelaufen. Kein sinngleiches Paar zu `12-vektoren-grundlagen` und `12-geraden-raum` gefunden.
Sichtprüfung: alle 36 am Bildbogen, die 14 geänderten in der Endfassung, sechs bei 360 px (#10, #19, #25, #26, #31, #36): keine zerbrochene Formel, kein Überlauf. Im Bild geändert: Gedankenstriche direkt hinter einer Formel (#19, #31) lasen sich als Minuszeichen und sind Satzenden geworden.
