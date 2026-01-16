# Analyse des Zusammenhangs zwischen Temperatur  
# und Verkehrsunfällen in Nashville (2020–2024)

Im Modul DIS08 Data Modeling an der Technischen Hochschule Köln wurde im Rahmen einer Gruppenarbeit ein datenbasierter Projekt umgesetzt. Ziel war die Durchführung einer vollständigen Datenanalyse von der Datensuche über die Datenaufbereitung bis hin zur Auswertung und Interpretation. Untersucht wurde der Zusammenhang zwischen den durchschnittlichen Temperaturbedingungen und Verkehrsunfällen in Nashville (USA) im Zeitraum von 2020 bis 2024, da die Stadt deutliche saisonale Temperaturunterschiede aufweist und geeignete öffentliche Daten verfügbar sind.

Das Thema wirkte besonders interessant, da es auf den ersten Blick so scheint, als käme es bei niedrigeren Temperaturen häufiger zu Verkehrsunfällen, beispielsweise aufgrund von Glatteis, Schnee und rutschigen Fahrbahnen. Darüber hinaus soll analysiert werden, ob sich aus den Unfallzahlen Rückschlüsse auf die Verkehrssicherheit ziehen lassen. Die Suche nach geeigneten Datensätzen erwies sich anfangs als herausfordernder als erwartet, da viele verfügbare Datenquellen bereits bereinigt waren oder nicht den gewünschten Anforderungen entsprachen.

Parallel zur Themenfindung wurden erste Anforderungen an das Projekt definiert, die sich an den Kursinhalten orientieren. Dazu zählen die Nutzung offener Datenquellen, die Anwendung von Web Scraping, eine strukturierte Datenbereinigung, die Zusammenführung mehrerer Datensätze sowie die Durchführung einer statistischen Analyse. Auf dieser Grundlage wurde ein Projektplan erstellt.

Die Relevanz dieses Themas liegt in der zunehmenden Nutzung von Daten zur Verbesserung der Verkehrssicherheit. Durch die Analyse des Zusammenhangs zwischen Temperatur und Unfallzahlen soll untersucht werden, ob sich risikoreiche Muster erkennen lassen. Zudem zeigt das Projekt, wie unterschiedliche Datenquellen sinnvoll zusammengeführt und analysiert werden können.

Analyse zur Unfallentwicklung: **Quelle:**  
https://pmc.ncbi.nlm.nih.gov/articles/PMC11952289



## Forschungsfrage und Hypothesen

Die zentrale Forschungsfrage dieses Projekts lautet:  
***Besteht in der Stadt Nashville (USA) ein Zusammenhang zwischen der täglichen Durchschnittstemperatur und der Anzahl der Verkehrsunfälle im Zeitraum von 2020 bis 2024?***

Die Alternativhypothese lautet:  
***H₁: Je niedriger die tägliche Durchschnittstemperatur, desto höher ist die Anzahl der Verkehrsunfälle.***

Die Nullhypothese lautet:  
***H₀: Es besteht kein Zusammenhang zwischen der täglichen Durchschnittstemperatur und der Anzahl der Verkehrsunfälle in der Stadt Nashville (USA) im Zeitraum von 2020 bis 2024.***

Diese Hypothesen werden mithilfe der ausgewählten Unfall- und Wetterdatensätze empirisch überprüft. Ziel der Analyse ist es, statistisch zu untersuchen, ob ein relevanter Zusammenhang zwischen der täglichen Durchschnittstemperatur und der Anzahl der Verkehrsunfälle vorliegt.


## 1.Rohdaten

### 1.1 Auswahl der Daten

Wie anfangs bereits erwähnt, stellte sich die Suche nach geeigneten Rohdaten als schwieriger heraus als erwartet. Viele der verfügbaren Datensätze waren bereits bereinigt oder passten nicht zu unserer Fragestellung. Da wir in unserem Projekt nicht nur Ergebnisse analysieren, sondern auch praktisch mit Rohdaten arbeiten wollten, war es uns wichtig, Datensätze zu verwenden, die noch nicht vollständig vorverarbeitet waren. Außerdem benötigten wir zwei unterschiedliche Datensätze, die sich über ein gemeinsames Merkmal miteinander verbinden lassen. Für unsere Fragestellung war das Datum entscheidend, da wir Unfallzahlen mit den jeweiligen Temperaturbedingungen eines Tages verknüpfen wollten. Deshalb entschieden wir uns für einen Unfall-Datensatz von Kaggle und für Wetterdaten von der Plattform Weather Underground.

Der Kaggle-Datensatz enthält für jeden Tag das Datum sowie die Anzahl der Verkehrsunfälle. Die Wetterdaten von Weather Underground liefern zu denselben Tagen Temperatur Informationen, insbesondere die maximale, minimale und durchschnittliche Temperatur. Dadurch eigneten sich beide Datensätze gut, um sie später zusammenzuführen und den Zusammenhang zwischen Temperatur und Unfallhäufigkeit zu untersuchen.

Allerdings lagen die Daten in unterschiedlichen Formaten vor. Die Datumsangaben waren nicht einheitlich, und die Temperaturwerte wurden im US-amerikanischen Maßsystem in Fahrenheit angegeben. Daher war eine umfangreiche Umformatierung und Datenbereinigung notwendig, bevor die Datensätze miteinander kombiniert werden konnten. Auch wenn dies zusätzlichen Aufwand bedeutete, erwies sich dieser Schritt als sehr sinnvoll, da wir zentrale Inhalte des Projekts wie Data Cleaning, Formatumwandlungen und das Mergen mehrerer Datensätze praktisch anwenden konnten.

**Link zu den Rohdaten:**  
https://www.kaggle.com/datasets/justinwilcher/nashville-accident-reports-jan-2018-apl-2025

### 1.2 Bereinigung der Rohdaten

Die Rohdaten beziehen sich auf Verkehrsunfälle in Nashville im Zeitraum von Januar 2018 bis April 2025. Bezüglich Datenbereinigung wurde für unsere Untersuchung relevanten Spalten ausgewählt:

- Accident Number  
- Date and Time  

Im zweiten Schritt wurde das Datumsformat vereinheitlicht und in ein festes Format überführt. Dies ist notwendig, um sicherzustellen, dass die Web-Scraping-Daten und die Rohdaten korrekt zusammengeführt (gemerged) werden können.

Anschließend wurden ausschließlich die Daten aus dem Zeitraum von 2020 bis 2024 berücksichtigt. Die Datumswerte innerhalb der Jahre wurden chronologisch sortiert, da sie auf der Kaggle-Datensatz nicht korrekt aufeinander folgend vorlagen. Darüber hinaus wurde die Uhrzeit aus Date and Time entfernt, da für das Projekt und die Hypothese das Datum relevant ist. Nach der Entfernung der Uhrzeit wurde der Name der Spalte von Date and Time in Date geändert. Die Unfälle pro Tag wurden aggregiert, sodass die Datenmenge in der CSV-Datei reduziert und sinnvoll für das weitere Mergen der Datensätze aufbereitet wurde. Für die Aggregation wurde die Funktion unique benutzt, da jeder Unfall eine eigene Id hat. Zusätzlich wurde geprüft, ob fehlende Daten vorhanden sind. Am Ende wurde die neue und bereinigte CSV-Datei gespeichert.



[Bearbeitung der Rohdaten](src/bearbeitete_rohedaten.py)


<br><br>
<img width="1170" height="512" alt="Bearbeitete_Rohdaten" src="https://github.com/user-attachments/assets/de72f0d5-7f46-42b4-b745-4bda9ce03aa5" />
<br><br>
Der Python-Code zur Verarbeitung der Rohdaten wurde im Terminal erfolgreich ausgeführt. Dabei wurde überprüft, ob fehlende Werte im Datensatz vorhanden sind. Die Ausgabe zeigte, dass weder im ursprünglichen Datensatz noch im Tagesdatensatz fehlende Daten enthalten sind.  
Anschließend wurden die Unfälle nach Datum zusammengefasst und als Übersicht ausgegeben. Zum Schluss wurde die bereinigte Datei als CSV gespeichert. Diese Datei wird in den nächsten Schritten für die weitere Verarbeitung und die Zusammenführung mit den Temperaturdaten verwendet.

[Unfalldaten pro Tag (2020–2024)](daten/nashville_accidents_daily_2020_2024.csv)



## 2. Web-Scraping

### 2.1 Auswahl der Web-Scraping-Daten (Nashville, USA)

Für die Analyse wurden die täglichen Wetterdaten für die Stadt Nashville (USA) im Zeitraum **01.01.2020 bis 31.12.2024** gesammelt. Diese Daten bilden die Grundlage der Web-Scraping-Daten für die spätere Untersuchung des Zusammenhangs zwischen Temperatur und Verkehrsunfällen.

Die Wetterdaten wurden von der Website **Weather Underground (Wunderground)** bezogen. Auf dieser Website wird für jeden Monat eine Tabelle mit dem Titel **„Daily Observations“** angezeigt, die alle verfügbaren täglichen Wetterparameter enthält.

**Beispiel-Link (Januar 2020):**  
https://www.wunderground.com/history/monthly/us/tn/nashville/KJWN/date/2020-1

Die Daten sind auf der Website monatlich organisiert, deswegen mussten für den Zeitraum von fünf Jahren (2020–2024) **60 Monatsseiten** (12 Monate × 5 Jahre) separat abgerufen werden.

Im Web-Scraping-Schritt wurde die gesamte Tabelle der jeweiligen Monatsseite heruntergeladen. Das bedeutet, dass alle angezeigten Wettervariablen (z. B. Temperatur, Luftfeuchtigkeit, Wind, Niederschlag usw.) zunächst gespeichert wurden. Die Auswahl der für die Analyse relevanten Variablen erfolgte nicht beim Download, sondern erst während der Datenbereinigung der Web-Scraping-Daten.

---

### 2.2 Herunterladen der Web-Scraping-Daten

Da die Wettertabelle auf der Webseite dynamisch mit JavaScript erzeugt wurde, wurde der HTML-Code der Tabelle manuell aus dem Browser kopiert. Der kopierte Code wurde anschließend im **Visual Studio Code** als HTML-Datei gespeichert, indem die Datei mit der Endung `.html` abgelegt wurde.

Nach dem Speichern konnte die Tabelle lokal im Browser korrekt angezeigt werden. Damit lag die Wettertabelle als statische HTML-Datei vor und konnte weiterverarbeitet werden. Dieser Vorgang wurde für alle Monate im Zeitraum von **2020 bis 2024** durchgeführt (insgesamt 60 Monate).

Das folgende Skript zeigt beispielhaft die Extraktion der Daten für einen Monat (Januar 2024). Dabei wurden die Bibliotheken **BeautifulSoup** zur Analyse der HTML-Dateien und **pandas** zur Strukturierung der Daten verwendet:

[web-scraping-daten-download](src/web_scraping_daten_download.py)

- Zuerst wurde die HTML-Datei eines Monats eingelesen und ausgewertet.  
- Anschließend wurde die Wettertabelle mit den monatlichen Wetterdaten identifiziert.  
- Aus der Tabelle wurden alle Variablen wie Temperatur, Taupunkt, Luftfeuchtigkeit, Wind, Luftdruck und Niederschlag extrahiert.  
- Für die Tabelle mit den Spalten **Maximum**, **Durchschnitt** und **Minimum** wurde eine separate Parser-Funktion verwendet.  
- Die extrahierten Tagesdaten eines Monats wurden in einem pandas DataFrame zusammengeführt und als CSV-Datei gespeichert.

Der oben gezeigte Prozess wurde für jeden Monat einzeln durchgeführt. So wurde für jede HTML-Datei eine passende CSV-Datei erstellt. Diese Struktur ermöglichte eine übersichtliche Weiterverarbeitung der Daten und bildete die Grundlage für die Bereinigung und Zusammenführung der Web-Scraping-Daten.

### 2.3. Anzeige der Web-Scraping-Daten

[web-scraping-daten-anzeigen](src/web_scraping_daten_anzeigen.py)

Zur Kontrolle der gesammelten Web-Scraping-Daten wurde ein Python-Skript zur Anzeige der Daten erstellt. Dabei wurden alle gespeicherten CSV-Dateien aus dem entsprechenden Ordner [web_scraping_daten](daten/web_scraping_daten) eingelesen.

Das Skript durchläuft systematisch alle Monate und Jahre im Zeitraum von **2020 bis 2024** und versucht, die jeweilige CSV-Datei zu laden.
Für jeden Monat und jedes Jahr werden die vorhandenen Wetterdaten im Terminal ausgegeben.
Vor der Ausgabe der jeweiligen Tabelle erscheint im Terminal eine Überschrift mit dem entsprechenden Monat und Jahr. 
Falls eine CSV-Datei nicht vorhanden ist, wird dies erkannt und die fehlende Datei protokolliert.

<img width="1422" height="141" alt="Screenshot 2026-01-15 123254" src="https://github.com/user-attachments/assets/e9959c37-cd22-46d9-9b75-60068f177339" />
<br><br>

<img width="1479" height="162" alt="Screenshot 2026-01-15 123152" src="https://github.com/user-attachments/assets/24890222-e580-41c1-92e3-81d9f447fe0a" />
<br><br>

<img width="1572" height="128" alt="Screenshot 2026-01-15 123023" src="https://github.com/user-attachments/assets/1f8619e7-5675-4ec9-92c6-d2088d57641a" />
<br><br>

Beim Ausführen des Skripts wurde im Terminal die Meldung **„Keine fehlenden Dateien“** ausgegeben. Dies bestätigt, dass alle erwarteten Monatsdateien für den gesamten Zeitraum vollständig vorliegen.
Dieser Schritt diente der Überprüfung der Vollständigkeit und Struktur der Web-Scraping-Daten und bildete die notwendige Grundlage, um im nächsten Schritt mit der **Datenbereinigung** beginnen zu können.

### 2.4 Bereinigung und Zusammenführung der Web-Scraping-Daten
[web_scraping_daten_bereinigen_und_zusammenfuehren](src/web_scraping_daten_bereinigen_und_zusammenfuehren.py)

Zur Bereinigung und Zusammenführung der Web-Scraping-Daten wurde ein Python-Skript verwendet, das alle monatlichen CSV-Dateien aus dem Zeitraum **2020–2024** aus dem Ordner [web_scraping_daten](daten/web_scraping_daten) einliest.

Für jeden Monat wurden zunächst nur die relevanten Temperaturspalten (Temp_Max, Temp_Avg und Temp_Min) sowie der Tag (Day) ausgewählt, um für die spätere Auswertung flexibel zu bleiben. Im Verlauf der Analyse zeigte sich jedoch, dass für unsere Fragestellung vor allem die durchschnittliche Temperatur relevant ist, weshalb in der endgültigen Auswertung Temp_Avg_C verwendet wurde.

Anschließend wurden die Temperaturwerte von **Fahrenheit** in **Celsius** umgerechnet und auf ganze Zahlen gerundet. Die Umrechnung erfolgte, da Celsius die in Europa übliche Temperatureinheit ist und eine bessere Vergleichbarkeit der Daten ermöglicht. Zudem erleichtert die Verwendung von Celsius die Interpretation der Ergebnisse in den späteren Analyse- und Modellierungsschritten.

Danach wurde aus **Jahr**, **Monat** und **Tag** ein Datumsfeld (**Date**) erstellt, um eine einheitliche Zeitstruktur für die weitere Analyse zu erhalten. Das einheitliche Datumsformat bildet die Grundlage für die spätere Zusammenführung der Temperaturdaten mit den Verkehrsunfalldaten. Zeilen mit ungültigem oder fehlendem Datum wurden entfernt, um eine saubere Zeitreihe zu erhalten.

Im nächsten Schritt wurden alle bereinigten Monatsdaten zu einem gemeinsamen Datensatz zusammengeführt und nach dem Datum sortiert. Der bereinigte Gesamtdatensatz wurde anschließend als CSV-Datei unter dem Namen **[bereinigte_web_scraping_daten.csv](daten/bereinigte_web_scraping_daten.csv)** gespeichert.

Zusätzlich wurde im Skript eine Fehlerbehandlung implementiert: Falls eine Monatsdatei nicht gefunden wird, wird dies erkannt und die entsprechende Datei protokolliert. Darüber hinaus werden auch andere mögliche Fehler beim Einlesen oder Verarbeiten der Dateien abgefangen und im Terminal ausgegeben. Dies ermöglicht eine transparente Kontrolle möglicher Probleme während der Datenverarbeitung.
<br><br>
<img width="1248" height="541" alt="Screenshot 2026-01-15 135006" src="https://github.com/user-attachments/assets/e4aa9c5d-8117-4d3f-9475-acc602d1c3bf" />
<br><br>
Nach dem Ausführen des Skripts wurde im Terminal eine Vorschau der bereinigten Daten angezeigt. Diese Vorschau zeigt die Spalten **Date** sowie die **maximale, durchschnittliche und minimale** Temperatur nach der Umrechnung in Celsius. Die Daten wurden chronologisch verarbeitet und ausgegeben.

Zudem wurde die erfolgreiche Speicherung der bereinigten Daten in einer einzelnen CSV-Datei bestätigt. Die Datei wurde unter dem Namen **[bereinigte_web_scraping_daten.csv](daten/bereinigte_web_scraping_daten.csv)** gespeichert. 

Die Meldung **„Keine fehlenden Dateien“** zeigt, dass alle erwarteten monatlichen Dateien vorhanden waren und erfolgreich verarbeitet wurden. Die Terminal-Ausgabe diente somit als Bestätigung für die erfolgreiche Datenbereinigung und Zusammenführung der Web-Scraping-Daten.

## 3. Zusammenführung der bereinigten Unfall- und Temperaturdaten

Zur Zusammenführung der bereinigten Rohdaten (Verkehrsunfälle) mit den bereinigten Web-Scraping-Daten (Temperaturdaten) wurde ein Python-Skript verwendet [merge](src/merge.py).

Nach dem Einlesen der beiden CSV-Dateien wurden die Datumsspalten in beiden Datensätzen erneut in ein einheitliches Datumsformat umgewandelt, da CSV-Dateien keine Datentypen speichern und Datumswerte beim Laden häufig als Text (String) interpretiert werden. Diese Vereinheitlichung ist notwendig, da die Zusammenführung der Daten auf Basis des Datums erfolgt.

Vor dem Merge wurde ein Vergleich der Datumswerte durchgeführt, um mögliche zeitliche Abweichungen zwischen den beiden Datensätzen zu identifizieren. Im nächsten Schritt wurden die beiden Datensätze mithilfe eines Inner Joins über das Datumsfeld zusammengeführt, sodass nur Tage in den finalen Datensatz übernommen wurden, für die sowohl Unfall- als auch Temperaturdaten vorlagen.

Nach dem Merge wurde der Datensatz chronologisch sortiert und es wurde geprüft, ob fehlende Werte vorhanden sind, um sicherzustellen, dass der zusammengeführte Datensatz vollständig und für die weitere Analyse geeignet ist.

Abschließend wurde der zusammengeführte Datensatz als CSV-Datei gespeichert und dient als Grundlage für die weitere Analyse des Zusammenhangs zwischen Temperatur und Unfallzahlen.
<br><br>
<img width="1547" height="846" alt="Screenshot 2026-01-15 140939" src="https://github.com/user-attachments/assets/fc293d8a-816d-4be4-aaa9-1d1d0dfe416f" />
<br><br>
Nach dem Ausführen des Merge-Skripts wurde im Terminal zunächst ein Vergleich der Datumswerte zwischen Unfalldaten und Temperaturdaten angezeigt. Dabei zeigte sich, dass ein Tag (08.11.2020) nur im Unfalldatensatz vorhanden war und in den Temperaturdaten fehlte. Zum Vergleich: https://www.wunderground.com/history/monthly/us/tn/nashville/KJWN/date/2020-11

Dieser Tag wurde beim anschließenden Inner Join automatisch ausgeschlossen. Da nur ein einzelner Tag von insgesamt über 1800 Tagen betroffen ist, hat dies keinen relevanten Einfluss auf die weitere Analyse.

Nach dem Merge wurde eine Überprüfung auf fehlende Werte durchgeführt. Die Ausgabe bestätigte, dass im zusammengeführten Datensatz keine fehlenden Werte vorhanden sind. Anschließend wurde die erfolgreiche Speicherung des gemergten Datensatzes als CSV-Datei  
**[merged_nashville_accidents_temperature_daily_2020_2024.csv](daten/merged_nashville_accidents_temperature_daily_2020_2024.csv)** bestätigt.

Zum Abschluss wurde im Terminal eine Vorschau des finalen Datensatzes angezeigt, die die täglichen Unfallzahlen sowie die zugehörigen Temperaturwerte enthält. Diese Vorschau bestätigt die korrekte Struktur sowie die chronologische Ordnung der zusammengeführten Daten.


## 4. Analyse der Daten und grafische Darstellung

Die zusammengeführten Daten (2020–2024) wurden analysiert und grafisch dargestellt, um den Zusammenhang zwischen der täglichen Durchschnittstemperatur und der Anzahl der Verkehrsunfälle zu untersuchen.  
Ziel war es zu prüfen, ob eine niedrigere Durchschnittstemperatur zu einer höheren Unfallanzahl führt.

---

### Schritte der Analyse
[ Zum Analysen Pythoncode](src/analyse.py)
[Zu den Diagrammen](diagramme)


Im ersten Schritt wurden die zusammengeführten Daten eingelesen und die relevanten Variablen (Temperatur (Avg)) und Unfallanzahl für die Analyse ausgewählt.  
Um die Analyse besser interpretieren zu können, wurden drei Diagramme erstellt.

---

### 1)

Das Streudiagramm visualisiert den Zusammenhang zwischen der täglichen Durchschnittstemperatur und der Anzahl der Verkehrsunfälle pro Tag in Nashville. Insgesamt liegen die meisten Werte in einem ähnlichen Bereich, während einzelne Tage deutlich höhere Unfallzahlen aufweisen und als Ausreißer („Outliers“) hervorgehoben sind. Die nahezu horizontale Regressionslinie deutet darauf hin, dass nur ein schwacher Zusammenhang zwischen niedrigen Temperaturen und einer erhöhten Unfallanzahl besteht.
<br><br>
<img width="1256" height="652" alt="diagramm_temp_unfaelle_outlier_alle_daten" src="https://github.com/user-attachments/assets/b8070340-e148-4e98-8793-2ad79aa290da" />
<br><br>


Der Korrelationskoeffizient wurde berechnet, um die Stärke des Zusammenhangs zu bestimmen.
<br><br>
![WhatsApp Image 2026-01-16 at 11 08 13](https://github.com/user-attachments/assets/fd8cf81d-101a-4f95-880a-affe97752b1b)
<br><br>


Der Korrelationskoeffizient liegt bei **r = -0,029 (mit Outlier)** bzw. **r = -0,001 (ohne Outlier)**. Dies deutet auf einen nicht relevanten Zusammenhang zwischen Temperatur und Unfallanzahl hin.

---

### 2)

Das Diagramm für alle Temperaturwerte zeigt, dass die beiden Regressionslinien (mit und ohne Outlier) nahezu identisch verlaufen und somit auf einen nicht relevanten Zusammenhang zwischen Temperatur und Unfallanzahl hindeuten.

<br><br>
<img width="1256" height="652" alt="diagramm_temp_unfaelle" src="https://github.com/user-attachments/assets/f82a4293-4b5b-47fe-96bb-b494ef1135ed" />
<br><br>


Nach dem Vergleich mit und ohne Outlier ergibt sich folgendes Ergebnis:  
Am Anfang zeigte sich mit Outliern ein schwacher Zusammenhang zwischen der durchschnittlichen Temperatur und der Unfallanzahl. Nach der Entfernung der Outlier ist jedoch kein relevanter Zusammenhang zwischen der durchschnittlichen Temperatur und der Unfallanzahl mehr erkennbar.

**Extrainfo:**  
**Unabhängige Variable (X):**  
Durchschnittstemperatur (Temp_Avg_C)  
→ die Temperatur ist der Einflussfaktor  

**Abhängige Variable (Y):**  
Anzahl der Verkehrsunfälle pro Tag (Accidents_Count)  
→ die Unfallanzahl ist das Ergebnis, das sich (eventuell) durch die Temperatur verändert  

Es wurde die Durchschnittstemperatur (Avg) verwendet, weil sie die Temperatur des ganzen Tages am besten widerspiegelt, während Max/Min nur Extremwerte sind und die Ergebnisse stärker verzerren können.  
Die Avg-Temperatur lag im niedrigsten bei −15 °C und im höchsten bei 33 °C.

---

### 3)

Das dritte Diagramm berücksichtigt ausschließlich Tage mit Temperaturen unter 0 °C, um den Zusammenhang zwischen sehr niedrigen Temperaturen und der Unfallanzahl gezielt zu untersuchen.
<br><br>
<img width="1256" height="652" alt="diagramm_entferne_fur_alle_temperaturdaten" src="https://github.com/user-attachments/assets/8385d091-5826-4d23-b39c-ee0095171567" />
<br><br>
<br><br>
![WhatsApp Image 2026-01-16 at 11 08 01](https://github.com/user-attachments/assets/bcf83d3c-44ba-49e6-8edc-e1a9b9a337d4)
<br><br>


Die Ergebnisse zeigen, dass entgegen der Erwartung bei niedrigeren Temperaturen nicht mehr Unfälle auftreten. Stattdessen weist die Analyse auf einen schwach positiven Zusammenhang hin (**r = 0,167 mit Outlier** bzw. **r = 0,19 ohne Outlier**). Auch der Temperatur-Effekt der linearen Regression ist positiv (**β1 = 1,321 mit Outlier** bzw. **β1 = 0,973 ohne Outlier**), was bedeutet, dass mit steigender Temperatur tendenziell mehr Unfälle beobachtet werden können.

---

## Diskussion der Ergebnisse

Ein möglicher Grund dafür, dass es mehr Unfälle bei höheren Temperaturen in dem Fall gibt, ist, dass bei niedrigen Temperaturen weniger Verkehr auf den Straßen stattfindet, da Menschen häufiger zuhause bleiben oder Fahrten vermeiden. Darüber hinaus kann es sein, dass Menschen bei niedrigen Temperaturen vorsichtiger fahren, während sie sich bei höheren Temperaturen sicherer fühlen und dadurch unaufmerksamer sind.

Letztendlich deuten die Daten aus Nashville (2020–2024) darauf hin, dass tendenziell gilt: **Je höher die durchschnittliche Temperatur, desto höher ist die Anzahl der Verkehrsunfälle (positiver Zusammenhang).**



