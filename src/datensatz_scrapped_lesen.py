import pandas as pd
from pathlib import Path 

years = ["2020","2021","2022","2023","2024"]

months = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
]

def print_header_month_year(month,year):
    print("\n" + "-" * 30)
    print(f"{month.upper()} {year}")
    print("-" * 30)

def print_df_for_month_year(month,year):  
        #nutze path lib: einheitliche dir Operationen
        file_name = f"{month}{year}.csv"   
        dir_path = Path("nashville_projekt/daten")
        #dir_path.mkdir(parents=True,exist_ok=True)
        file_path = dir_path /file_name
       
        print_header_month_year(month,year) 

        try:
            df = pd.read_csv(file_path)
            print(df)

        except FileNotFoundError as error:
            print(f"{month.upper()} {year}")
            print("Datei nicht gefunden")
            print(f"error:{error}")

for year in years:
    for month in months:
         print_df_for_month_year(month,year)