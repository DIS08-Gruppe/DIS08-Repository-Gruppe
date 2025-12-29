import pandas as pd
from pathlib import Path 
from bs4 import BeautifulSoup

# Projekt-Hinweis:
# Jedes Gruppenmitglied hat die Daten jeweils monatsweise für ein Jahr gesammelt.
# Am Ende wurden alle Monatsdateien zusammengeführt.

# HTML laden
path = r"./daten/web_scraping_daten/Januar2024.html"
with open(path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# Haupttabelle finden (enthält die Monatsübersicht)
main = soup.find("table", {"class": "days"})

# Alle inneren Tabellen extrahieren (Tage, Temperatur, Taupunkt, Luftfeuchte, Wind, Druck, Niederschlag)
inner_tables = main.find_all("table")

# Erste Tabelle: Tage (erste Zelle ist i.d.R. nur ein Label, daher [1:])
days = [row.get_text(strip=True) for row in inner_tables[0].find_all("td")][1:]

# Parser für 3-Spalten Tabellen (Max/Avg/Min)
def parse_three_col(table):
    # Erste Zeile ist der Header, daher ab Zeile 2 lesen
    rows = table.find_all("tr")[1:]
    maxv, avgv, minv = [], [], []
    for r in rows:
        tds = [c.get_text(strip=True) for c in r.find_all("td")]
        maxv.append(tds[0])
        avgv.append(tds[1])
        minv.append(tds[2])
    return maxv, avgv, minv

# Spalten extrahieren (Reihenfolge entspricht der Struktur in der HTML-Datei)
temp_max, temp_avg, temp_min = parse_three_col(inner_tables[1])
dew_max, dew_avg, dew_min = parse_three_col(inner_tables[2])
hum_max, hum_avg, hum_min = parse_three_col(inner_tables[3])
wind_max, wind_avg, wind_min = parse_three_col(inner_tables[4])
pres_max, pres_avg, pres_min = parse_three_col(inner_tables[5])

# Niederschlag (einspaltig, erste Zelle ist i.d.R. nur ein Label, daher [1:])
precip = [row.get_text(strip=True) for row in inner_tables[6].find_all("td")][1:]

# DataFrame bauen
df = pd.DataFrame({
    "Day": days,
    "Temp_Max": temp_max,
    "Temp_Avg": temp_avg,
    "Temp_Min": temp_min,
    "Dew_Max": dew_max,
    "Dew_Avg": dew_avg,
    "Dew_Min": dew_min,
    "Humidity_Max": hum_max,
    "Humidity_Avg": hum_avg,
    "Humidity_Min": hum_min,
    "Wind_Max": wind_max,
    "Wind_Avg": wind_avg,
    "Wind_Min": wind_min,
    "Pressure_Max": pres_max,
    "Pressure_Avg": pres_avg,
    "Pressure_Min": pres_min,
    "Precip_Total": precip
})

# CSV speichern
df.to_csv(r"./daten/web_scraping_daten/Januar2024.csv", index=False)

# Kurzer Check der ersten Zeilen
df.head()
