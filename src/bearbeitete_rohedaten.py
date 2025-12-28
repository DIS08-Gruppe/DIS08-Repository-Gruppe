import pandas as pd
from pathlib import Path

csv_file = Path('.') / "daten" / "rohe_daten" / "Nashville Accidents Jan 2018 - Apl 2025.csv"

df = pd.read_csv(csv_file)

# Nur relevante Spalten
df = df[["Accident Number", "Date and Time"]]

# Datum konvertieren (festes Format)
df["Date"] = pd.to_datetime(
    df["Date and Time"],
    errors="coerce",
    format="%m/%d/%Y %I:%M:%S %p"
)

# Jahre 2020–2024 filtern
df = df[df["Date"].dt.year.between(2020, 2024)]

# Hier sortieren 
df = df.sort_values("Date").reset_index(drop=True)

# Uhrzeit entfernen → nur Datum
df["Date"] = df["Date"].dt.date

# Alte Spalte löschen
df = df.drop(columns=["Date and Time"])

# Prüfung auf fehlende Daten
if df.isna().any().any():
    print("Es gibt fehlende Daten im Datensatz.")
else:
    print("Es gibt KEINE fehlenden Daten im Datensatz.")

# Neue CSV speichern
output_path = Path('.')/ "daten" / "nashville_accidents_2020_2024.csv"
df.to_csv(output_path, index=False)

print("Datei gespeichert als:")
print(output_path)




