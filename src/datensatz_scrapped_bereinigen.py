import pandas as pd

def temperatur_wechseln_f_zu_c(temperatur_f):
    temperatur_c = (temperatur_f - 32) * 5 / 9
    return round(temperatur_c)


years = ["2020","2021","2022","2023","2024"]

# Monatsnamen müssen exakt zu alle Dateinamen passen (z.B. märz2020.csv)
months = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
]

# Monat -> Monatsnummer
month_map = {
    "Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6,
    "Juli": 7, "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12
}

all_data = []
missing_files = []

for year in years:
    for month in months:
        file_path = f"nashville_projekt/daten/{month}{year}.csv"

        try:
            df_temp = pd.read_csv(file_path)

            # nur wichtige Spalten
            df_temp = df_temp[["Day", "Temp_Max", "Temp_Avg", "Temp_Min"]]

            # Fahrenheit -> Celsius
            df_temp["Temp_Max_C"] = df_temp["Temp_Max"].apply(temperatur_wechseln_f_zu_c)
            df_temp["Temp_Avg_C"] = df_temp["Temp_Avg"].apply(temperatur_wechseln_f_zu_c)
            df_temp["Temp_Min_C"] = df_temp["Temp_Min"].apply(temperatur_wechseln_f_zu_c)

            # Datum erstellen (year + month + day)
            m_num = month_map[month]
            df_temp["Date"] = pd.to_datetime(
                {"year": year, "month": m_num, "day": df_temp["Day"]},
                errors="coerce"
            )

            # Endformat
            df_temp = df_temp[["Date", "Temp_Max_C", "Temp_Avg_C", "Temp_Min_C"]]
            all_data.append(df_temp)

        except FileNotFoundError:
            print(f"Datei nicht gefunden: {file_path}")
            missing_files.append(file_path)

        except Exception as e:
            print(f"Problem mit der Datei {file_path}: {e}")

# alles zusammenführen (nur wenn mindestens eine Datei geladen wurde)
if all_data:
    df_all = pd.concat(all_data, ignore_index=True).sort_values("Date")
    print(df_all)
else:
    print("Keine Dateien wurden geladen. Bitte Pfad/Dateinamen prüfen.")

# fehlende Dateien am Ende anzeigen
print("\nFehlende Dateien:")
if not missing_files:
    print("Keine fehlenden Dateien ")
else:
    for f in missing_files:
        print(f)
  