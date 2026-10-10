# Kriterien Qualifikationsphase (Spalte 12) — Level-Durchgang 2026-10

Je Trainer ein Abschnitt (Format: Plan `2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, „Kriterien-Datei“).
KC = Kerncurriculum Mathematik für die gymnasiale Oberstufe Niedersachsen (`ma_go_kc_2019.txt`), Zeilenangaben dort.

## 12-e-funktion — e-Funktion

Verfahren: **Ersatz** (Task 2, vorgezogen). Alle 36 Aufgaben neu; der frühere Inhalt (f(x) = a·bˣ, KC 9/10, S14)
steht unverändert in `10-exponentialfunktionen.html` (Spalte 10, eigener localStorage-Schlüssel
`spirale-10-exponentialfunktionen`) und wird in der Welle Klasse 10 durchgesehen.

KC: QP gA, Lernbereich „Die e-Funktion“ (G7, Z. 1863–1904); Ableitungsregeln gA „Produktregel und Kettenregel bei
linearer innerer Funktion“ (G4, Z. 889–891). Kern-Inhalte, auf die sich die Tabelle bezieht:

| Kürzel | KC-Zeile | Wortlaut (gekürzt) |
|---|---|---|
| K1 | 1883–1884 | Wachstumsgeschwindigkeit bei exponentiellem Wachstum als proportional zum Bestand beschreiben |
| K2 | 1885–1886 | die Basis e durch (eˣ)′ = eˣ charakterisieren |
| K3 | 1887–1890 | Ableitungsfunktion von eˣ und von aˣ verwenden (Intentionen Z. 1869–1870: beliebige Basen in Terme zur Basis e umformen und ableiten) |
| K4 | 1891–1892 | additive und multiplikative Verknüpfungen mit ganzrationalen Funktionen beschreiben, untersuchen, in Sachproblemen anwenden |
| K5 | 1893–1894 | Verkettung mit linearen Funktionen beschreiben, untersuchen, in Sachproblemen anwenden |
| K6 | 1895 | Produktregel und Kettenregel bei linearer innerer Funktion anwenden |
| K7 | 1896 | Parameterbestimmungen zur Angleichung an Daten durchführen |
| K8 | 1897 | Exponentialgleichungen lösen (Intentionen Z. 1872–1873: ln als Umkehroperation) |
| K9 | 1898 | asymptotisches Verhalten des begrenzten Wachstums beschreiben |

Gelesen: KC-Lernbereich im Wortlaut, Spaltenvergleich gA/eA (Z. 1075–1114). Urteil Lehrplan: passt.
Abweichungen vom Stufenaufbau des Plans (das KC geht vor):

- **Fallunterscheidung nach dem Vorzeichen von k (L6)** bleibt bei f(x) = 2·e^(k·x) (#33). Eine Schar aus Produkten wie
  x·e^(k·x) mit Lage der Extremstelle in Abhängigkeit von k steht nur in der eA-Spalte (Z. 1091–1096 „Scharen, die durch
  Verknüpfungen und Verkettungen der e-Funktion … entstehen, in Abhängigkeit vom Scharparameter“; Z. 1110–1114).
  #31 und #33 unterscheiden Fälle nach a und k an der Grundfunktion a·e^(kx); das ist die Grenze dessen, was gA trägt
  (offene Frage im Bericht zu Task 2).
- **Kein „Krümmung“/„linksgekrümmt“**: Das Wort kommt im KC nicht vor (nur Monotonie, Extrem- und Wendepunkte,
  Z. 780, 839–840, 1767–1768). #33 beschreibt den Verlauf mit „steiler/flacher“, #32 nutzt die Wendestelle.
- **ln nur als Werkzeug** (Z. 1900 „ln als Funktion“ fakultativ): ln(e), ln(1) als Werte (#3, #4), sonst nur zum Lösen
  von Exponentialgleichungen und zum Umschreiben von aˣ. Kein Graph, keine Ableitung, keine Stammfunktion von ln.
- **Nur lineare innere Funktionen** (G4): e^(kx), e^(2x−4); kein e^(x²).
- **N′ = 0,3·N wird in Worten gestellt** (#22: „Wachstumsgeschwindigkeit ist das 0,3-Fache des Bestands“). Die
  Schreibweise als Differentialgleichung mit Überprüfen von Lösungsfunktionen steht nur in der eA-Spalte (Z. 900–903,
  1115–1117).
- **Ergänzt, weil KC-Kern und im Plan nicht genannt:** K1 Wachstumsgeschwindigkeit proportional zum Bestand
  (#22, #28), K4 additive Verknüpfung (#10, #17, #29, #34), K7 Parameter aus Daten (#28), Satz vom Nullprodukt mit
  e-Faktor (#11), aˣ als e-Potenz schon auf Stufe 3 (#18) als Vorstufe zu #27.
- **K9 (begrenztes Wachstum)** hat den eigenen Trainer `12-wachstum-begrenzt`; hier nur die Annäherung an die x-Achse im
  Lösungsweg von #33.
- **Tangente (L3)**: statt einer reinen Tangentensteigung der y-Achsenabschnitt der Tangente (#14) und die
  Tangentensteigung mit Produkt- und Kettenregel (#15); die reine Kettenregel mit Einsetzen ist Stufe 2 (#8, #12).
- **Zahlen des Plans geändert**, wo sie einen Fehlweg belohnen oder zahlengleich mit Vorarbeiten wären: eˣ = 5 wurde
  2·eˣ = 14 (#9, zwei Schritte); 3·e^(2x) = 12 wurde 3·e^(2x) = 18 (#16: bei e^(2x) = 4 liefert das falsche
  „Halbieren“ 4 : 2 denselben Wert wie √4); „Ableitung von 2ˣ“ ist als Stelle mit vorgegebener Tangentensteigung
  gestellt (#27), weil das bloße Einsetzen in ln(2)·2ˣ Stufe 2 wäre.

Stufenaufbau, wie er geworden ist:

| Stufe | Inhalt |
|---|---|
| 1 | Werte e⁰, e¹, ln(e), ln(1); Ableitung von eˣ und 3·eˣ |
| 2 | Kettenregel bei 6·e^(−0,5x) und e^(2x−4), Summenregel, zweite Ableitung; 2·eˣ = 14; Nullstelle eines Produkts mit e-Faktor |
| 3 | Produktregel (Term auswählen; Tangente mit y-Achsenabschnitt), Produkt- mit Kettenregel als Tangentensteigung; 3·e^(2x) = 18; waagerechte Tangente bei eˣ − 4x; 1,5ˣ als e-Potenz |
| 4 | Verfahren wählen (größte Konzentration), Modell aus Text (k aus der Halbwertszeit; Wachstumsgeschwindigkeit proportional zum Bestand), Umkehraufgaben (k aus f′(0), Stelle zu gegebener Steigung, a aus waagerechter Tangente) |
| 5 | Parameter aus zwei Bedingungen ((ax+b)·eˣ; Wachstum aus zwei Zählungen mit Wachstumsgeschwindigkeit), zwei Verfahren (Tangente an 2ˣ parallel zu einer Geraden; kleinster Funktionswert von e^(2x) − 6x), Fehler finden (Ableitung; Exponentialgleichung) |
| 6 | Aussagen begründet prüfen (a·e^(kx) ohne Extremstelle; eˣ − x ohne Nullstelle), Fallunterscheidung nach dem Vorzeichen von k, hilfsmittelfreies Abiturformat (Wendetangente; Monotonie-Intervall von (x²−3)·eˣ; Berührpunkt einer Tangente mit vorgegebener Nullstelle) |

Herkunft: „MP“ = eigene Vorarbeit im Schwesterprojekt Mathepfade (`11-e-funktion.html` = MP-e,
`11-e-funktion-ableitung.html` = MP-a; dort anderer Lehrplan). Übernommen ist jeweils nur die Aufgaben**form**, Zahlen
und Funktionen sind geändert. „Plan“ = Vorgabe im Stufenaufbau des Plans. „neu“ = ohne Vorlage. „ZP“ = Fassung nach
dem zweiten Prüfdurchgang (s. u.).

| id | Stufe | Kriterium laut Rubrik | KC | Aufgabe (Kurzform) | Typ | Herkunft |
|---|---|---|---|---|---|---|
| 1 | 1 | ein Rechenschritt, Objekt gegeben | K3 | e⁰ | num | Plan; Form MP-e #2 |
| 2 | 1 | ein Rechenschritt, Objekt gegeben | K2 | e¹ auf zwei Dezimalstellen | num | Plan; Form MP-e #5 |
| 3 | 1 | ein Rechenschritt, Objekt gegeben | K8 | ln(e) | num | Plan; Form MP-e #13 |
| 4 | 1 | ein Rechenschritt, Objekt gegeben | K8 | ln(1) | num | Plan; Form MP-e #14 |
| 5 | 1 | ein Rechenschritt, Objekt gegeben | K2 | Ableitung von eˣ auswählen | MC | Plan; Form MP-a #1 |
| 6 | 1 | ein Rechenschritt, Objekt gegeben | K3 | f = 3·eˣ, f′ = a·eˣ, a gesucht | num | Plan |
| 7 | 2 | Standardverfahren, zwei Schritte | K5, K6 | Ableitung von 6·e^(−0,5x) auswählen (Faktor und Vorzeichen) | MC | Plan; Form MP-a #7–9 |
| 8 | 2 | Standardverfahren, zwei Schritte | K6 | f′(2) für e^(2x−4) | num | Plan |
| 9 | 2 | Standardverfahren, zwei Schritte | K8 | 2·eˣ = 14 | num | Plan; Form MP-e #20; ZP |
| 10 | 2 | Standardverfahren, zwei Schritte | K4 | f′(0) für 2·eˣ − 3x | num | neu |
| 11 | 2 | Standardverfahren, zwei Schritte | K4 | Nullstelle von (2x − 6)·e^(−x) | num | neu |
| 12 | 2 | Standardverfahren, zwei Schritte | K6 | f″(0) für e^(3x) | num | neu |
| 13 | 3 | Klassenarbeits-Standard, Zwischenergebnis | K6 | Ableitung von (2x + 1)·eˣ auswählen | MC | Plan; Form MP-a #13, #17 |
| 14 | 3 | Klassenarbeits-Standard, Zwischenergebnis | K4, K6 | y-Achsenabschnitt der Tangente an x·eˣ bei x = 1 | num | Plan (x·eˣ); ZP |
| 15 | 3 | Klassenarbeits-Standard, Zwischenergebnis | K5, K6 | Tangentensteigung von x·e^(0,5x) bei x = 1 | num | Plan |
| 16 | 3 | Klassenarbeits-Standard, Zwischenergebnis | K8 | 3·e^(2x) = 18 | num | Plan; ZP (Zahl) |
| 17 | 3 | Klassenarbeits-Standard, Zwischenergebnis | K4, K8 | waagerechte Tangente von eˣ − 4x | num | neu |
| 18 | 3 | Klassenarbeits-Standard, Zwischenergebnis | K3 | 1,5ˣ = e^(k·x), k gesucht | num | neu |
| 19 | 4 | Verfahren wählen | K4, K6 | c(t) = 4t·e^(−0,5t): Wann ist die Konzentration am größten? | num | Plan |
| 20 | 4 | Modell aus Text aufstellen | K5, K8 | Abbau mit Halbwertszeit 4 h, k in 80·e^(−kt) | num | Plan; Form MP-e #24 |
| 21 | 4 | Umkehraufgabe | K6 | 5·e^(kx) mit f′(0) = −2, k gesucht | num | Plan |
| 22 | 4 | Modell aus Text aufstellen | K1 | Wachstumsgeschwindigkeit = 0,3-Faches des Bestands, N(0) = 50: passende Funktion | MC | neu; ZP (Wortlaut) |
| 23 | 4 | Umkehraufgabe | K6, K8 | Stelle mit Steigung 2 bei e^(0,5x) | num | Form MP-a #28 |
| 24 | 4 | Umkehraufgabe | K6 | (x + a)·eˣ mit waagerechter Tangente bei x = 2 | num | neu |
| 25 | 5 | Parameter aus zwei Bedingungen | K4, K6 | (ax + b)·eˣ: Nullstelle 3, Steigung 4 bei x = 0 | num | Plan; Form MP-a #26 |
| 26 | 5 | Fehler im Rechenweg finden | K6 | Ableitung von x·e^(−2x), innere Ableitung fehlt; Optionen nennen den Schritt, kein Endergebnis | MC | Plan; ZP (Optionen, Tipp) |
| 27 | 5 | zwei Verfahren kombinieren | K3, K8 | Tangente an 2ˣ parallel zu y = 4x − 1: Stelle gesucht | num | Plan (Ableitung von 2ˣ); ZP |
| 28 | 5 | Parameter aus zwei Bedingungen, zwei Verfahren | K1, K7 | 500 → 2000 Bakterien in 3 h: Wachstumsgeschwindigkeit nach 3 h | num | Form MP-e #25, um die Ableitung erweitert |
| 29 | 5 | zwei Verfahren kombinieren | K4, K8 | kleinster Funktionswert von e^(2x) − 6x | num | neu |
| 30 | 5 | Fehler im Rechenweg finden | K8 | 4·e^(2x) = 20 falsch logarithmiert; Optionen nennen den Fehler, kein Endergebnis | MC | neu; ZP (Optionen) |
| 31 | 6 | Aussage begründet prüfen | K5 | „a·e^(kx) hat keine Extremstelle“ | MC | Plan |
| 32 | 6 | Abiturformat (hilfsmittelfrei) | K4, K6 | Wendetangente von x·e^(−x): Schnittstelle mit der x-Achse | num | Plan |
| 33 | 6 | Fallunterscheidung | K5 | Verlauf von 2·e^(kx) für k > 0 und k < 0 | MC | Plan (auf gA begrenzt, s. o.) |
| 34 | 6 | Aussage begründet prüfen | K4 | „eˣ − x hat keine Nullstelle“ | MC | neu |
| 35 | 6 | Abiturformat (hilfsmittelfrei) | K4, K6 | (x² − 3)·eˣ fällt nur in einem Intervall: Anfang des Intervalls | num | neu; ZP |
| 36 | 6 | Abiturformat (hilfsmittelfrei), Umkehraufgabe | K5, K6 | Tangente an e^(2x) schneidet die x-Achse bei 1: Berührstelle gesucht | num | neu; ZP |

### Prüfung

- **Nachrechnen:** Alle 36 Lösungen, die Wahrheitswerte aller MC-Optionen, 99 typische Fehlwege gegen die Toleranz und
  15 im Text genannte Nebenwerte sind mit sympy unabhängig vom Aufgabentext hergeleitet (0 Abweichungen).
- **Zweiter Prüfdurchgang** (frischer Agent, nur die ausgewerteten Aufgaben, Rubrik und KC): kein Rechenfehler;
  4 Mängel und 8 Hinweise, in einer Nachprüfung der geänderten Aufgaben noch 3 Mängel und 4 Hinweise. Umgesetzt:
  #27 war als bloßes Einsetzen zu leicht; #26/#30 ließen sich über das Endergebnis der Optionen lösen, ohne den Fehler
  zu suchen; der Tipp zu #26 zeigte auf den Schritt; #36 (Dreieck unter der Tangente bei x = 0) lag unter Stufe 5 und
  ist jetzt eine Umkehraufgabe; #35 fragt nach dem Anfang des Monotonie-Intervalls, weil die Intervalllänge auch mit
  Vorzeichenfehler 4 ergibt; #16 bekam die rechte Seite 18 (s. o.); #9 hat zwei Schritte; #14 ist keine zweite
  Einsetzaufgabe mehr; #22 und #25 im Wortlaut. Nicht umgesetzt: parameterfreie Fassung von #31 (Plan nennt die
  Aussage ausdrücklich; als offene Frage gemeldet).
- **Fehlweg-Kontrolle:** Bei keiner numerischen Aufgabe führt ein geprüfter Fehlweg (innere Ableitung vergessen,
  u′·v′, Vorzeichen, f statt f′, lg statt ln, Halbieren statt Wurzel, mittlere statt momentane Rate) in die Toleranz.
- **Sichtprüfung:** alle 36 Aufgaben mit Tipp und Lösungsweg am Bildbogen angesehen. Inline-Formeln sind als Gruppe
  gesetzt, damit sie nicht hinter einem Rechen- oder Relationszeichen umbrechen; Satzzeichen hinter einer Formel stehen
  in der Formel, damit sie nicht allein in die nächste Zeile rutschen; lange abgesetzte Formeln sind mehrzeilig, sodass
  bei 360 px Breite nichts aus dem Kasten ragt.
