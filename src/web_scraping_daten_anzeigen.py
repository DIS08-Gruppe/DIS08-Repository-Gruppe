import pandas as pd
from pathlib import Path 

# Pfad zum Ordner, in dem alle CSV-Dateien gespeichert sind 
DIR_PATH = Path("./daten/web_scraping_daten")

# Liste der Jahre, die verarbeitet werden
years = ["2020", "2021", "2022", "2023", "2024"]

# Liste der Monate, passend zu den Dateinamen 
months = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
]

# Gibt eine klare Überschrift für Monat und Jahr aus
def print_header_month_year(month, year):
    print("\n" + "-" * 30)
    print(f"{month.upper()} {year}")
    print("-" * 30)

# Liest die CSV-Datei für einen bestimmten Monat und ein bestimmtes Jahr 
def print_df_for_month_year(month, year, missing_files):  
    file_name = f"{month}{year}.csv"   
    file_path = DIR_PATH / file_name
       
    print_header_month_year(month, year) 

    try: 
        df = pd.read_csv(file_path)
        print(df)

    except FileNotFoundError as error:
        print("Datei nicht gefunden")
        print(f"error: {error}")
        missing_files.append(file_path)

missing_files = []

for year in years:
    for month in months:
        print_df_for_month_year(month, year, missing_files)
        
# Fehlende Dateien anzeigen
print("\nFehlende Dateien: ", end="")
if not missing_files:
    print("Keine fehlenden Dateien")
else:
    for f in missing_files:
        print(f)