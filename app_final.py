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
    df = pd.read_csv(BASE / "data" / "raw" / "responses.csv")
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

#   PESTAÑA 1: EDA ---
with tab1:
    st.header("Análisis Exploratorio de Preferencias y Estilo de Vida")
    
    # Diccionario para traducir las columnas a un español claro
    nombres_claros = {
        'Music': 'Música (General)',
        'Dance': 'Gusto por el Baile',
        'Folk': 'Música Folk',
        'Country': 'Música Country',
        'Pop': 'Música Pop',
        'Horror': 'Cine de Terror',
        'Art exhibitions': 'Interés en el Arte',
        'Finances': 'Ahorro / Finanzas',
        'Science and technology': 'Tecnología',
        'Socializing': 'Socialización'
    }
    
    # --- FILTROS LATERALES ORGANIZADOS POR TEMA ---
    st.sidebar.header("Filtros Globales")
    
    # Tema 1: Música
    st.sidebar.subheader("🎵 Tema: Música")
    filtro_musica = st.sidebar.slider("Afinidad General (1-5)", 1, 5, (1, 5))
    filtro_pop = st.sidebar.slider("Gusto por el Pop (1-5)", 1, 5, (1, 5))
    
    # Tema 2: Estilo de Vida
    st.sidebar.subheader("💡 Tema: Estilo de Vida")
    filtro_tec = st.sidebar.slider("Interés en Tecnología (1-5)", 1, 5, (1, 5))
    filtro_social = st.sidebar.slider("Nivel de Socialización (1-5)", 1, 5, (1, 5))
    
    # Aplicar los filtros de ambos temas simultáneamente
    df_filtrado = df[
        (df['Music'] >= filtro_musica[0]) & (df['Music'] <= filtro_musica[1]) &
        (df['Pop'] >= filtro_pop[0]) & (df['Pop'] <= filtro_pop[1]) &
        (df['Science and technology'] >= filtro_tec[0]) & (df['Science and technology'] <= filtro_tec[1]) &
        (df['Socializing'] >= filtro_social[0]) & (df['Socializing'] <= filtro_social[1])
    ].copy()
    
    # Renombrar columnas para la visualización de las gráficas
    df_visual = df_filtrado.rename(columns=nombres_claros)
    
    st.write(f"Mostrando **{len(df_visual)}** registros que cumplen con los criterios seleccionados.")

    # --- AQUÍ CONTINÚAN TUS COLUMNAS CON LOS GRÁFICOS (col1, col2...) ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Distribución de Gusto por el Baile")
        fig1, ax1 = plt.subplots()
        sns.histplot(df_visual['Gusto por el Baile'], bins=5, kde=True, ax=ax1, color='#3498db')
        ax1.set_xlabel("Escala de Preferencia (1 = Nada, 5 = Mucho)")
        ax1.set_ylabel("Cantidad de Personas")
        st.pyplot(fig1)

    with col2:
        st.subheader("2. Matriz de Correlaciones (Estilo de Vida)")
        # Seleccionamos una mezcla interesante de variables para que la matriz no se vea amontonada
        variables_matriz = ['Gusto por el Baile', 'Música Pop', 'Cine de Terror', 'Tecnología', 'Socialización', 'Ahorro / Finanzas']
        fig2, ax2 = plt.subplots()
        sns.heatmap(df_visual[variables_matriz].corr(), annot=True, cmap='coolwarm', ax=ax2, fmt=".2f", vmin=-1, vmax=1)
        st.pyplot(fig2)

    st.subheader("3. Relación: Interés en el Arte vs Ahorro / Finanzas")
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.scatterplot(data=df_visual, x='Interés en el Arte', y='Ahorro / Finanzas', alpha=0.5, color='#e74c3c', ax=ax3)
    # Ruido visual para separar los puntos solapados
    sns.stripplot(data=df_visual, x='Interés en el Arte', y='Ahorro / Finanzas', color="black", alpha=0.2, jitter=0.2, ax=ax3)
    ax3.set_xlabel("Nivel de Interés en el Arte")
    ax3.set_ylabel("Preocupación por el Ahorro / Finanzas")
    st.pyplot(fig3)



# --- PESTAÑA 2: PREDICCIÓN ---
with tab2:
    st.header("Clasificador Multidimensional de Perfiles")
    
    # Mostrar métricas leídas desde el JSON
    st.caption(f"**Modelo utilizado:** {metadata['modelo']} v{metadata['version']} | **{metadata['metrica_principal']}:** {metadata['valor_metrica']} | **Inercia:** {metadata['inercia']}")
    
    st.write("Ingresa las preferencias del usuario (escala del 1 al 5) para clasificarlo en un clúster de mercado:")

    # Formulario de entrada
    with st.form("formulario_prediccion"):
        st.subheader("🎵 Preferencias Musicales")
        c1, c2, c3 = st.columns(3)
        with c1:
            val_music = st.slider("Afinidad por la Música", 1, 5, 3)
            val_slow = st.slider("Canciones lentas o rápidas", 1, 5, 3)
        with c2:
            val_dance = st.slider("Gusto por el Baile", 1, 5, 3)
            val_folk = st.slider("Música Folk", 1, 5, 3)
        with c3:
            val_country = st.slider("Música Country", 1, 5, 3)
            val_pop = st.slider("Música Pop", 1, 5, 3)

        st.divider()

        st.subheader("💡 Estilo de Vida y Otros Intereses")
        c4, c5, c6 = st.columns(3)
        with c4:
            val_terror = st.slider("Cine de Terror", 1, 5, 3)
            val_arte = st.slider("Exhibiciones de Arte", 1, 5, 3)
        with c5:
            val_finanzas = st.slider("Gasto Financiero", 1, 5, 3)
            val_tec = st.slider("Tecnología", 1, 5, 3)
        with c6:
            val_social = st.slider("Socialización", 1, 5, 3)
            
        submit = st.form_submit_button("Generar Predicción", type="primary")

    # Lógica al presionar el botón
    if submit:
        # 1. Empaquetar los 11 datos EXACTAMENTE en el orden del entrenamiento
        datos_nuevos = pd.DataFrame([{
            'Music': val_music,
            'Slow songs or fast songs': val_slow,
            'Dance': val_dance,
            'Folk': val_folk,
            'Country': val_country,
            'Pop': val_pop,
            'Horror': val_terror,
            'Art exhibitions': val_arte,
            'Finances': val_finanzas,
            'Science and technology': val_tec,
            'Socializing': val_social
        }])
        
        # 2. Escalar los datos usando el objeto guardado (CRÍTICO)
        datos_escalados = escalador.transform(datos_nuevos)
        
        # 3. Predecir
        cluster_asignado = modelo.predict(datos_escalados)[0]
        
        # 4. Renderizar resultado en lenguaje claro
        st.success(f"🎯 El usuario ha sido clasificado exitosamente en el **Clúster {cluster_asignado}**.")
        
       
       # Textos dinámicos según el clúster (Extraídos de los centroides reales)
        if cluster_asignado == 0:
            st.write("**Interpretación Comercial: Segmento Ecléctico/Tradicional.** Tienen la mayor afinidad por géneros tradicionales (Folk/Country) y tecnología. Son un público excelente para festivales culturales y documentales.")
        elif cluster_asignado == 1:
            st.write("**Interpretación Comercial: Segmento Mainstream/Fiestero.** Amantes del Pop y el Baile, rechazan la música tradicional. Tienen la mayor vida social. Público objetivo perfecto para discotecas, conciertos masivos y tendencias virales.")
        elif cluster_asignado == 2:
            st.write("**Interpretación Comercial: Segmento Alternativo.** Aman la música en general, pero puntúan muy bajo en Baile, Pop y Country. Suelen consumir géneros de nicho (Rock/Indie). Ideales para productos culturales no convencionales.")
        else:
            st.write("**Interpretación Comercial: Segmento Pragmático/Indiferente.** Su interés por la música es el más bajo de todos los grupos. Sin embargo, tienen la mayor preocupación por el Ahorro y las Finanzas. No invertir recursos de entretenimiento musical en ellos.")

    st.divider()
    # Advertencia Ética Obligatoria
    st.info(
        "⚠️ **Aviso de Responsabilidad:** El resultado obtenido es una estimación probabilística generada por un modelo de Machine Learning. "
        "Debe ser interpretado como una herramienta de apoyo analítico y revisado por una persona responsable antes de tomar decisiones estratégicas definitivas."
    )