# Kriterien Klasse 10, Block C (Wachstum) — Level-Durchgang 2026-10

Je Trainer ein Abschnitt (Format: Plan `2026-10-10-lehrplan-nds-und-level-durchgang-plan.md`, „Kriterien-Datei“). Diese Datei ergänzt
`2026-10-10-kl10-kriterien.md` (Blöcke A und B); sie ist eine eigene Datei, weil die Blöcke der Welle 10 gleichzeitig bearbeitet wurden.
KC = Kerncurriculum Mathematik für das Gymnasium, Schuljahrgänge 5–10, Niedersachsen (`ma_gym_si_kc_druck.txt`), Zeilenangaben dort.
Lesart der Stufen für Klasse 9/10: Stufe 4 = Verfahren selbst wählen, Umkehraufgabe, Modell aus Text; Stufe 5 = zwei Verfahren verbinden,
Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung finden; Stufe 6 = Fallunterscheidung, Aussage begründet prüfen.
„Befund“ beschreibt den Stand vor dem Durchgang.

## KC-Befund am Wortlaut

Lernbereich 9/10 „Exponentielle Zusammenhänge“ (S14, SI Z. 2379–2432). Was die drei Trainer trägt:

- **Intentionen** (Z. 2381–2383): „Ausgehend von der Idee des prozentualen positiven bzw. negativen Zuwachses wird exponentielles Wachstum
  iterativ eingeführt und auch explizit beschrieben sowie gegen lineares Wachstum abgegrenzt.“ → `10-wachstum-linear-exponentiell`.
- **Überlagerung und begrenztes Wachstum** (Z. 2384–2393): Die iterativ beschriebene Überlagerung
  \(b(n) = b(n-1) + w \cdot b(n-1) + d\) mit \(w > -1\) bzw. \(b(n) = k \cdot b(n-1) + d\) mit \(k > 0\) „führt auf vier Fälle, die in
  Abhängigkeit des Anfangswertes sowie der Parameter d und w bzw. k untersucht und mit Sachsituationen verknüpft werden. Zusammenhänge
  zwischen iterativer und expliziter Beschreibung begrenzten Wachstums werden hergestellt. In den Fällen, in denen sich begrenztes Wachstum
  ergibt, kann die Grenze G bestimmt werden.“ → der Ersatz in `10-potenzen-ganzzahlig`. Das KC schreibt die Vorschrift mit \(n - 1\) auf
  der rechten Seite, mit \(k\) und \(d\) und nennt die Grenze \(G\); der Ersatz-Trainer übernimmt genau das (Bestand groß geschrieben:
  \(B(n) = k \cdot B(n-1) + d\)).
- **Kern** (Z. 2409–2414): „exponentielle Wachstums- und Abnahmeprozesse modellieren – Sachsituationen iterativ und explizit modellieren –
  lineare und exponentielle Prozesse voneinander abgrenzen – Überlagerung von linearem und exponentiellem Wachstum untersuchen – Bestimmen
  der Grenze G beim begrenzten Wachstum – Vergleich der expliziten und iterativen Darstellung“.
- **Kern** (Z. 2415–2422): „Exponentialfunktionen untersuchen – Parametervariation – Zusammenhang von Funktionsgleichung und -graph für
  \(f(x) = a \cdot b^x + c\) – hilfsmittelfreies Skizzieren der Graphen \(f(x) = a \cdot b^x\) für \(b > 0\) – Funktionsgleichungen aus
  zwei Punkten bestimmen, in einfachen Fällen hilfsmittelfrei – Ausgleichsfunktionen mithilfe des Regressionsmoduls oder
  Parametervariation bestimmen“. Dazu Z. 2396–2405 (Parametervariation wie bei linearen und quadratischen Funktionen, „Darstellungswechsel
  Gleichung – Graph – Tabelle“, „Bedeutung der Parameter erläutern“, „Die Rechengesetze für Potenzen werden genutzt, um Erkenntnisse über
  die Funktionen oder einen zugehörigen Sachzusammenhang zu gewinnen“) → `10-exponentialfunktionen`. Der Parameter \(c\) ist Kern.
  Regression braucht ein Werkzeug und Daten; im Trainer nicht abbildbar.
- **Logarithmus** (Z. 2406 und Kap. 3.2.1, Z. 996–1002): „nennen \(\log_b(a)\) als Lösung von \(b^x = a\)“, „nutzen das Wurzelziehen und das
  Logarithmieren als Umkehroperationen zum Potenzieren“. Der Logarithmus ist also KC – aber als \(\log_b(a)\), nicht als \(\ln\) und ohne
  Logarithmengesetze. Die drei Altaufgaben mit \(\ln\) in den Lösungswegen (`10-wachstum-linear-exponentiell` #25, #26, #31) sind entsprechend
  umgeschrieben; in beiden Durchgangs-Trainern gibt es jetzt je eine Aufgabe, deren Lösung ausdrücklich \(\log_b(a)\) ist, und der Tipp
  nennt daneben das gezielte Probieren.
- **Kap. 3.2.4** (Z. 1261–1271): „modellieren lineares, exponentielles und begrenztes Wachstum explizit und iterativ“, „interpretieren den
  Wachstumsfaktor beim exponentiellem Wachstum als prozentuale Änderung und grenzen lineares und exponentielles Wachstum gegeneinander ab“;
  Z. 1275–1285: „beschreiben und begründen Auswirkungen von Parametervariationen bei … Exponentialfunktionen“.
- **Nicht im KC der Sek I und deshalb nicht verwendet:** \(e\)-Funktion, \(\ln\), Ableitung (Lehrplan-Gate), Logarithmengesetze, die Wörter
  „Asymptote“ und „(streng) monoton“ (Volltextsuche: kein Treffer in der KC-Datei der Sek I). Der Altbestand von `10-exponentialfunktionen`
  benutzte „waagerechte Asymptote“ in #10, #27, #30 und „streng monoton fallend“ in #32. Jetzt steht dort in Worten, was gemeint ist („die
  Funktionswerte nähern sich dem Wert …, ohne ihn zu erreichen“, „der Graph fällt“). „Halbwertszeit“ und „Verdopplungszeit“ stehen nicht
  wörtlich im KC, sind aber die Standard-Sachsituationen zu \(b^x = a\); beide Wörter werden in der Aufgabe erklärt.
- Der Lernbereich „Näherungsverfahren als Grenzprozesse“ (S16, Z. 2499, 2513) greift „exponentieller Zerfall und begrenztes Wachstum als
  Grenzprozesse“ wieder auf. Das gehört in den Trainer des Blocks E (`8-gebrochen-rationale-einfuehrung`, Ersatz „Grenzprozesse &
  Zahlbereiche“); hier bleibt davon nur, was zum Modell gehört (die Grenze wird nicht erreicht, weil der Rest in jedem Schritt mit
  demselben Faktor multipliziert wird).

## Zuschnitt der drei Trainer

Vorher: `10-wachstum-linear-exponentiell` hatte trotz des Dateinamens keine einzige Aufgabe zu linearem Wachstum auf Stufe 1 bis 3 und
bestand dort aus Faktor-Fragen und Zinseszins-Rechnungen; `10-exponentialfunktionen` (aus Spalte 12 gekommen) rechnete auf Stufe 4 dieselben
Sachaufgaben (Bakterien, Neuwagen) und auf Stufe 5 dieselben Zwei-Punkte-Aufgaben wie der Wachstums-Trainer (#27, #30 dort); beide
hatten dieselbe Abkühlungsaufgabe (#33). `10-potenzen-ganzzahlig` wiederholte die Potenzgesetze aus `9-binomische-formeln-vertieft` und
enthielt Potenzfunktionen mit negativen Exponenten (Einführungsphase).

- **`10-wachstum-linear-exponentiell`** – *Vorgänge in Schritten*: lineares und exponentielles Wachstum unterscheiden (gleicher Zuwachs
  gegen gleicher Faktor), Prozentsatz ↔ Wachstumsfaktor, Folgen und Tabellen fortsetzen und zuordnen, iterative und explizite Beschreibung
  desselben Vorgangs, Sachsituationen (Zinseszins, Wertverlust, Bakterien, Zerfall), Rückwärtsrechnen (Startwert, Prozentsatz), Verdopplungs-
  und Halbwertszeit, lineare gegen exponentielle Prognose. Schreibweise: Bestand \(B(n)\) nach \(n\) Schritten, Wachstumsfaktor \(q\)
  (wie in der Zinsrechnung). Sachkontext ab Stufe 3.
- **`10-exponentialfunktionen`** – *die Funktion als Objekt*: \(f(x) = a \cdot b^x\) und \(f(x) = a \cdot b^x + c\) für alle \(x\), auch
  negative; Funktionswerte, Wertetabelle, Eigenschaften des Graphen in Worten, Bedeutung von \(a\), \(b\), \(c\) (Parametervariation),
  Funktionsgleichung aus zwei Punkten, einfache Exponentialgleichungen (Exponentenvergleich, \(\log_b\)), Potenzgesetze als Werkzeug
  (\(f(x+1) = b \cdot f(x)\), \(b^{-x} = (\frac{1}{b})^x\)). Ohne Sachkontext.
- **`10-potenzen-ganzzahlig`** (Ersatz „Begrenztes Wachstum & iterative Modelle“) – *alles, was eine Grenze oder einen festen Zusatz hat*:
  rekursive Vorschriften lesen und ausführen, Zuwachs als Anteil des Rests \(G - B\), Überlagerung \(B(n) = k \cdot B(n-1) + d\)
  (Medikament, Sparplan, Kredit, Fischteich), Grenze \(G\) bestimmen, Start über oder unter der Grenze, Zusammenhang zur expliziten
  Darstellung \(B(n) = G - c \cdot k^n\), Vergleich der drei Modelle. Die Abkühlungsaufgaben der beiden anderen Trainer (je #33) sind
  hierher gewandert (jetzt eine Aufgabe, #19).

Regeln gegen Dopplungen zwischen den dreien:
- „Zwei Messwerte bestimmen das Modell“ steht als *Funktionsgleichung aus zwei Punkten* nur im Exponentialfunktionen-Trainer; der
  Wachstums-Trainer fragt stattdessen nach dem Zwischenwert (#23) und verbindet ein lineares mit einem exponentiellen Wachstum, die nach
  zwei Jahren gleich groß sind (#26). „Zwei Modelle aus denselben zwei Werten, Unterschied der Vorhersagen“ steht nur im Ersatz-Trainer
  (#34, exponentiell gegen begrenzt); die gleich gebaute Aufgabe des Wachstums-Trainers (linear gegen exponentiell) ist nach dem
  Prüfdurchgang ersetzt worden.
- „Wann sind zwei Größen gleich?“ steht nur als Schnittstelle zweier Graphen im Exponentialfunktionen-Trainer (#30).
- Reines lineares und reines exponentielles Wachstum als rekursive Vorschrift kommt im Ersatz-Trainer nur auf Stufe 1 vor (je ein Schritt,
  als Einstieg in die Schreibweise); ab Stufe 2 hat jede Vorschrift dort eine Grenze oder einen Zusatz.
- Kontexte und Namen sind über die drei Trainer verteilt (Zinseszins, Auto, Bakterien, Zerfall nur im Wachstums-Trainer; Medikament,
  Abkühlung, Teich, Akku, Kredit nur im Ersatz-Trainer).

Abgrenzung zu den Nachbarn:
- `12-wachstum-begrenzt` und `12-e-funktion` (Qualifikationsphase, noch nicht überarbeitet): dort \(f(t) = S - a \cdot e^{-kt}\), \(\ln\),
  Ableitung, Änderungsrate. Klasse 10 bleibt bei Schritten, beim Faktor je Schritt und bei \(a \cdot b^x\); die explizite Darstellung des
  begrenzten Wachstums erscheint nur als \(G - c \cdot k^n\) mit ganzen Schrittzahlen. Das Wort „Sättigungsgrenze“ bleibt der Oberstufe;
  hier heißt sie wie im KC „Grenze \(G\)“.
- `7-prozent-anwendungen-zins` (#36: Zinseszins über zwei Jahre, \(1000\,€\) zu \(5\,\%\)) und die beiden Prozent-Trainer: Die
  Altaufgabe #15 („zwei Jahre je \(5\,\%\) – insgesamt?“) war dieselbe Idee und ist entfallen; die Kette „erst \(+p\,\%\), dann
  \(-p\,\%\)“ kommt hier nicht vor.
- `9-binomische-formeln-vertieft` (Potenzgesetze, auch negative Exponenten; #33 „kleinste \(n\) mit \(2^{-n} < 0{,}001\)“) und
  `9-potenzen-wurzeln`: Potenzen werden hier nur benutzt, nicht geübt.
- `8-gebrochen-rationale-einfuehrung` (Block E, Ersatz „Grenzprozesse & Zahlbereiche“, gleichzeitig entstanden und nach dessen Commit
  gegengelesen): Dort berühren #12 (Halbierungsfolge, erste Zahl unter 1), #24 (zwei Folgen: Halbieren und „Abstand zur 10 halbieren“) und
  #29 (\(\frac{1}{n}\) gegen \(0{,}5^n\)) das Thema. Keine sinngleiche Aufgabe: Dort sind es reine Zahlenfolgen ohne Vorschrift und ohne
  Sachsituation, gefragt ist der Grenzprozess selbst; hier wird modelliert und gerechnet. Dieselbe Einsicht („der Rest wird halbiert und
  ist deshalb nie 0“) trägt dort einen Distraktor von #24 und hier die Aufgabe `10-potenzen-ganzzahlig` #31 sowie den Schluss von
  `10-wachstum-linear-exponentiell` #36 – das ist gewollt (das KC nennt den Inhalt in beiden Lernbereichen, Z. 2394 und 2513).


## Gemeinsame Regeln dieses Blocks

- **Schreibweisen:** Wachstums-Trainer \(B(n)\) und Wachstumsfaktor \(q\); Exponentialfunktionen \(f(x) = a \cdot b^x + c\) wie im KC;
  Ersatz-Trainer \(B(n) = k \cdot B(n-1) + d\) und Grenze \(G\) wie im KC. Rekursive Vorschriften stehen immer zusammen mit dem
  Anfangswert in der Aufgabe („Für einen Bestand gilt \(B(0) = …\) und \(B(n) = …\)“). Jede Sachaufgabe nennt Zeiteinheit, Startwert, den
  Zeitpunkt der Messung („direkt nach der dritten Einnahme“, „nach \(3\) Jahren, direkt nach der dritten Einzahlung“) und die Rundung.
- **Tabellen** stehen als KaTeX-`array` mit `\footnotesize` in der Frage (Vorbild `9-daten-zufall-boxplot`); alle sieben Tabellen sind bei
  360 px Breite im Bild geprüft und passen ohne Überlauf.
- **Rundung und Toleranz:** Nicht ganzzahlige Antworten verlangen „als Dezimalzahl“ oder nennen die Rundung. Toleranzen liegen nie auf der
  Rundungsstufe (0,011 bei Cent, 0,055 bzw. 0,05 bei einer Dezimalstelle, 0,006 bei zwei Dezimalstellen, wo ein Fehlweg 0,01 daneben liegt);
  glatte Ergebnisse, die auch über gerundete Zwischenwerte erreicht werden, haben 0,5.
- **Nachrechnen** (`wlib.py`, `rechne_wl.py`, `rechne_ef.py`, `rechne_bw.py` im Scratchpad `w10c`, je Stufe aufrufbar, nur Gleitkomma):
  Wo der Lösungsweg die Potenz benutzt, läuft im Skript die Schleife Schritt für Schritt, und umgekehrt (geschlossene Form
  \(G + (B(0) - G) \cdot k^n\)); Umkehraufgaben und Parameter aus Punkten werden durch Bisektion bestimmt, Grenzen durch 3000 Iterationen
  gemessen, Aussagen über Graphen an 161 Stellen abgetastet; die Behauptung „die Grenze wird nie erreicht“ ist mit Brüchen exakt gerechnet
  (in Gleitkomma wird der Bestand nach 55 Schritten genau 100). Gegen die Toleranz laufen je Aufgabe 5 bis 11 Fehlwege: Prozentsatz statt
  Faktor, linear statt exponentiell, Zuwachs zum Bestand statt zum Rest, ein Schritt zu viel oder zu wenig, Wurzel vergessen oder halbiert,
  Potenz als Produkt gelesen, Basis und Exponent vertauscht, Reihenfolge von Verzinsen und Einzahlen, gerundete Zwischenwerte. Dazu das
  Zufallsnetz: Lösung gleich einer gegebenen Zahl oder gleich Summe, Differenz, Produkt, Quotient oder Mittelwert zweier gegebener Zahlen
  (Zahlwörter und Tabellenwerte eingeschlossen).
- **Was das Zufallsnetz gefunden hat** (alle vor dem Setzen mit anderen Zahlen behoben; Nummern nach dem Endstand):
  `10-exponentialfunktionen` #7 (\(3 \cdot 2^4\): wegen \(2^4 = 4^2\) ging der Fehler „Basis und Exponent vertauscht“ durch), #15
  (\(a = 5 = 2 + 3\)), #13 und #27 (Lösung \(3\) als Mittel von \(4\) und \(2\)), #17 (Lösung \(4\) aus den Tabellenwerten), #27 (erste
  Zahlen: der Fehler \(2x = 4\) statt \(2^x = 4\) traf die Lösung \(2\); \(2^x = 16\) hätte \(\sqrt{16} = 4\) durchgelassen), #29
  (\(b = 1{,}5\) und \(b = 3\) sind Mittel und Summe der Stellen \(1\) und \(2\)), #30 (bei Schnittstellen
  \(10 \cdot 2^x = 640 \cdot 0{,}5^x\) trifft fast jede kleine Lösung eine Kombination aus Faktor und Basis); `10-potenzen-ganzzahlig`
  #25 (bei halbierten Zuwächsen ist die Grenze „letzter Wert plus letzter Zuwachs“), #28 (\(G : B(0)\) traf die Schrittzahl), #29
  (\(c = B(0) + d\)), #34 (Unterschied der Modelle gleich dem ersten Zuwachs). Kleine ganze Lösungen neben Basis \(2\) oder \(3\) sind
  die Stelle, an der es fast immer knallt.
- **Was das Zufallsnetz nicht gefunden hat** (Befund des zweiten Prüfers, `10-exponentialfunktionen` #25): Bei \(P(1 \mid 24)\),
  \(Q(3 \mid 6)\) lieferte der Fehlweg „Faktor durch die Schrittzahl teilen statt Wurzel ziehen“ die richtige Lösung, weil
  \(\sqrt{4} = 4 : 2\) ist – und zwar nur, wenn man den größeren durch den kleineren Wert teilt. Das Netz hatte den Fehlweg nur in der
  anderen Richtung (\(0{,}25 : 2\)). Seither laufen „halbiert vorwärts“ und „halbiert rückwärts“ beide mit; Quotienten \(4\) und
  \(\frac14\) sind bei Abstand 2 zu meiden.


## 10-wachstum-linear-exponentiell — Lineares & exponentielles Wachstum
KC: 9/10 „Exponentielle Zusammenhänge“ (S14, SI Z. 2381–2383: „… wird exponentielles Wachstum iterativ eingeführt und auch explizit beschrieben sowie gegen lineares Wachstum abgegrenzt“; Kern Z. 2409–2411, 2414: „Sachsituationen iterativ und explizit modellieren – lineare und exponentielle Prozesse voneinander abgrenzen – Vergleich der expliziten und iterativen Darstellung“; Kap. 3.2.4 Z. 1261–1271; Logarithmus Z. 996–1002 und 2406).
Gelesen: alle 36 Aufgaben. Urteil Lehrplan: passt im Stoff (Abgleich: „passt; iterative Modelle und begrenztes Wachstum fehlen“). Punkte aus dem Abgleich: iterative Beschreibung – erledigt (#7, #9 rekursive Vorschrift, #10 explizit, #24 Vorschrift und Situation); begrenztes Wachstum – erledigt im Ersatz-Trainer `10-potenzen-ganzzahlig`; #33 (Abkühlung, einzige Aufgabe zum begrenzten Wachstum) – dorthin umgezogen (dort #19, neue Zahlen); Logarithmus „nur in Lösungswegen (#25, #26, #31)“ und dort als \(\ln\) – erledigt: #22 und #35 haben \(\log_b(a)\) als Lösung, \(\ln\) kommt nicht mehr vor.
Eigene Funde im Altbestand: Kein lineares Wachstum auf Stufe 1 bis 4 außer einem Distraktor (#24) – der Trainer hieß „linear – exponentiell“ und übte nur exponentiell. #7, #8, #11, #14 waren viermal dieselbe Zinseszins-Rechnung (zwei davon auf Stufe 2 mit Sachkontext und der Formel im Tipp), #13, #15, #16 dreimal „Prozente addieren sich nicht“, #19, #20, #21 dreimal „Wurzel aus dem Quotienten“ mit der fertigen Gleichung im Tipp, #22, #23 zweimal „Startwert zurückrechnen“ mit der fertigen Gleichung im Tipp, #27, #30 zweimal dieselben Zahlen (\(q^3 = 8\)). #9: „\(145{,}8\) Tiere“. #12: Auto für \(800\,€\). #31, #36: Tipp enthielt die fertige Gleichung. #35: Tipp nannte die beiden Jahre, auf die es ankam. #15 war dieselbe Idee wie `7-prozent-anwendungen-zins` #36.
Titel (Empfehlung, nicht gesetzt – Parallelbetrieb): an allen drei Stellen „Lineares & exponentielles Wachstum“ (bisher `<title>` „Exponentielles Wachstum & Zerfall“, Kopfzeile „Wachstum & Zerfall“).

Befund zum Aufbau: Die Stufen waren Teilthemen (1 = Prozentsatz → Faktor, sechsmal; 2 = \(B_0 \cdot q^n\) einsetzen, sechsmal; 3 = dasselbe mit einem Schritt mehr; 4 = \(q\) oder \(B_0\) zurückrechnen; 5 = Logarithmus; 6 = Gemischtes). Neuer Aufbau: Stufe 1 ein Schritt (Prozentsatz ↔ Faktor, Folge fortsetzen, Art benennen); Stufe 2 Bestand nach wenigen Schritten, iterativ und explizit, ohne Kontext; Stufe 3 Sachsituationen mit Zwischenergebnis; Stufe 4 Umkehraufgaben und Modellwahl; Stufe 5 zwei Verfahren, zwei Bedingungen, Fehlersuche; Stufe 6 Aussagen prüfen (lineares Denken gegen exponentielles Wachstum). Alle 36 Aufgaben sind neu gesetzt; aus dem Altbestand übernommen sind #1, #2 (jetzt #3), #29 (jetzt #27, neuer Tipp) und – mit neuen Zahlen oder neuer Frage – #7 (jetzt #13), #13 (jetzt #14), #24 (jetzt #15 als Tabelle mit Lücke), #10 (jetzt #18, umgekehrt), #23 (jetzt #19), #20 (jetzt #20, Prozentsatz statt Faktor), #25 (jetzt #22), #28 (jetzt #25), #34 (jetzt #28), #35 (jetzt #32), #31 (jetzt #35). Aus dem ersetzten `10-potenzfunktionen` kommt die Schachbrett-Aufgabe (dort #23, jetzt #17 mit ausgeschriebener Zählung „elftes Feld“).

| id | Stufe | Kriterium laut Rubrik | Befund | Änderung |
|---|---|---|---|---|
| 1 | 1 | ein Schritt | trägt (\(+5\,\%\) → Faktor) | Wortlaut ohne Formelbuchstaben; Distraktor \(0{,}95\) durch \(5\) ersetzt |
| 2 | 1 | ein Schritt | (alt: \(-3\,\%\) → Faktor, jetzt #3) | neu: umgekehrt, Faktor \(1{,}2\) → Prozentsatz |
| 3 | 1 | ein Schritt | dritte Faktor-Frage | jetzt die alte #2 (Abnahme um \(3\,\%\)) |
| 4 | 1 | ein Schritt | vierte Faktor-Frage mit Kontext (Auto) | neu: lineare Folge fortsetzen |
| 5 | 1 | ein Schritt | fünfte Faktor-Frage mit Kontext | neu: exponentielle Folge fortsetzen |
| 6 | 1 | ein Schritt | sechste Faktor-Frage | neu: \(5;\ 10;\ 20;\ 40\) – Art und Begründung als 2×2-Raster |
| 7–12 | 2 | Standardverfahren, zwei Schritte, kein Kontext | sechs Sachaufgaben \(B_0 \cdot q^n\), Formel im Tipp | neu: rekursive Vorschrift exponentiell (#7) und linear (#9), Abnahme in Worten (#8), explizite Gleichung zuordnen (#10) und auswerten (#11), Zuwachs in Prozent aus zwei Werten (#12; nach dem Prüfdurchgang Prozentsatz statt Faktor, damit es zwei Schritte sind) |
| 13 | 3 | Klassenarbeits-Standard | Zinseszins (alt #7 auf Stufe 2) | neue Zahlen, Tipp ohne Formel |
| 14 | 3 | Zwischenergebnis nötig | (alt #13: Rest in Prozent) | Gesamtabnahme nach drei Jahren je \(20\,\%\) „des jeweiligen Werts“ (Zusatz nach dem Prüfdurchgang: bei einer Maschine läge sonst die lineare Abschreibung nahe); die Fehlwege \(60\) und \(51{,}2\) fallen |
| 15 | 3 | Zwischenergebnis nötig | alt #24 (Stufe 4): „Welche Tabelle ist exponentiell?“ – drei lineare Distraktoren, kein Rechnen | neu: Tabelle mit Lücke, Art nicht genannt |
| 16 | 3 | Zwischenergebnis nötig | — | neu: lineares gegen exponentielles Angebot nach vier Jahren |
| 17 | 3 | Zwischenergebnis nötig | — | Schachbrett aus `10-potenzfunktionen` (alt #23): Zahl der Verdopplungen ist die Leistung |
| 18 | 3 | Zwischenergebnis nötig | alt #10 (vorwärts) | umgekehrt: Wann sind es \(19\,200\)? (Exponentenvergleich) |
| 19 | 4 | Umkehraufgabe | alt #22/#23: fertige Gleichung im Tipp | Startkapital aus dem Endbetrag; glatte Zahlen (\(5000\)), Tipp nennt nur den Weg |
| 20 | 4 | Umkehraufgabe | alt #19–#21: \(q\) aus zwei Werten, Gleichung im Tipp | Prozentsatz aus drei Stunden (dritte Wurzel); der Fehlweg „\(72{,}8\,\% : 3\)“ fällt |
| 21 | 4 | Modell aus Text wählen | — | neu: Welcher Vorgang ist exponentiell? (zwei lineare, ein quadratischer Distraktor) |
| 22 | 4 | Verfahren wählen | alt #25 (Stufe 5) mit \(\ln\) | Verdopplungszeit als \(\log_{1{,}06}(2)\). Nach dem Prüfdurchgang Algenfläche statt Guthaben: Bei jährlicher Zinsgutschrift wäre „12 Jahre“ vertretbar gewesen; Tipp ohne Zielwert und Basis |
| 23 | 4 | Umkehraufgabe | — | neu: Wert zwischen zwei Messungen (\(q^2 = 2{,}25\)); der Mittelwert \(650\) fällt |
| 24 | 4 | Modell wählen | — | neu: rekursive Vorschrift ↔ Sachsituation; Distraktor „\(12\,€\) = \(4\,\%\) von \(300\,€\)“ stimmt nur im ersten Jahr |
| 25 | 5 | zwei Verfahren | alt #28: Halbwertszeit → Prozent pro Jahr | Halbwertszeit 8 Tage → Rest nach 3 Tagen (Tagesfaktor, dann Potenz) |
| 26 | 5 | zwei Verfahren | alt #27/#30: \(q\) und \(B(0)\) aus zwei Werten – das ist jetzt Stoff des Exponentialfunktionen-Trainers | neu: ein linear und ein exponentiell wachsender Verein sind nach zwei Jahren gleich groß – Prozentsatz gesucht (\(q^2 = 1{,}69\)). Die erste Fassung (lineare und exponentielle Prognose aus denselben zwei Werten) hatte dieselbe Form wie `10-potenzen-ganzzahlig` #34 und ist nach dem Prüfdurchgang ersetzt |
| 27 | 5 | Fehler im Rechenweg | alt #29, Tipp verriet den Schritt („Wie zieht man die Wurzel aus 0,64?“) | Tipp neu (Probe mit dem Ergebnis), Rest trägt |
| 28 | 5 | zwei Verfahren | alt #34 (Stufe 6): „die Hälfte entnommen“ – Halbieren und Wachsen sind vertauschbar, die Aufgabe prüfte die Reihenfolge nicht | \(400\) Bakterien entnommen: Jetzt ist die Reihenfolge entscheidend (\(844\) fällt) |
| 29 | 5 | zwei Verfahren | — | neu: gleichbleibender Jahreszuwachs zu \(+75\,\%\) und \(+12\,\%\) (\(q^2 = 1{,}96\)); der Mittelwert \(43{,}5\) fällt |
| 30 | 5 | Parameter aus zwei Bedingungen | — | neu: Zinsen im ersten und zweiten Jahr → Anfangsguthaben |
| 31 | 6 | Aussage prüfen | alt #36: \(q^4 = 3\), Gleichung im Tipp | neu: Verdopplung in 6 Jahren – was gilt für 3, 12, 18 Jahre? |
| 32 | 6 | Aussage prüfen | alt #35: Tipp nannte \(t = 18\) und \(t = 19\) | Behauptung „A bleibt immer vorn“; neue Zahlen (Überholen nach 9 Jahren statt 19), numerisch |
| 33 | 6 | Aussage prüfen | alt #32: Tabelle erkennen (Stufe 3) | neu: Verdopplungszeit hängt nicht vom Anfangswert ab |
| 34 | 6 | Aussage prüfen | alt #33: Abkühlung (jetzt im Ersatz-Trainer) | neu: „in den vier Jahren davor und danach je 300“ – Zuwachs danach minus Zuwachs davor (\(292{,}5\)); exponentiell vorwärts und rückwärts. Die erste Fassung (nur vorwärts, \(480\)) war nach dem Prüfdurchgang die halbe alte #26. Toleranz 0,105, damit der Umweg über den Jahresfaktor \(1{,}1247\) (\(292{,}56\)) angenommen wird |
| 35 | 6 | Aussage prüfen | alt #31: C-14, Gleichung im Tipp, \(\ln\) | „nach vier Halbwertszeiten weniger als \(5\,\%\)“; Lösung über \(\log_{0{,}5}\). Nach dem Prüfdurchgang Tipp ohne Basis und Toleranz 0,7 statt 1,3 (früh gerundete Wege mit 129 fallen jetzt; nach 129 Jahren sind es noch \(5{,}08\,\%\)) |
| 36 | 6 | Fallunterscheidung | — | neu: lineare gegen exponentielle Abnahme – wird der Tank leer? Nach dem Prüfdurchgang zwei Distraktoren, die Rechnen verlangen („nach 5 Stunden gleich viel“, „B ab der zweiten Stunde stets weniger als A“) |

Nachrechnen (`rechne_wl.py`): 36 Aufgaben, 0 Fehler, kein offener Zufallstreffer. Nicht rechnerisch, sondern am Begriff entschieden: keine (auch #21 und #24 sind simuliert).
Zweiter Prüfdurchgang (alle 36): kein Fehler, 2 Mängel (#34 Stufe und Dopplung, #35 Tipp), Hinweise zu #12, #14, #16/#32, #20/#23, #22, #36. Eingearbeitet: #34 und #26 neu, #35 (Tipp, Toleranz), #12 (zwei Schritte), #14 („des jeweiligen Werts“), #22 (stetiger Vorgang statt Guthaben, Tipp), #36 (Distraktoren, Zahlen in Formelschrift). Nicht übernommen: der Vorschlag, #26 und #34 nur die Stufen tauschen zu lassen (die Dopplung mit `10-potenzen-ganzzahlig` #34 wäre geblieben – stattdessen #26 neu); #16/#32 (beide „fester Betrag gegen Prozent“, aber verschiedene Anforderung auf Stufe 3 und 6 – belassen); #20/#23 (beide mit Wurzel, verschiedene Zielgröße – belassen). Der Prüfer hat alle 26 Lösungswerte, die MC-Schlüssel und die Toleranzen gegen Fehlwege bestätigt.
Nachtrags-Prüfer (ein Agent für alle drei Trainer; hier #12, #26, #34, #36): kein Fehler, kein Mangel; zwei Hinweise (#34 Toleranz, #36 Satz im Lösungsweg) – beide eingearbeitet.


## 10-exponentialfunktionen — Exponentialfunktionen
KC: 9/10 „Exponentielle Zusammenhänge“ (S14, SI Z. 2415–2421: „Exponentialfunktionen untersuchen – Parametervariation – Zusammenhang von Funktionsgleichung und -graph für \(f(x) = a \cdot b^x + c\) – hilfsmittelfreies Skizzieren der Graphen \(f(x) = a \cdot b^x\) für \(b > 0\) – Funktionsgleichungen aus zwei Punkten bestimmen, in einfachen Fällen hilfsmittelfrei“; Z. 2396–2405: Darstellungswechsel Gleichung – Graph – Tabelle, Bedeutung der Parameter, Potenzgesetze als Werkzeug; Kap. 3.2.4 Z. 1275–1285; Logarithmus Z. 996–1002; einfache Exponentialgleichungen Z. 1477).
Gelesen: alle 36 Aufgaben. Urteil Lehrplan: passt im Stoff (der Trainer kam mit Task 2 aus Spalte 12; Abgleich: „alle 36 Aufgaben \(a \cdot b^x\) ohne \(e\), ohne Ableitung, ohne \(\ln\)“). Als Klasse-10-Trainer fehlte ihm aber gerade der Kern: Parametervariation kam nur als „Basis größer oder kleiner als 1“ vor, \(a\) als Streckung gar nicht, \(c\) nur in drei Aufgaben der Stufen 5 und 6; die Zwei-Punkte-Aufgaben lieferten auf Stufe 3 und 4 immer \(a\) mit oder hatten die fertige Gleichung im Tipp.
Eigene Funde im Altbestand: „waagerechte Asymptote“ (#10, #27, #30) und „streng monoton fallend“ (#32) – beide Wörter kennt das KC der Sek I nicht (siehe oben); #16 fragte „Antworte mit 1 für ja, 0 für nein“ (Ratewahrscheinlichkeit \(50\,\%\), keine Rechnung prüfbar); #23, #24 (Bakterien, Neuwagen) und #33 (Kaffee) waren Sachaufgaben des Wachstums-Trainers; #1 bis #6 sechsmal „Potenz ausrechnen“; #7 bis #9 dreimal „Wachstum oder Zerfall“; #19 bis #22 viermal „\(a\) gegeben, \(b\) aus einem Punkt“ (Stufe 3) mit der Gleichung im Tipp; #29 Tipp enthielt die fertige Gleichung; #36 war die Idee „exponentiell überholt linear“ des Wachstums-Trainers.
Titel: bleibt „Exponentialfunktionen“ (an allen drei Stellen schon einheitlich).

Befund zum Aufbau: Stufe 1 bis 4 lagen je eine Stufe zu tief und waren Teilthemen. Neuer Aufbau: Stufe 1 ein Schritt (Funktionswert, Exponentialfunktion erkennen, steigt oder fällt, Basis aus der Tabelle); Stufe 2 Standardverfahren (Funktionswert mit Faktor und negativem Exponenten, Punktprobe, Tabelle → Gleichung, Verhalten für kleine \(x\), \(y\)-Achsenabschnitt mit \(c\)); Stufe 3 Zwischenergebnisse (zwei Punkte mit einem auf der \(y\)-Achse, Wirkung von \(a\), \(a\) aus einem Punkt, Exponentialgleichung, Tabelle nach links fortsetzen, Beschreibung → Gleichung); Stufe 4 Umkehraufgaben und Gleichung aus der Beschreibung (\(\log_2\), \(c\) aus dem Verhalten und Schnitt mit der \(x\)-Achse, Vergleich zweier Basen, Spiegelung, zwei benachbarte Punkte); Stufe 5 zwei allgemeine Punkte, zwei und drei Parameter mit \(c\), Schnittstelle, Fehlersuche; Stufe 6 Fallunterscheidung und Aussagen prüfen mit den Potenzgesetzen. Alle 36 Aufgaben sind neu gesetzt; aus dem Altbestand übernommen sind #5 (jetzt #3), #31 (trägt, Wortlaut „genau für“) und – mit neuen Zahlen oder neuer Frage – #8 (jetzt #5), #14 (jetzt #8), #16 (jetzt #9 als Auswahl), #10 (jetzt #11), #18 (jetzt #15), #17/#29 (jetzt #13), #26 (jetzt #25), #34 (jetzt #26), #27 (jetzt #22), #30 (jetzt #29), #35 (jetzt #34).

| id | Stufe | Kriterium laut Rubrik | Befund | Änderung |
|---|---|---|---|---|
| 1–6 | 1 | ein Schritt | sechsmal Potenz ausrechnen | \(f(0) = a\) (#1), \(2^5\) (#2), \(2^{-1}\) (#3, alt #5), Exponentialfunktion erkennen (#4; Lösungsweg ohne das Wort „Potenzfunktion“, das im KC der Sek I nicht vorkommt), steigt oder fällt (#5), Basis aus der Tabelle (#6) |
| 7 | 2 | Standardverfahren | — | \(7 \cdot 2^3\); die erste Fassung \(3 \cdot 2^4\) ließ wegen \(2^4 = 4^2\) den Vertauschungsfehler durch |
| 8–12 | 2 | Standardverfahren | dreimal „Wachstum oder Zerfall“, Asymptote, „radioaktiver Zerfall“ | negativer Exponent mit Basis \(0{,}5\) (#8), Punktprobe mit vier verschiedenen Stellen (#9, \(2 \cdot 5^x\); nach dem Nachtrag: drei Optionen mit \(x = 2\) waren nur „berechne \(f(2)\)“), Tabelle → Gleichung (#10), Verhalten für \(x = -1, -2, -3, \ldots\) in Worten (#11), \(f(0)\) bei \(a \cdot b^x + c\) (#12; nach dem Prüfdurchgang von Stufe 3 hierher: Einsetzen ohne Parameter) |
| 13–18 | 3 | Klassenarbeits-Standard, Zwischenergebnis | Differenz zweier Funktionswerte, ja/nein-Frage, \(a\) und \(b\) aus \(f(0)\), \(f(1)\) | zwei Punkte mit einem auf der \(y\)-Achse (#13), Streckung durch \(a\) (#14), \(a\) aus einem Punkt (#15; nach dem Prüfdurchgang von Stufe 2 hierher: Parameter und Zwischenergebnis), \(20 \cdot 2^x = 5\) mit negativer Lösung (#16; vorher \(5 \cdot 2^x = 40\), sinngleich mit `10-wachstum-linear-exponentiell` #18), Tabelle nach links (#17), Beschreibung → Gleichung (#18) |
| 19 | 4 | Umkehraufgabe | alt: \(a\) gegeben, \(b^2 = 9\) (Stufe 3) | neu: \(2^x = 10\), Lösung \(\log_2(10)\); Toleranz 0,006, damit \(3{,}31\) und \(3{,}33\) fallen |
| 20 | 4 | Modell aus Beschreibung | wie #19 | neu: steigt, \(f(0) = 1\), kommt für immer kleinere \(x\) dem Wert \(-2\) beliebig nahe → Gleichung mit \(c\). Wortlaut nach dem Prüfdurchgang in allen vier Aufgaben dieser Art (#20, #22, #27, #29): „für immer kleinere \(x\) (zum Beispiel \(x = -10\) oder \(x = -100\)) … beliebig nahe“ – „nähern sich“ allein träfe wörtlich auch auf \(3 \cdot 2^x + 1\) zu, und „immer kleinere \(x\)“ wurde als „\(x\) nahe 0“ lesbar |
| 21 | 4 | Verfahren wählen | wie #19 | neu: \(2^x\) gegen \(3^x\) – Lage der Graphen rechts und links der \(y\)-Achse |
| 22 | 4 | Umkehraufgabe | MC, Gleichung im Tipp | \(c\) aus dem Verhalten für kleine \(x\), dann Schnitt mit der \(x\)-Achse: \(2 \cdot 3^x - 162 = 0\) (alt #27 mit „Asymptote“). Basis 3, weil \(6 \cdot 2^x = 192\) die Zahlen des Wachstums-Trainers #18 waren. Nach dem Nachtrag von Stufe 5 hierher (ein Parameter, dann eine Gleichung der Stufe 3) |
| 23 | 4 | Verfahren wählen | Bakterien (Wachstums-Trainer) | neu: Spiegelung an der \(y\)-Achse, \(2^{-x} = 0{,}5^x\) |
| 24 | 4 | Umkehraufgabe | Neuwagen (Wachstums-Trainer) | neu: zwei benachbarte Punkte, \(a\) durch einen Schritt zurück |
| 25 | 5 | Parameter aus zwei Bedingungen | alt #25/#26 | fallend, Abstand 2: \(P(1 \mid 50)\), \(Q(3 \mid 2)\), \(b^2 = \frac{1}{25}\). Erste Fassung (\(24\) und \(6\)) verworfen – siehe „Was das Zufallsnetz nicht gefunden hat“ |
| 26 | 5 | Parameter aus zwei Bedingungen | alt #34 (Stufe 6) | negative Stelle, Abstand 3 (dritte Wurzel), gefragt \(f(1)\); \(Q(2 \mid 128)\), \(b = 4\). Erste Fassung (\(Q(2 \mid 54)\), \(b = 3\)) verworfen: \(b\) war gleich der Schrittzahl, und die Funktion war dieselbe wie in #10 |
| 27 | 5 | Parameter aus zwei Bedingungen | (alt #27 steht jetzt als #22) | \(a\) und \(c\) aus einem Punkt abseits der \(y\)-Achse (\(P(3 \mid 50)\)) und dem Wert, dem die Funktionswerte beliebig nahe kommen. Nach dem Nachtrag von Stufe 4 hierher; die erste Fassung mit \(P(0 \mid 3)\) war kerngleich mit #20 |
| 28 | 5 | Fehler im Rechenweg | alt #28: \(2^x\) als \(2 \cdot x\) gelesen (ein Schritt) | neu: Zwei-Punkte-Rechnung mit Fehler bei der Division der Potenzen (\(b^3\) statt \(b^2\)); die Folgeschritte sind folgerichtig. Tipp nach dem Prüfdurchgang ohne den Hinweis „auch die Division der Potenzen“ (zeigte auf den gesuchten Schritt) |
| 29 | 5 | Parameter aus drei Bedingungen | alt #30 (MC), Tipp mit allen drei Gleichungen | numerisch, ohne \(f(0)\): \(f(1) = 13\), \(f(2) = 73\), Grenzwert \(-7\) → \(b = 4\). Die erste Fassung mit \(f(0)\) zerfiel in drei Einzelschritte. \(b > 1\) steht in der Aufgabe, damit das Verhalten für kleine \(x\) eindeutig \(c\) liefert |
| 30 | 5 | zwei Verfahren | alt #29: Gleichung im Tipp | neu: Schnittstelle von \(10 \cdot 2^x\) und \(640 \cdot 0{,}5^x\) |
| 31 | 6 | Fallunterscheidung | trägt | Wortlaut „Für genau welche Werte“ und „genau für alle“, damit \(c > 0\) als Antwort falsch ist |
| 32 | 6 | Fallunterscheidung | „streng monoton“, Distraktor mit Quotient; für \(a > 0\) Grundwissen der Stufen 1 bis 3 | neu nach dem Prüfdurchgang: Aussage für jede Funktion mit \(a \neq 0\) und \(0 < b < 1\) – richtig ist nur „der Funktionswert rückt näher an die 0“; „fällt überall“ und „oberhalb der \(x\)-Achse“ scheitern an \(a < 0\). Der Lösungsweg nennt die Aussagen beim Inhalt (nach dem Nachtrag: „die ersten beiden Aussagen“ zeigte auf gemischte Positionen) |
| 33 | 6 | Aussage prüfen | Kaffee (jetzt im Ersatz-Trainer) | neu: \(8 \cdot 2^x = 2^{x+3}\) – Streckung als Verschiebung; Wortlaut „statt durch Strecken auch allein durch eine Verschiebung“ (vorher als „Strecken und zusätzlich Verschieben“ lesbar) |
| 34 | 6 | Aussage prüfen | alt #35 | \(f(x+2) = 6{,}25 \cdot f(x)\) |
| 35 | 6 | Aussage prüfen | alt #36 (exponentiell überholt linear – Wachstums-Trainer) | neu: „doppeltes \(x\), doppelter Funktionswert“ – \(3^{2x} = (3^x)^2\); „für jedes \(x\)“ steht in der Behauptung, weil sie an der einen Stelle \(x = \log_3 2\) stimmt. Schlusssatz des Lösungswegs nach dem Prüfdurchgang ohne „nur“ |
| 36 | 6 | Aussage prüfen | — | neu: Tabelle passt nicht zu \(a \cdot b^x\), aber zu \(a \cdot 2^x + c\) – \(c\) über die Differenzen |

Nachrechnen (`rechne_ef.py`): 36 Aufgaben, 0 Fehler, kein offener Zufallstreffer. Beurteilt und stehen gelassen: #1 (\(f(0) = a\) ist der Inhalt), #6 (Basis 3 steht auch als \(x\)-Wert in der Tabelle), #12 (\(3 - 5\) ist die Rechnung). Zu #22: Die Fehl-Lesart „immer kleinere \(x\) = \(x\) nahe 0“ gäbe \(c = -164\) und \(x \approx 4{,}011\) – gerundet die Lösung; deshalb der Klammerzusatz in der Frage.
Zweiter Prüfdurchgang (alle 36): kein Fehler, 2 Mängel (#25 Fehlweg trifft, #28 Tipp), Hinweise zu #4, #6/#9, #10/#26, #12/#15, #16, #20/#22/#27/#29, #32, #33, #35. Eingearbeitet: alle genannten (neue Zahlen bei #9, #16, #22, #25, #26, #27, #29; neue Aufgabe #32; Stufentausch #12/#15; Wortlaut #4, #20, #28, #33, #35). Nicht übernommen: der Wortlaut des Vorschlags zu #29 (\(b = 1{,}5\) ist der Mittelwert der Stellen 1 und 2 – stattdessen \(b = 4\)) und der zu #9 (hätte die Zahlen von #24 getroffen). Der Prüfer hat alle 21 Lösungswerte, die MC-Schlüssel und jede Option auch unter der Lesart „\(a \cdot b^x\) ist ein verschobener Graph von \(b^x\)“ bestätigt.
Nachtrags-Prüfer (hier #9, #16, #22, #25, #26, #27, #29, #32): kein Fehler, ein Mangel (#32 Verweis auf Positionen im Lösungsweg), zwei Hinweise (#9 Punktprobe, #22/#27 Stufenabstand) – alle drei eingearbeitet (dabei haben #22 und #27 die Plätze getauscht).
Für den Autor: Ob „Asymptote“ in Klasse 10 doch verwendet werden soll (das KC nennt das Wort nicht, die Lehrwerke schon), ist eine Lehrwerksfrage; die Aufgaben kommen jetzt ohne das Wort aus.


## 10-potenzen-ganzzahlig — Begrenztes Wachstum & iterative Modelle (Ersatz)
KC: 9/10 „Exponentielle Zusammenhänge“ (S14, SI Z. 2384–2393: Überlagerung \(b(n) = k \cdot b(n-1) + d\), „vier Fälle … in Abhängigkeit des Anfangswertes sowie der Parameter“, „Zusammenhänge zwischen iterativer und expliziter Beschreibung begrenzten Wachstums“, „kann die Grenze G bestimmt werden“; Kern Z. 2410, 2412–2414: „Sachsituationen iterativ und explizit modellieren – Überlagerung von linearem und exponentiellem Wachstum untersuchen – Bestimmen der Grenze G beim begrenzten Wachstum – Vergleich der expliziten und iterativen Darstellung“; Kap. 3.2.4 Z. 1261–1262).
Gelesen: alle 36 Altaufgaben. Urteil Lehrplan (Altbestand, Abgleich: „überwiegend in anderer Spalte“): Rechnen mit negativen Exponenten ist S14, aber schon in `9-binomische-formeln-vertieft` geübt; Funktionen \(x^{-n}\) (#7–#12, #23, #31, #33) sind Einführungsphase; #32 und #35 sind Antiproportionalität (Klasse 7/8). Der Ersatz schließt die laut Abgleich „große“ Lücke „iterative Modellierung, Überlagerung, begrenztes Wachstum, Grenze G“.
Verfahren: Ersatz – alle 36 Aufgaben neu. Dateiname und `THEMA_KEY` bleiben; Kommentar in Zeile 2 gesetzt; Stufen-Kommentare im Quelltext neu. Original gesichert im Scratchpad (`w10c/orig/`).
Titel (Empfehlung, nicht gesetzt – Parallelbetrieb): an allen drei Stellen „Begrenztes Wachstum & iterative Modelle“ (bisher „Potenzfunktionen (ganzz. Exp.)“); `<title>` dann mit `&amp;`.
Altaufgaben: Die Rechenaufgaben zu negativen Exponenten ziehen laut Auftrag nicht um. In `9-binomische-formeln-vertieft` gibt es zu folgenden Altaufgaben keine sinngleiche: #4 und #5 (Koeffizient vor einer Potenz mit negativem Exponenten: \(2x^{-1} = \frac{2}{x}\), \(\frac{5}{x^2} = 5x^{-2}\)), #15 (\((x^{-3})^2\) – Potenz einer Potenz mit negativem Exponenten), #17 (\((2x^{-1})^3\)), #21 (Fehlvorstellung \(x^{-2} = -x^2\) begründet zurückweisen), #25, #26, #28 (Potenzgleichungen \(x^{-2} = \frac19\), \(2x^{-1} = 8\), \(x^{-3} = -\frac{1}{27}\)), #29 (\((\frac{x^{-2}}{y^3})^{-1}\)), #36 (Begründung von \(a^0 = 1\) über die Divisionsregel – KC Z. 2424 „Rechengesetze exemplarisch begründen“). Sinngleich vorhanden sind #1–#3, #6 (dort #9), #13 (dort #11), #14 (dort #17), #16 und #30 (dort #16, fast dieselben Zahlen), #18 (dort #15), #19 (dort #10), #20 (dort #24; die Altaufgabe hatte zudem eine in sich widersprüchliche richtige Option), #22 und #34 (dort #23, #26), #24 und #27 (dort #13, #18, #25, #27).

Stufenaufbau (Plan Task 6, am KC geprüft – eine Abweichung): Stufe 1 ein Schritt einer rekursiven Vorschrift (linear, exponentiell, überlagert, „Anteil des Rests“), Grenze ablesen; Stufe 2 zwei bis drei Schritte, Zuwachs als Anteil des Rests; Stufe 3 Tabelle fortsetzen, Wachstumsart erkennen, iterativ gegen explizit – **dazu** (nicht im Plan, aber KC Z. 2385/2388) das Umschreiben zwischen den beiden Formen \(B(n-1) + w \cdot (G - B(n-1))\) und \(k \cdot B(n-1) + d\) (#17) und die Grenze durch Einsetzen (#18); Stufe 4 Modell aus Text (Abkühlung, Medikament, See, Akku), Grenze bestimmen, Umkehraufgaben; Stufe 5 Grenze aus drei Messwerten, Fehlersuche (Zuwachs zum Bestand statt zum Rest), Überlagerung (Sparplan, Einzahlung gesucht), Schwelle, explizite Darstellung; Stufe 6 Behauptung prüfen („nach genügend vielen Schritten genau 100“; „wer zurückzahlt, hat weniger Schulden“), Start über oder unter der Grenze, die Fälle mit \(k > 1\) (Kredit) und mit vier Werten für \(k\), Modellvergleich. Die „vier Fälle“ des KC sind verteilt: \(k < 1\), \(d > 0\) (fast alle), \(k > 1\), \(d < 0\) (#10, #30, #33), \(k > 1\), \(d > 0\) (#27, #30, #35), \(k = 1\) (#1, #30); Anfangswert über der Grenze in #3, #7, #11, #19, #32, #35.

| id | Stufe | Kriterium laut Rubrik | Inhalt | Anmerkung |
|---|---|---|---|---|
| 1–6 | 1 | ein Schritt, Objekt gegeben | je ein Schritt linear, exponentiell, \(0{,}5 \cdot B + 20\); Zuwachs als Anteil des Rests (#4); Grenze ablesen; Art benennen | Zahlen so, dass Fehlwege wie „Klammer vergessen“ nicht treffen (#3: erste Zahlen \(40\), \(+10\) → \(30 = 40 - 10\)). #1 und #2 sind die reinen Fälle \(k = 1\) und \(d = 0\) und der Form nach wie `10-wachstum-linear-exponentiell` #9 und #7 – als Einstieg in die Schreibweise belassen |
| 7–12 | 2 | Standardverfahren, zwei bis drei Schritte | \(k \cdot B + d\) fallend (#7), Anteil des Rests in Worten (#8) und als Vorschrift (#9, andere Zahlen als #8 und #15), Zuwachs im zweiten Schritt bei \(1{,}5 \cdot B - 20\) (#10), von oben auf die Grenze in Worten (#11), Zuwächse werden kleiner (#12) | nach dem Prüfdurchgang: #4 und #9 getauscht (der bloße Zuwachs ist Stufe 1, die Vorschrift mit zwei Schritten Stufe 2); #10 fragt den Zuwachs statt \(B(2)\) (war sinngleich mit #7); #11 neu (vorher dieselbe Zahlenfolge wie #14) |
| 13–18 | 3 | Zwischenergebnis, keine Formel im Text | Tabelle mit Lücke, Anteil selbst bestimmen (#13); \(0;\ 40;\ 60;\ 70;\ 75\) einordnen (#14); explizite Gleichung zuordnen (#15); Rest nach zwei Schritten (#16); Umschreiben in \(k \cdot B + d\), gefragt \(k\) (#17); Grenze durch Einsetzen (#18) | #14: Distraktor „Grenze 75“ ist falsch, weil der nächste Wert \(77{,}5\) ist; #15: Distraktor \(20 + 40 \cdot n\) stimmt bis \(n = 1\); #17: nach dem Nachtrag \(k\) statt \(d\) (\(d\) war das Produkt der beiden gegebenen Zahlen, ohne Umformen zu haben) |
| 19 | 4 | Modell aus Text | Abkühlung: Unterschied zum Raum sinkt um \(10\,\%\) je Minute | aus den beiden Schwestertrainern hierher (dort je #33); neue Zahlen; \(90 \cdot 0{,}9^3\) und der lineare Weg fallen. Schlusssatz des Lösungswegs nach dem Prüfdurchgang berichtigt (\(65{,}6\,{}^\circ\text{C}\) sind nicht „kälter als der Raum“; das wäre erst nach 15 Minuten so) |
| 20 | 4 | Modell aus Text | Medikament: täglich \(50\,\text{mg}\), \(40\,\%\) Abbau – Menge direkt nach der dritten Einnahme | Zeitpunkt ausgeschrieben, Beginn der Behandlung ausdrücklich („Von heute an“); „\(40\,\%\) bleiben“ (\(78\)) und „vierte Einnahme“ (\(108{,}8\)) fallen |
| 21 | 4 | Grenze bestimmen | See: \(20\,\%\) Verlust, \(300\) Fische Zusatz – bei welchem Bestand ergibt die Zählung jedes Jahr dieselbe Anzahl? | „Gezählt wird jeweils direkt nach dem Aussetzen“ nach dem Prüfdurchgang ergänzt: vor dem Aussetzen gezählt wäre \(1200\) ebenso richtig gewesen |
| 22 | 4 | Modell aus Text wählen | Akku: Vorschrift zu „\(5\,\%\) der fehlenden Ladung“ | drei Distraktoren = drei typische Verwechslungen (Anteil vom Bestand, fester Zuwachs, Rollen vertauscht) |
| 23 | 4 | Umkehraufgabe | Grenze aus dem Anteil und zwei aufeinanderfolgenden Werten | nach dem Prüfdurchgang umgekehrt: Die erste Fassung („Anteil aus \(G\), \(B(0)\), \(B(1)\)“) war der erste Teilschritt von #13 (Stufe 3) |
| 24 | 4 | Umkehraufgabe | \(d\) aus \(k\) und \(G\) | — |
| 25 | 5 | Parameter aus zwei Bedingungen | Grenze aus drei Messwerten | Faktor \(0{,}6\) statt \(0{,}5\) (sonst „letzter Wert plus letzter Zuwachs“) |
| 26 | 5 | Fehler im Rechenweg | Tim nimmt im zweiten Jahr \(10\,\%\) vom Bestand statt vom freien Platz | erster Schritt mit dem richtigen Rest, damit der Fehler erst im dritten Schritt liegt; Schritte kurz gefasst (Zeilenumbruch) |
| 27 | 5 | Parameter aus einer Bedingung (Überlagerung) | Sparplan: \(5\,\%\) Zinsen und gleichbleibende Einzahlung – Einzahlung aus dem Guthaben nach zwei Jahren (\(d = 400\)) | nach dem Prüfdurchgang Umkehraufgabe: Die erste Fassung (dreimal \(1{,}02 \cdot B + 500\) anwenden) war dieselbe Leistung wie #20. Nach dem Nachtrag \(5\,\%\) statt \(2\,\%\) und Toleranz 0,05: Mit \(2\,\%\) lag der Fehlweg „Startkapital ohne Zinseszins“ bei \(400{,}20\) und traf gerundet die Lösung; jetzt liegt er bei \(401{,}22\). „Erste Einzahlung unverzinst“ (\(410\)) und „erst einzahlen, dann Zinsen“ (\(380{,}95\)) fallen |
| 28 | 5 | zwei Verfahren | Schwelle: Bestand größer als \(400\) ⇔ Rest kleiner als \(100\) | nach 5 Schritten \(395{,}6\) – knapp, aber eindeutig |
| 29 | 5 | Parameter aus zwei Bedingungen | \(c\) in \(B(n) = G - c \cdot 0{,}5^n\) zur Vorschrift \(0{,}5 \cdot B + 40\) | Zusammenhang iterativ ↔ explizit (KC Z. 2391) |
| 30 | 5 | Verfahren wählen (vier Fälle) | Welche der vier Vorschriften hat eine Grenze? | \(1{,}1 \cdot B - 50\) hat zwar einen Bestand, der gleich bleibt (\(500\)), aber der Bestand läuft von ihm weg |
| 31 | 6 | Aussage prüfen | „Nach genügend vielen Schritten ist der Bestand genau \(100\).“ | Distraktoren je mit einer falschen Tatsache (Summe der Zuwächse erreicht 100; Rest nach 10 Schritten genau 0; Bestand über 100) |
| 32 | 6 | Fallunterscheidung | dieselbe Vorschrift, Start bei \(100\) und bei \(200\) | 2×2-Raster wächst/fällt |
| 33 | 6 | Fallunterscheidung, Aussage prüfen | Kredit: \(4\,\%\) Zinsen, \(2000\,€\) Rückzahlung; „wer zurückzahlt, hat jedes Jahr weniger Schulden“ gilt nur unter einer Schwelle – Restschuld nach zwei Jahren bei einer Summe \(10\,000\,€\) darunter | Fall \(k > 1\), \(d < 0\): Der Wert, der gleich bleibt, stößt ab. Nach dem Prüfdurchgang neu: Die erste Fassung fragte nur die Schwelle (eine Division, sinngleich mit #21) |
| 34 | 6 | Modellvergleich | exponentiell gegen begrenzt aus denselben zwei Werten, Unterschied bei \(B(2)\) | \(G = 300\) statt \(250\) (sonst Unterschied = erster Zuwachs) |
| 35 | 6 | Fallunterscheidung | \(B(n) = k \cdot B(n-1) + 30\), \(B(0) = 50\), vier Werte für \(k\): fällt, bleibt, wächst zur Grenze, wächst ohne Grenze – Grenze des einen passenden Falls | nach dem Prüfdurchgang neu: Die erste Fassung löste nur die Gleichbleib-Bedingung nach \(k\) auf (wie #24 nach \(d\)) |
| 36 | 6 | Modellvergleich | Schwimmbecken: lineare Rechnung überschreitet die Grenze – was liefert die begrenzte an diesem Tag? | zwei Stufen (Tag aus dem linearen Modell, Wert aus dem begrenzten) |

Nachrechnen (`rechne_bw.py`): 36 Aufgaben, 0 Fehler, kein offener Zufallstreffer. Beurteilt und stehen gelassen: #1, #2 (die Rechnung ist der verlangte Schritt), #5 (Ablesen der Grenze ist der Inhalt). #12 (allgemeine Aussage) ist an fünf Beispielfolgen geprüft, nicht bewiesen.
Zweiter Prüfdurchgang (alle 36): kein Fehler, 6 Mängel (#19 falscher Satz im Lösungsweg, #21 Zeitpunkt der Zählung, #23, #27, #33, #35 Stufe und Dopplung), Hinweise zu #1/#2, #4/#9, #7/#10, #8/#11, #14, #20, #34. Eingearbeitet: alle sechs Mängel (#23, #27, #33, #35 neu gefasst), dazu #4/#9, #10, #11, #17 (andere Zahlen als #5), #20. Nicht übernommen: #1/#2 ersetzen (der Plan verlangt auf Stufe 1 je einen linearen und einen exponentiellen Schritt), andere Zahlen für #14 (die Dopplung mit #11 ist durch die neue #11 weg), #34 herabstufen (Modellvergleich ist laut Plan Stufe 6; die gleich gebaute Aufgabe des Wachstums-Trainers ist ersetzt). Der Prüfer hat alle 26 Lösungswerte und die MC-Schlüssel bestätigt.
Nachtrags-Prüfer (hier #9, #10, #11, #17, #23, #27, #33, #35): kein Fehler, zwei leichte Mängel (#17 Zufallstreffer, #27 Toleranz), ein Hinweis (#9 Zahlen) – eingearbeitet. Danach von keinem Prüfer mehr gesehen: #27 mit \(5\,\%\) (eine lineare Gleichung; im Skript mit Bisektion und neun Fehlwegen nachgerechnet, im Bild angesehen).
Für den Autor: Der Trainer benutzt für die Grenze nur das Wort „Grenze“ (KC); „Sättigungsgrenze“ und „Schranke“ kommen nicht vor.
