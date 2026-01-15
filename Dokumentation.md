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


