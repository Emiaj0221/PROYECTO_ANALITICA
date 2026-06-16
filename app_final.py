import streamlit as st
import pandas as pd
import joblib
import json
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Proyecto Integrador", layout="wide")

# --- CARGA DE RECURSOS ---
BASE = Path(__file__).parent

# Usamos caché para que no recargue los archivos en cada clic
@st.cache_resource
def cargar_modelos():
    modelo = joblib.load(BASE / "models" / "modelo_final.pkl")
    escalador = joblib.load(BASE / "models" / "escalador.pkl")
    return modelo, escalador

@st.cache_data
def cargar_datos():
    df = pd.read_csv(BASE / "data" / "processed" / "dataset_limpio.csv")
    with open(BASE / "models" / "model_metadata.json") as f:
        metadata = json.load(f)
    return df, metadata

try:
    modelo, escalador = cargar_modelos()
    df, metadata = cargar_datos()
except FileNotFoundError:
    st.error("Error: No se encontraron los archivos del modelo o los datos. Asegúrate de haber ejecutado los notebooks y scripts previos.")
    st.stop()

# --- NAVEGACIÓN ---
tab1, tab2 = st.tabs(["📊 Análisis Exploratorio", "🤖 Predicción con Modelo"])

# --- PESTAÑA 1: EDA ---
with tab1:
    st.header("Análisis Exploratorio del Dataset")
    
    # Filtro interactivo lateral
    st.sidebar.header("Filtros Globales")
    filtro_musica = st.sidebar.slider("Filtrar por afinidad general a la Música (1-5)", 1, 5, (1, 5))
    
    # Aplicar filtro
    df_filtrado = df[(df['Music'] >= filtro_musica[0]) & (df['Music'] <= filtro_musica[1])]
    
    st.write(f"Mostrando datos para usuarios con afinidad musical entre {filtro_musica[0]} y {filtro_musica[1]} ({len(df_filtrado)} registros).")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Distribución de gusto por el Baile (Dance)")
        fig1, ax1 = plt.subplots()
        sns.histplot(df_filtrado['Dance'], bins=5, kde=True, ax=ax1, color='#3498db')
        ax1.set_xlabel("Escala Likert (1-5)")
        st.pyplot(fig1)

    with col2:
        st.subheader("2. Matriz de Correlaciones")
        fig2, ax2 = plt.subplots()
        sns.heatmap(df_filtrado.corr(), annot=True, cmap='coolwarm', ax=ax2, fmt=".2f")
        st.pyplot(fig2)

    st.subheader("3. Dispersión: Folk vs Country")
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.scatterplot(data=df_filtrado, x='Folk', y='Country', alpha=0.5, color='#e74c3c', ax=ax3)
    # Pequeña variación de ruido visual (jitter) para que los puntos no se superpongan exactos
    sns.stripplot(data=df_filtrado, x='Folk', y='Country', color="black", alpha=0.2, jitter=0.2, ax=ax3)
    st.pyplot(fig3)

# --- PESTAÑA 2: PREDICCIÓN ---
with tab2:
    st.header("Clasificador de Perfiles")
    
    # Mostrar métricas leídas desde el JSON
    st.caption(f"**Modelo utilizado:** {metadata['modelo']} v{metadata['version']} | **{metadata['metrica_principal']}:** {metadata['valor_metrica']} | **Inercia:** {metadata['inercia']}")
    
    st.write("Ingresa las preferencias del usuario para clasificarlo en un clúster de mercado:")

    # Formulario de entrada
    with st.form("formulario_prediccion"):
        c1, c2, c3 = st.columns(3)
        with c1:
            val_music = st.slider("Afinidad por la Música (General)", 1, 5, 3)
            val_slow = st.slider("Canciones lentas o rápidas", 1, 5, 3)
        with c2:
            val_dance = st.slider("Gusto por el Baile (Dance)", 1, 5, 3)
            val_folk = st.slider("Música Folk", 1, 5, 3)
        with c3:
            val_country = st.slider("Música Country", 1, 5, 3)
            
        submit = st.form_submit_button("Generar Predicción", type="primary")

    # Lógica al presionar el botón
    if submit:
        # 1. Empaquetar los datos igual que en el entrenamiento
        datos_nuevos = pd.DataFrame([{
            'Music': val_music,
            'Slow songs or fast songs': val_slow,
            'Dance': val_dance,
            'Folk': val_folk,
            'Country': val_country
        }])
        
        # 2. Escalar los datos usando el objeto guardado (CRÍTICO)
        datos_escalados = escalador.transform(datos_nuevos)
        
        # 3. Predecir
        cluster_asignado = modelo.predict(datos_escalados)[0]
        
        # 4. Renderizar resultado en lenguaje claro
        st.success(f"🎯 El usuario ha sido clasificado exitosamente en el **Clúster {cluster_asignado}**.")
        st.write("**Interpretación Comercial:** Este perfil representa un segmento poblacional descubierto por el algoritmo K-Means basado en similitudes geométricas. Puedes usar este identificador para personalizar campañas de marketing dirigidas a este grupo específico.")

    st.divider()
    # Advertencia Ética Obligatoria
    st.info(
        "⚠️ **Aviso de Responsabilidad:** El resultado obtenido es una estimación probabilística generada por un modelo de Machine Learning. "
        "Debe ser interpretado como una herramienta de apoyo analítico y revisado por una persona responsable antes de tomar decisiones estratégicas definitivas."
    )