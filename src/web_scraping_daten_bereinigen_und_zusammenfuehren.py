import pandas as pd
from pathlib import Path

# Pfad zum Ordner, in dem alle CSV-Dateien gespeichert sind
DIR_PATH = Path("./daten/web_scraping_daten")

# Liste der Jahre, die verarbeitet werden
years = ["2020", "2021", "2022", "2023", "2024"]

# Liste der Monate 
months = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
]

# Wandelt Temperatur von Fahrenheit in Celsius um und rundet auf ganze Zahlen
def temperature_change_f_to_c(temperature_f):
    temperature_c = (temperature_f - 32) * 5 / 9
    return round(temperature_c)

# Erstellt den vollständigen Dateipfad für einen Monat und ein Jahr
def build_file_path(month, year):
    file_name = f"{month}{year}.csv"
    return DIR_PATH / file_name

# Lädt eine Monatsdatei, bereitet die Daten auf und gibt ein DataFrame zurück
def load_and_prepare_month_df(month, year, missing_files):
    file_path = build_file_path(month, year)

    try:
        df_month = pd.read_csv(file_path)

        # Nur die relevanten Spalten auswählen
        df_month = df_month[["Day", "Temp_Max", "Temp_Avg", "Temp_Min"]]

        # Temperaturen von Fahrenheit in Celsius umrechnen
        df_month["Temp_Max_C"] = df_month["Temp_Max"].apply(temperature_change_f_to_c)
        df_month["Temp_Avg_C"] = df_month["Temp_Avg"].apply(temperature_change_f_to_c)
        df_month["Temp_Min_C"] = df_month["Temp_Min"].apply(temperature_change_f_to_c)

        # Datum aus Jahr, Monat und Tag erstellen, Nutze index,um Monat in nummerische Werte umzuwandeln
        df_month["Date"] = pd.to_datetime(
            {"year": year, "month":months.index(month)+1, "day": df_month["Day"]},
            errors="coerce"
        )

        # Entfernt Zeilen mit ungültigem oder fehlendem Datum
        df_month = df_month.dropna(subset=["Date"])      
           
        # Endgültiges Datenformat zurückgeben
        return df_month[["Date", "Temp_Max_C", "Temp_Avg_C", "Temp_Min_C"]]

    except FileNotFoundError:
        # Falls die Datei nicht existiert
        print(f"Datei nicht gefunden: {file_path}")
        missing_files.append(file_path)
        return None

    except Exception as error:
        # Falls ein anderer Fehler auftritt
        print(f"Problem mit der Datei {file_path}: {error}")
        return None

def main():
    all_data = []
    missing_files = []

    for year in years:
        for month in months:
            df_ready = load_and_prepare_month_df(month, year, missing_files)
            if df_ready is not None:
                all_data.append(df_ready)

    # Alle Monatsdaten zusammenführen und sortieren
    if all_data:
        df_all = pd.concat(all_data, ignore_index=True).sort_values("Date")
        print(df_all)
        df_all.to_csv("./daten/bereinigte_web_scraping_daten.csv", index=False)
    else:
        print("Keine Dateien wurden geladen.")

    # Fehlende Dateien anzeigen
    print("\nFehlende Dateien: ", end="")
    if not missing_files:
        print("Keine fehlenden Dateien")
    else:
        for f in missing_files:
            print(f)

if __name__ == "__main__":
    main()
