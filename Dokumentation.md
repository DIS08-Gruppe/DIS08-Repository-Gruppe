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


## Rohdaten

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



<img width="1170" height="512" alt="Bearbeitete_Rohdaten" src="https://github.com/user-attachments/assets/de72f0d5-7f46-42b4-b745-4bda9ce03aa5" />

Der Python-Code zur Verarbeitung der Rohdaten wurde im Terminal erfolgreich ausgeführt. Dabei wurde überprüft, ob fehlende Werte im Datensatz vorhanden sind. Die Ausgabe zeigte, dass weder im ursprünglichen Datensatz noch im Tagesdatensatz fehlende Daten enthalten sind.  
Anschließend wurden die Unfälle nach Datum zusammengefasst und als Übersicht ausgegeben. Zum Schluss wurde die bereinigte Datei als CSV gespeichert. Diese Datei wird in den nächsten Schritten für die weitere Verarbeitung und die Zusammenführung mit den Temperaturdaten verwendet.

[Unfalldaten pro Tag (2020–2024)](daten/nashville_accidents_daily_2020_2024.csv)

