import pandas as pd
from pathlib import Path

# Pfade definieren
ACCIDENTS_DAILY_PATH    = Path("./daten/nashville_accidents_daily_2020_2024.csv")
TEMPERATURE_DAILY_PATH  = Path("./daten/bereinigte_web_scraping_daten.csv")
OUT_PATH = Path("./daten/merged_nashville_accidents_temperature_daily_2020_2024.csv")

# Daten laden
df_accidents_daily    = pd.read_csv(ACCIDENTS_DAILY_PATH)
df_temperature_daily  = pd.read_csv(TEMPERATURE_DAILY_PATH)

# Datum vereinheitlichen
df_accidents_daily["Date"]   = pd.to_datetime(df_accidents_daily["Date"], errors="coerce").dt.date
df_temperature_daily["Date"] = pd.to_datetime(df_temperature_daily["Date"], errors="coerce").dt.date

# Vergleich der Datumswerte vor dem Merge (Welche Tage fehlen in welchem Datensatz?)(fehlende Tage prüfen)
missing_dates = df_temperature_daily[["Date"]].drop_duplicates().merge(
    df_accidents_daily[["Date"]].drop_duplicates(),
    on="Date",
    how="outer",
    indicator=True
)

dates_only_in_temperature = missing_dates[missing_dates["_merge"] == "left_only"]["Date"]
dates_only_in_accidents   = missing_dates[missing_dates["_merge"] == "right_only"]["Date"]

print()
print("* VERGLEICH DER DATUMSWERTE VOR DEM MERGE")
print(".........................................")

print("Tage nur im Temperatur-Datensatz (nicht in Unfällen):")
print(dates_only_in_temperature.to_string(index=False) if len(dates_only_in_temperature) else "Keine")

print("\nTage nur im Unfall-Datensatz (nicht in Temperaturdaten):")
print(dates_only_in_accidents.to_string(index=False) if len(dates_only_in_accidents) else "Keine")

# Merge (nur Tage mit vollständigen Unfall und Temperaturdaten behalten)
df_merged = pd.merge(df_accidents_daily, df_temperature_daily, on="Date", how="inner")

# chronologisch sortieren
df_merged = df_merged.sort_values("Date").reset_index(drop=True)

# Prüfung auf fehlende Werte nach dem Merge
print()
print("* PRÜFUNG AUF FEHLENDE WERTE NACH DEM MERGE")
print("...........................................")
print(df_merged.isna().sum()) 

if df_merged.isna().any().any():
    print("Ergebnis: Es gibt fehlende Werte im gemergten Datensatz")
else:
    print("Ergebnis: Keine fehlenden Werte im gemergten Datensatz.")

# Speichern
df_merged.to_csv(OUT_PATH, index=False)

print("\nMerge fertig! Gespeichert unter:")
print(OUT_PATH.resolve())

print("\nVorschau:")
print(df_merged)


