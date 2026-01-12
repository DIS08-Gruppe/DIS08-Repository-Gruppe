import os
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# Daten laden
df = pd.read_csv("daten/merged_nashville_accidents_temperature_daily_2020_2024.csv")

temp_col = "Temp_Avg_C"
acc_col = "Accidents_Count"

# Datentypen sicherstellen + fehlende entfernen
df[temp_col] = pd.to_numeric(df[temp_col], errors="coerce")
df[acc_col] = pd.to_numeric(df[acc_col], errors="coerce")
df = df.dropna(subset=[temp_col, acc_col])

df=df[df[temp_col] < 0]   # entferne für alle Temperaturdaten

print("Anzahl Tage (nach dropna):", len(df))
print(df[[temp_col, acc_col]].describe())

# Outlier-Analyse (IQR) – NUR für Unfälle
q1 = df[acc_col].quantile(0.25)
q3 = df[acc_col].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

df["Outlier_Unfaelle"] = (df[acc_col] < lower) | (df[acc_col] > upper)

print("\nOutlier-Grenzen (Unfälle):")
print(f"[{round(lower, 2)} , {round(upper, 2)}]")
print("Anzahl Outlier-Tage:", int(df["Outlier_Unfaelle"].sum()))

print("\nBeispiel-Outlier (erste 10):")
print(df.loc[df["Outlier_Unfaelle"], [temp_col, acc_col]].head(10))

# DataFrame ohne Outlier
df_no = df[df["Outlier_Unfaelle"] == False].copy()
print("\nAnzahl Tage ohne Outlier:", len(df_no))

# Korrelation + Regression (mit Outlier) 
r_all = np.corrcoef(df[temp_col], df[acc_col])[0, 1]
beta1_all, beta0_all = np.polyfit(df[temp_col], df[acc_col], 1)

print("\nKorrelationskoeffizient (mit Outlier) r =", round(r_all, 3))
print("Lineare Regression (mit Outlier)")
print("β0 (Intercept):", round(beta0_all, 3))
print("β1 (Temperatur-Effekt):", round(beta1_all, 3))

print("Interpretation (mit Outlier):")
if abs(r_all) < 0.1:
    print("Kein relevanter Zusammenhang zwischen Temperatur und Unfallanzahl(sehr schwache korrelation).")
elif beta1_all < 0:
    print("Höhere Temperatur → weniger Unfälle")
else:
    print("Höhere Temperatur → mehr Unfälle")

# Vergleich: ohne Outlier
r_no = np.corrcoef(df_no[temp_col], df_no[acc_col])[0, 1]
beta1_no, beta0_no = np.polyfit(df_no[temp_col], df_no[acc_col], 1)

print("\n--- Vergleich ohne Outlier ---")
print("Korrelationskoeffizient (ohne Outlier) r =", round(r_no, 3))
print("β0 (Intercept):", round(beta0_no, 3))
print("β1 (Temperatur-Effekt):", round(beta1_no, 3))


print("Interpretation (ohne Outlier):")
if abs(r_all) < 0.1:
    print("Kein relevanter Zusammenhang zwischen Temperatur und Unfallanzahl.")
elif beta1_all < 0:
    print("Höhere Temperatur → weniger Unfälle")
else:
    print("Höhere Temperatur → mehr Unfälle")

# Diagramm
print("\n[INFO] Erzeuge Diagramm...")

# Punkte ohne Outlier
fig = px.scatter(
    df_no,
    x=temp_col,
    y=acc_col,
    title="Nashville: Temperatur vs. Verkehrsunfälle (2020–2024)",
    labels={
        temp_col: "Durchschnittstemperatur (°C)",
        acc_col: "Anzahl Verkehrsunfälle pro Tag"
    },
    opacity=0.6
)

# Outlier-Punkte (grün)
fig.add_scatter(
    x=df.loc[df["Outlier_Unfaelle"], temp_col],
    y=df.loc[df["Outlier_Unfaelle"], acc_col],
    mode="markers",
    name="Outlier (Unfälle)",
    marker=dict(color="green", symbol="circle")
)

# Regressionslinie MIT Outlier (ROT)
x_vals = np.linspace(df[temp_col].min(), df[temp_col].max(), 100)
y_vals_all = beta0_all + beta1_all * x_vals

fig.add_scatter(
    x=x_vals,
    y=y_vals_all,
    mode="lines",
    name="Regression (mit Outlier)",
    line=dict(color="red", width=3)
)

# Regressionslinie OHNE Outlier (gestrichelt)
y_vals_no = beta0_no + beta1_no * x_vals
fig.add_scatter(
    x=x_vals,
    y=y_vals_no,
    mode="lines",
    name="Regression (ohne Outlier)",
    line=dict(dash="dash",color='black')
)

# Diagramm speichern
out_file = os.path.abspath("diagramm_temp_unfaelle_outlier.html")
fig.write_html(out_file)

print("[OK] Diagramm gespeichert:")
print(out_file)
print("[OK] Datei existiert:", os.path.exists(out_file))
