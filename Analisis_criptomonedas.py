
# ====================================================
# 🔹 PROYECTO: Análisis comparativo de Criptomonedas y Activos Tradicionales
# Herramientas: Python + MySQL + Power BI
# Autor: Karolina Romero
# ====================================================

# --- 1. Importar librerías ---
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine


# --- 2. Definir activos ---
tickers = ["BTC-USD", "ETH-USD", "GC=F", "CL=F", "^GSPC"]  # Bitcoin, Ethereum, Oro, Petróleo, S&P500

# --- 3. Descargar datos ---
print("📥 Descargando datos desde Yahoo Finance...")
data = yf.download(tickers, start="2020-01-01", end="2025-01-01")

# --- 4. Seleccionar precios ajustados ---
adj_close_cols = [col for col in data.columns if 'Adj Close' in col]

if not adj_close_cols:
    print("⚠️ No se encontraron columnas 'Adj Close'. Se usarán 'Close'.")
    adj_close_cols = [col for col in data.columns if 'Close' in col]

adj_close = data[adj_close_cols].dropna(how='all')
adj_close.columns = [col.replace('Adj Close_', '').replace('Close_', '') for col in adj_close.columns]

print("✅ Datos descargados y preparados.")
print(f"Columnas finales: {list(adj_close.columns)}")

# --- 5. Calcular métricas ---
returns = adj_close.pct_change().dropna()
returns.columns = [f"{c}_ret" for c in adj_close.columns]

volatility = returns.rolling(window=30).std() * np.sqrt(30)
volatility.columns = [f"{c}_vol" for c in adj_close.columns]


# ====================================================
# 🔹 SECCIÓN DE VISUALIZACIÓN
# ====================================================

# --- 6. Evolución de precios ---
plt.figure(figsize=(12,6))
for col in adj_close.columns:
    plt.plot(adj_close.index, adj_close[col], label=col)
plt.title("Evolución de precios (2020-2025)")
plt.xlabel("Fecha")
plt.ylabel("Precio (USD)")
plt.legend()
plt.tight_layout()
plt.show()

# --- 7. Volatilidad comparada ---
plt.figure(figsize=(12,6))
for col in volatility.columns:
    plt.plot(volatility.index, volatility[col], label=col.replace("_vol",""))
plt.title("Volatilidad móvil (30 días)")
plt.xlabel("Fecha")
plt.ylabel("Volatilidad mensual (%)")
plt.legend()
plt.tight_layout()
plt.show()

# --- 8. Correlación de rendimientos ---
corr = returns.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Correlación entre rendimientos")
plt.tight_layout()
plt.show()

# --- 9. Ranking de activos por riesgo y rendimiento ---
mean_returns = returns.mean() * 252
risk = returns.std() * np.sqrt(252)
summary = pd.DataFrame({"Rendimiento anual (%)": mean_returns*100,
                        "Volatilidad anual (%)": risk*100})

plt.figure(figsize=(8,6))
sns.scatterplot(x="Volatilidad anual (%)", y="Rendimiento anual (%)", data=summary)
for i, txt in enumerate(summary.index):
    plt.annotate(txt.replace("_ret",""), (summary["Volatilidad anual (%)"][i], summary["Rendimiento anual (%)"][i]))
plt.title("Riesgo vs. Rendimiento")
plt.tight_layout()
plt.show()

print("\n✅ Visualizaciones generadas con éxito.")
