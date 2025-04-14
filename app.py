import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

# ---------- CONFIG ----------
st.set_page_config(page_title="Juan Ignacio Algarin - Portfolio", layout="wide")

# ---------- NAVIGATION ----------
menu = st.radio("Navegación", ["Inicio", "Proyectos", "Clasificador", "Explorador", "Contacto"], horizontal=True)

# ---------- INICIO ----------
if menu == "Inicio":
    st.title("🚀 Juan Ignacio Algarin")
    st.subheader("Lic. en Ciencia de Datos (UNSAM) | Apasionado por los datos, la visualización y las APIs")

    st.success("""📢 *“"El objetivo de la analítica es convertir datos en información, y la información en conocimiento."
                        — Carly Fiorina, ex CEO de HP”*""")

    st.markdown("""
    Bienvenido a mi portfolio interactivo. Aquí encontrarás proyectos reales que exploran desde el análisis político con IA hasta dashboards de transporte público.
    Cada sección combina datos abiertos, Python y visualización para contar historias.
    """)

    # SOBRE MI
    st.header("👨‍💻 Sobre mí")
    st.markdown("""
    Soy Juan Ignacio Algarin, estudiante avanzado de Ciencia de Datos en la Universidad Nacional de San Martín (UNSAM).
    Me interesa especialmente el análisis de datos en contextos reales: elecciones, movilidad urbana, consumo masivo, etc. 
    Me gusta trabajar con APIs, visualizar datos con claridad y crear soluciones interactivas.
    """)

    # SKILLS
    st.header("🧰 Herramientas que manejo")
    st.markdown("""
    - 🐍 Python (Avanzado)  
    - 📊 Pandas, NumPy, Matplotlib, Seaborn  
    - 🔥 PySpark y Databricks  
    - 🧠 GPT & OpenAI APIs  
    - 📈 Power BI  
    - 🧮 SQL (PostgreSQL, SQLite)  
    - ☁️ Streamlit  
    - 📍 Plotly & Visualizaciones Interactivas
    """)

    # FORMACION
    st.header("🎓 Formación y Certificaciones")
    st.markdown("""
    - **Lic. en Ciencia de Datos - UNSAM** *(en curso)*  
    - Curso de Azure Fundamentals *(en proceso)*  
    - Certificación: Google Data Analytics *(en revisión)*  
    - Tableau Training - Maven Analytics *(free track)*  
    """)

    # CV
    try:
        with open("CV_Juan_Ignacio_Algarin.pdf", "rb") as cv_file:
            st.download_button("📄 Descargar mi CV", cv_file, file_name="CV_Juan_Ignacio_Algarin.pdf")
    except FileNotFoundError:
        st.warning("⚠️ CV no disponible en este entorno. Subilo al repositorio para activarlo.")

# ---------- PROYECTOS ----------
elif menu == "Proyectos":
    st.header("📊 Proyectos destacados")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🗳️ Análisis político en Reddit (2023)")
        st.markdown("""
        Exploración de +900 publicaciones de r/argentina con la API de Reddit. Se utilizó GPT para clasificar los temas y detectar menciones a políticos.
        Incluye gráficos interactivos y un análisis temporal del impacto mediático.
        """)
        st.markdown("[🔗 Ver notebook en GitHub](https://github.com/IgnacioAlgarin/reddit-politica-argentina-gpt)")

    with col2:
        image = Image.open("grafico_milei.png")
        st.image(image, caption="Menciones semanales a Milei (2017-2025)", use_container_width=True)

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🚌 Transporte público en Argentina (2024)")
        st.markdown("""
        Análisis de millones de transacciones SUBE para detectar patrones de movilidad. 
        Pipeline completo con PySpark en Databricks + dashboard en Power BI.
        """)
        st.markdown("[🔗 Ver proyecto en GitHub](https://github.com/IgnacioAlgarin/transporte-argentina-2024)")

    with col4:
        st.image("grafico_transporte.png", caption="Distribución de viajes por provincia", use_container_width=True)

    st.markdown("---")
    st.header("🚧 En desarrollo")
    st.markdown("""
    - 🔍 Análisis de consumo en supermercados
    - 📦 Exploración de APIs de música (Spotify)
    - 📡 Scraping de noticias + análisis con IA
    """)

# ---------- CLASIFICADOR ----------
elif menu == "Clasificador":
    st.header("🧠 Clasificador temático en vivo (próximamente)")
    st.info("¡Muy pronto vas a poder escribir tu propio título de Reddit y ver qué tema detecta una IA!")
    st.text_input("Escribí un título de Reddit...", disabled=True)

    st.markdown("---")
    st.header("📂 Clasificá tus propios datos (beta)")
    archivo = st.file_uploader("Subí un archivo CSV con una columna 'title'", type="csv")
    if archivo is not None:
        df = pd.read_csv(archivo)
        st.write("Primeras 5 filas del archivo:")
        st.dataframe(df.head())
        st.warning("🚧 La clasificación con GPT estará disponible próximamente.")

# ---------- EXPLORADOR ----------
elif menu == "Explorador":
    st.header("📈 Explorador interactivo de datos")
    try:
        df = pd.read_csv("viajes_provincia.csv")
        fig = px.bar(df, x="provincia", y="viajes", title="Cantidad de viajes por provincia", labels={"viajes": "Viajes", "provincia": "Provincia"})
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.warning("⚠️ Cargá el archivo 'viajes_provincia.csv' para activar esta sección.")

# ---------- CONTACTO ----------
elif menu == "Contacto":
    st.header("📬 Contacto")
    st.markdown("""
    **¿Querés que trabajemos juntos o tenés una propuesta?**
    
    Estoy siempre abierto a colaborar en proyectos que mezclen datos, creatividad y tecnología.  
    Ya sea para construir dashboards, automatizar procesos, explorar APIs o contar historias con gráficos... ¡contá conmigo!
    
    📩 Podés escribirme directamente por mail o contactarme por redes:  
    - ✉️ juanalgarin00@gmail.com  
    - 💼 [LinkedIn](https://www.linkedin.com/in/juan-ignacio-algarin-0167b018b/)  
    - 🐙 [GitHub](https://github.com/IgnacioAlgarin)

    ---

    🤝 *Actualmente busco mi primera experiencia formal en el mundo data.*  
    Estoy aprendiendo y creando todos los días, siempre con ganas de sumar valor desde el análisis.

    """)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Hecho con ❤️ en Argentina usando Python y Streamlit - © 2025 Juan Ignacio Algarin")
