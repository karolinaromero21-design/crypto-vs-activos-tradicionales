# 📊 Análisis comparativo de Criptomonedas y Activos Tradicionales (2020–2024)

Este proyecto integra **Python**, **MySQL** y **Power BI** para analizar la relación entre **Bitcoin** y activos tradicionales como **oro**, **petróleo** y el **índice S&P500**, con el objetivo de evaluar su rendimiento, volatilidad y correlación durante el periodo 2020–2024.

---

## 🧠 Objetivo del proyecto

El propósito principal es comprender cómo se comportan las criptomonedas frente a activos financieros tradicionales bajo distintas condiciones de mercado.  
El análisis busca responder preguntas clave como:

- ¿Bitcoin y Ethereum se comportan de forma similar?
- ¿Qué tan volátil es BTC en comparación con el oro o el S&P500?
- ¿Existe correlación entre las criptomonedas y los activos tradicionales?

---

## 💡 Sobre el proyecto y mi proceso de aprendizaje

Soy analista de datos en formación y este es mi primer proyecto completo de análisis de datos.
Lo diseñé con el objetivo de poner en práctica las habilidades técnicas adquiridas en los últimos meses y mostrar cómo diferentes herramientas pueden integrarse en un flujo de trabajo profesional.  

Este proyecto representa el inicio de mi camino en el análisis de datos aplicados a la economía y las finanzas.  
Mi objetivo es continuar aprendiendo y desarrollando proyectos cada vez más completos, innovadores y orientados a la toma de decisiones basada en datos.

---

## ⚙️ Tecnologías utilizadas

| Herramienta | Uso principal |
|--------------|----------------|
| 🐍 **Python (Pandas, yFinance, SQLAlchemy)** | Extracción y limpieza de datos |
| 🗄️ **MySQL** | Almacenamiento y modelado de datos históricos |
| 📊 **Power BI** | Visualización y análisis interactivo |
| 💻 **Yahoo Finance API (vía yfinance)** | Fuente de datos financieros reales |

---

📁 crypto-vs-activos-tradicionales/
│
├── README.md
├── sql/
│   ├── create_tables.sql
│   └── queries.sql
│
├── python/
│   ├── rendimientos_volatilidad.py
│   └── correlaciones.py
│
├── powerbi/
│   └── dashboard.pbix
│
└── images/
    ├── dashboard_powerbi.png
    ├── grafico_volatilidad.png
    ├── grafico_rendimientos.png
    └── grafico_correlacion.png

---

## 🧩 Metodología

1. **Extracción de datos:**  
   Se utilizaron las funciones de `yfinance` para descargar precios históricos diarios de BTC, ETH, Oro, Petróleo y S&P500 entre 2020 y 2024.

2. **Limpieza y procesamiento (Python):**  
   - Cálculo de rendimientos logarítmicos diarios.  
   - Medición de volatilidad (desviación estándar móvil).  
   - Consolidación en una base de datos relacional MySQL.

3. **Análisis en Power BI:**  
   - Creación de KPIs de precio promedio y volatilidad.  
   - Comparación de volatilidad entre activos.  
   - Cálculo de correlaciones BTC vs. otros activos.  
   - Dashboard interactivo con filtros por activo.

---

## 📊 Resultados principales

- 🪙 **Bitcoin** presenta la mayor **volatilidad promedio** del conjunto.  
- 💡 **Ethereum** mantiene una **alta correlación positiva** con Bitcoin.  
- 🪔 **Oro** y **petróleo** muestran **comportamientos más estables**.  
- 📈 El **S&P500** mantiene una **correlación baja o neutra** con BTC, reflejando su naturaleza distinta como activo de riesgo.

---

## 🖼️ Vista del Dashboard

!Dashboard Power BI   

> Dashboard interactivo con métricas clave, comparativas visuales y análisis de correlación BTC vs activos tradicionales.

---

## 📚 Fuente de datos

Los datos provienen de **Yahoo Finance**, obtenidos mediante la librería `yfinance`.  
Período analizado: **1 enero 2020 – 1 noviembre 2024.**

---

## 💬 Conclusiones

Este proyecto demuestra cómo integrar herramientas de análisis de datos para obtener información económica y financiera valiosa:

- **Python** facilita la automatización y preparación de datos.  
- **MySQL** permite estructurar y consultar información de forma eficiente.  
- **Power BI** ofrece visualización dinámica e interpretación ejecutiva.

> Este primer proyecto marca el inicio de una serie de análisis que seguiré desarrollando para fortalecer mis competencias como analista de datos.

---

## ✨ Autor

**Karolina Romero**  
📍 Economista | Analista de Datos en formación  
🔗 [LinkedIn](www.linkedin.com/in/karolinaromerolabarca)
📧 karolinaromero21@gmail.com

---

## 🗓️ Año
**2025**


#DataAnalytics #Python #PowerBI` #MySQL #Criptomonedas #EconomíaDigital #Portfolio
