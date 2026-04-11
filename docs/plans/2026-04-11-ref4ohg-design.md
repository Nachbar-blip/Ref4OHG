# Ref4OHG — Design-Dokument

Stand: 2026-04-11

## Ziel

Neues GitHub-Repo `Ref4OHG` mit adaptiven Mathe-Trainern basierend auf dem
Kerncurriculum Mathematik Gymnasium Niedersachsen (G9, Kl. 7–13).
Fork der bestehenden DifferenzierungsEngine (Sachsen-Anhalt), angepasst an
den niedersaechsischen Lehrplan.

## Grundlage

- **KC Sek I:** `ma_gym_si_kc_druck.pdf` (Kl. 5–10, Doppeljahrgaenge 5/6, 7/8, 9/10)
- **KC Sek II:** `ma_go_kc_druck_2019 (1)_260411_231611.pdf` (Einfuehrungsphase + Qualifikationsphase, 2018)
- Beide PDFs liegen in `zzz_TOP/`

## Architektur

- Eigenes Repo, eigene Kopie von `spirale-engine.js`, `spirale.css`, `index.html`
- Identische Level-Namen: babyleicht, leicht, nervenschonend, mittel, anspruchsvoll, wagnerisch
- Identisches Aufgabenformat: MC + numerisch, 36 Aufgaben pro Trainer, 6 Level x 6
- GitHub Pages Deployment

## Strukturelle Unterschiede SA vs. NDS

| Aspekt | Sachsen-Anhalt (G8) | Niedersachsen (G9) |
|--------|--------------------|--------------------|
| Schuljahre | 12 | 13 |
| Pythagoras | Kl. 8 | Kl. 9 |
| LGS | Kl. 10 | Kl. 8 |
| Trigonometrie | Kl. 9 | Kl. 10 |
| Ableitung Einfuehrung | Kl. 11 | Kl. 10 (!) |
| Ganzrationale Funktionen | Kl. 11 | Kl. 10/11 |
| Statistik (Lagemasze) | — | Kl. 11 (Einfuehrungsphase) |
| Vektoren | Kl. 10 | Kl. 12 |
| Kursbezeichnung | GK/LK | gA/eA |
| Abiturjahr | Kl. 12 | Kl. 13 |

## Trainer-Mapping

### Kl. 7 (10 Trainer — 10 kopieren)

| NDS-Trainer | SA-Quelle |
|---|---|
| 7-rationale-zahlen | 7-rationale-zahlen |
| 7-prozent-grundlagen | 7-prozent-grundlagen |
| 7-prozent-anwendungen | 7-prozent-anwendungen |
| 7-terme | 7-terme |
| 7-gleichungen | 7-gleichungen |
| 7-dreiecke | 7-dreiecke |
| 7-kreise | 7-kreise |
| 7-koerper | 7-koerper |
| 7-zuordnungen-proportional | 7-zuordnungen-proportional |
| 7-wahrscheinlichkeit | 7-wahrscheinlichkeit |

### Kl. 8 (10 Trainer — 7 kopieren, 1 umsortieren, 1 anpassen, 1 neu)

| NDS-Trainer | SA-Quelle | Aktion |
|---|---|---|
| 8-terme-binomische-formeln | 8-terme-binomische-formeln | kopieren |
| 8-lineare-gleichungen | 8-lineare-gleichungen | kopieren |
| 8-lineare-funktionen-grundlagen | 8-lineare-funktionen-grundlagen | kopieren |
| 8-lineare-funktionen-anwendungen | 8-lineare-funktionen-anwendungen | kopieren |
| 8-aehnlichkeit-strahlensaetze | 8-aehnlichkeit | kopieren |
| 8-flaechen-volumina | 8-koerper | anpassen |
| 8-zufallsexperimente-mehrstufig | 8-zufallsversuche | kopieren |
| 8-lgs-zwei-variablen | 10-func-lgs-2 | umsortieren |
| 8-kreise-winkel | 8-kreise-winkel | kopieren |
| 8-gebrochen-rationale-einfuehrung | — | NEU |

### Kl. 9 (10 Trainer — 3 kopieren, 2 umsortieren, 3 anpassen, 2 neu)

| NDS-Trainer | SA-Quelle | Aktion |
|---|---|---|
| 9-reelle-zahlen-quadratwurzeln | 8-quadratwurzeln | umsortieren |
| 9-binomische-formeln-vertieft | 9-pot-gesetze | anpassen |
| 9-quadratische-funktionen | 9-func-quadratisch | kopieren |
| 9-quadratische-gleichungen | 9-func-quadrat-gleichungen | kopieren |
| 9-quadratische-anwendungen | 9-func-quadrat-anwendungen | kopieren |
| 9-pythagoras | 8-pythagoras | umsortieren |
| 9-strahlensaetze | 8-aehnlichkeit | anpassen |
| 9-daten-zufall-boxplot | 9-stoch-haeufigkeiten | anpassen |
| 9-potenzen-wurzeln | 9-pot-wurzeln-rational | kopieren |
| 9-raumgeometrie | — | NEU |

### Kl. 10 (12 Trainer — 3 kopieren, 4 umsortieren, 1 anpassen, 4 neu)

| NDS-Trainer | SA-Quelle | Aktion |
|---|---|---|
| 10-trig-rechtwinkliges-dreieck | 9-trig-rechtwinkliges-dreieck | umsortieren |
| 10-trig-anwendungen | 9-trig-anwendungen | umsortieren |
| 10-sinusfunktion | 10-trig-sinusfunktion | kopieren |
| 10-cos-tan-funktion | 10-trig-cos-tan-funktion | kopieren |
| 10-sin-cos-parameter | 10-trig-sin-cos-parameter | kopieren |
| 10-potenzen-ganzzahlig | 9-pot-ganzzahlige-exp | umsortieren |
| 10-potenzfunktionen | 9-pot-natuerliche-exp | umsortieren |
| 10-kreis-kugel | — | NEU |
| 10-ganzrationale-funktionen | — | NEU |
| 10-ableitung-einfuehrung | — | NEU |
| 10-wachstum-linear-exponentiell | 10-exp-wachstum-zerfall | anpassen |
| 10-trig-einheitskreis | 10-trig-einheitskreis | kopieren |

### Kl. 11 Einfuehrungsphase (12 Trainer — 7 kopieren, 1 anpassen, 4 neu)

| NDS-Trainer | SA-Quelle | Aktion |
|---|---|---|
| 11-statistik-lagemasse | — | NEU |
| 11-statistik-streumasse | — | NEU |
| 11-funktionen-potenzfunktionen | — | NEU |
| 11-funktionen-ganzrational | 9-func-gleich-hoehere-grade | anpassen |
| 11-ableitungsregeln | 11-analysis-ableitungsregeln | kopieren |
| 11-tangenten-normalen | 11-analysis-tangenten-normalen | kopieren |
| 11-monotonie-kruemmung | 11-analysis-monotonie-kruemmung | kopieren |
| 11-extrempunkte-wendepunkte | 11-analysis-extrempunkte-wendepunkte | kopieren |
| 11-extremwertaufgaben | 11-analysis-extremwertaufgaben | kopieren |
| 11-kurvendiskussion | 11-analysis-kurvendiskussion | kopieren |
| 11-grenzwerte | 11-analysis-grenzwerte | kopieren |
| 11-funktionsbegriff | 11-analysis-funktionsbegriff | kopieren |

### Kl. 12 gA Qualifikationsphase (14 Trainer — 10 kopieren, 2 umsortieren, 2 anpassen)

| NDS-Trainer | SA-Quelle | Aktion |
|---|---|---|
| 12-steckbriefaufgaben | 11-analysis-steckbriefaufgaben | umsortieren |
| 12-stammfunktionen | 12-analysis-stammfunktionen | kopieren |
| 12-bestimmtes-integral | 12-analysis-bestimmtes-integral | kopieren |
| 12-flaechenberechnung | 12-analysis-flaechenberechnung | kopieren |
| 12-e-funktion | 10-exp-funktionen | anpassen |
| 12-wachstum-begrenzt | 10-exp-wachstum-zerfall | anpassen |
| 12-vektoren-grundlagen | 12-geom-vektoren-wiederholung | kopieren |
| 12-geraden-raum | 12-geom-geraden | kopieren |
| 12-ebenen | 12-geom-ebenen | kopieren |
| 12-skalarprodukt | 10-vek-skalarprodukt | umsortieren |
| 12-stoch-bedingte-wahrscheinlichkeit | 12-stoch-bedingte-wahrscheinlichkeit | kopieren |
| 12-stoch-binomialverteilung | 12-stoch-binomialverteilung | kopieren |
| 12-stoch-grundlagen | 12-stoch-grundlagen | kopieren |
| 12-stoch-sigma-umgebungen | 12-stoch-sigma-umgebungen | kopieren |

### Kl. 13 eA (8 Trainer — 5 kopieren, 1 umsortieren, 1 zusammenfuehren, 1 neu)

| NDS-Trainer | SA-Quelle | Aktion |
|---|---|---|
| 13-eA-integralrechnung-vertieft | 12-lk-analysis-ln-substitution | kopieren |
| 13-eA-funktionenscharen | 11-lk-analysis-funktionsscharen | umsortieren |
| 13-eA-wachstumsmodelle | — | NEU |
| 13-eA-ebenen-lagebeziehungen | 12-lk-geom-ebene-ebene | kopieren |
| 13-eA-abstaende | 12-geom-abstaende | kopieren |
| 13-eA-normalverteilung | 12-lk-stoch-normalverteilung | kopieren |
| 13-eA-beurteilende-statistik | 12-lk-stoch-beurteilende-statistik | kopieren |
| 13-eA-tangenten-kreise | 12-lk-geom-tangenten + kreis-kreis | zusammenfuehren |

## Zusammenfassung

| Aktion | Anzahl Trainer | Aufgaben |
|--------|---------------|----------|
| Kopieren | 45 | 1.620 |
| Umsortieren | 10 | 360 |
| Anpassen | 8 | 288 (teilw. umschreiben) |
| Neu | 13 | 468 |
| **Gesamt** | **76** | **2.736** |

## Testinfrastruktur

Playwright-Testsuite aus DifferenzierungsEngine uebernehmen:
- `conftest.py`: BASE_URL und TRAINER_FILES anpassen
- `helpers.py`: BASE_URL anpassen
- `test_trainer.py`: 1:1 uebernehmen
- 6 Tests pro Trainer, 76 Trainer = 456 Tests

## Nicht im Scope

- Kl. 5/6 (wie beim Original — UX-Frage offen)
- Eigenes CSS-Theme (identisches Design)
- Eigene spirale-engine.js-Aenderungen (identische Logik)
