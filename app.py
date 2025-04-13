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

    st.success("""📢 *“Los datos son el nuevo petróleo, pero sin análisis, solo es lodo.”*""")

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

    # DETRÁS DE ESCENA
    st.header("🎬 Cómo fue construido este sitio")
    st.markdown("""
    Esta aplicación fue desarrollada con **Streamlit**, diseñada para ser simple, interactiva y didáctica.
    - Los gráficos usan `Plotly`, `Seaborn` o imágenes generadas en R.
    - La app corre desde un entorno virtual en Linux y está lista para deploy.
    - El código está versionado en GitHub, y podés consultarlo, clonarlo o proponer mejoras.
    """)

    # CV
    try:
        with open("CV_Juan_Ignacio_Algarin.pdf", "rb") as cv_file:
            st.download_button("📄 Descargar mi CV", cv_file, file_name="CV_Juan_Ignacio_Algarin.pdf")
    except FileNotFoundError:
        st.warning("⚠️ CV no disponible en este entorno. Subilo al repositorio para activarlo.")

# ---------- PROYECTOS ----------
# [RESTA DEL CÓDIGO SIN CAMBIOS...]
