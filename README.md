# 📊 Análisis comparativo de Criptomonedas y Activos Tradicionales (2020–2024)

Este proyecto integra Python , MySQL y Power BI para analizar la relación entre Bitcoin y activos tradicionales como oro , petróleo y el índice S&P500 , con el objetivo de evaluar su rendimiento, volatilidad y valoración durante el periodo 2020–2024.

🧠 Objetivo del proyecto
El propósito principal es comprender cómo se comportan las criptomonedas frente a activos financieros tradicionales bajo distintas condiciones de mercado.
El análisis busca responder preguntas claves como:

¿Bitcoin y Ethereum se comportan de forma similar?
¿Qué tan volátil es BTC en comparación con el oro o el S&P500?
¿Existe valoración entre las criptomonedas y los activos tradicionales?
💡 Sobre el proyecto y mi proceso de aprendizaje
Soy analista de datos en formación y este es mi primer proyecto completo de análisis de datos. Lo diseñado con el objetivo de poner en práctica las habilidades técnicas adquiridas en los últimos meses y mostrar cómo diferentes herramientas pueden integrarse en un flujo de trabajo profesional.

Este proyecto representa el inicio de mi camino en el análisis de datos aplicados a la economía y las finanzas.
Mi objetivo es continuar aprendiendo y desarrollando proyectos cada vez más completos, innovadores y orientados a la toma de decisiones basadas en datos.

## ⚙️ Tecnologías utilizadas

| Herramienta | Uso principal |
|--------------|----------------|
| 🐍 **Python (Pandas, yFinance, SQLAlchemy)** | Extracción y limpieza de datos |
| 🗄️ **MySQL** | Almacenamiento y modelado de datos históricos |
| 📊 **Power BI** | Visualización y análisis interactivo |
| 💻 **Yahoo Finance API (vía yfinance)** | Fuente de datos financieros reales |


## 🧩 Metodología

1. **Extracción de datos:**
Utilizamos las funciones de `yfinance` para descargar los precios históricos diarios de BTC, ETH, Oro, Petróleo y S&P500 desde 2020 hasta 2024.

2. **Limpieza y procesamiento (Python):**
- Cálculo de los rendimientos logarítmicos diarios.
- Medición de la volatilidad (desviación estándar móvil).
- Consolidación de la información en una base de datos relacional MySQL.

3. **Análisis en Power BI:**
- Creación de KPIs para el precio promedio y la volatilidad.
- Comparación de la volatilidad entre diferentes activos.
- Cálculo de las correlaciones entre BTC y otros activos.
- Un dashboard interactivo con filtros por activo.

## 📊 Resultados principales

- 🪙 **Bitcoin** muestra la mayor **volatilidad promedio** entre todos.
- 💡 **Ethereum** tiene una **alta correlación positiva** con Bitcoin.
- 🪔 **Oro** y **petróleo** presentan **comportamientos más estables**.
- 📈 El **S&P500** mantiene una **correlación baja o neutra** con BTC, lo que refleja su naturaleza como activo de riesgo.

## 🖼️ Vista del Dashboard

!Dashboard Power BI

> Un dashboard interactivo que incluye métricas clave, comparativas visuales y análisis de la correlación entre BTC y activos tradicionales.

## 📚 Fuente de datos

Los datos provienen de **Yahoo Finance**, obtenidos a través de la librería `yfinance`.
Período analizado: **1 de enero de 2020 – 1 de noviembre de 2024.**

## 💬 Conclusiones

Este proyecto ilustra cómo se pueden integrar herramientas de análisis de datos para extraer información económica y financiera valiosa:

- **Python** facilita la automatización y preparación de datos.
- **MySQL** permite estructurar y consultar la información de manera eficiente.
- **Power BI** ofrece visualización dinámica e interpretación ejecutiva.

> Este primer proyecto marca el inicio de una serie de análisis que seguiré desarrollando para fortalecer mis competencias como analista de datos.

## ✨ Autor

**Karolina Romero**  
📍 Economista | Analista de Datos en formación  
🔗 [LinkedIn](www.linkedin.com/in/karolinaromerolabarca)
📧 karolinaromero21@gmail.com

## 🗓️ Año
**2025**


#DataAnalytics #Python #PowerBI` #MySQL #Criptomonedas #EconomíaDigital #Portfolio
