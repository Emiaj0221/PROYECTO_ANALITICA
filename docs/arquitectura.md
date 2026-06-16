# Arquitectura del Sistema

Este documento describe la arquitectura técnica de la solución implementada para la segmentación de perfiles musicales, detallando sus componentes principales, las tecnologías utilizadas y el flujo de la información.

## 1. Componentes del Sistema y Tecnologías

El proyecto sigue una arquitectura monolítica orientada a datos, donde el procesamiento, el modelo analítico y la interfaz de usuario coexisten en el mismo entorno manejado por Python.

* **Capa de Datos:** * *Fuente:* Archivo original `responses.csv`.
    * *Procesamiento:* Transformación y limpieza ejecutada mediante `Pandas`, generando el artefacto `dataset_limpio.csv`.
* **Capa de Machine Learning (Motor Analítico):** * *Entrenamiento:* Script de Python local usando `scikit-learn` para el entrenamiento del algoritmo K-Means y `StandardScaler` para la normalización.
    * *Artefactos:* Modelos serializados en formato binario mediante la librería `joblib` (`modelo_final.pkl` y `escalador.pkl`).
* **Capa de Presentación (Interfaz de Usuario):** * *Dashboard:* Construido íntegramente con `Streamlit`. Permite la interacción en tiempo real sin necesidad de recargar la página.
    * *Visualización:* Gráficos generados de forma dinámica utilizando `matplotlib` y `seaborn`.

## 2. Flujo de Datos

El recorrido de la información desde su origen hasta la predicción final sigue este ciclo:

1.  **Ingesta y Limpieza (Offline):** Los datos crudos entran al notebook de exploración, donde se imputan los valores nulos. El resultado se exporta a la carpeta `data/processed/`.
2.  **Entrenamiento (Offline):** El script `entrenar_modelo.py` consume los datos procesados, realiza la separación (train/test), entrena el algoritmo K-Means y exporta los archivos `.pkl` a la carpeta `models/`, junto con un archivo `model_metadata.json` que contiene las métricas.
3.  **Inferencia (Online):** * El usuario interactúa con los controles deslizantes (*sliders*) en el dashboard de Streamlit.
    * La aplicación empaqueta las entradas en un *DataFrame* de Pandas.
    * Se aplica el `escalador.pkl` sobre estos datos nuevos para normalizarlos con la misma escala del entrenamiento original.
    * El `modelo_final.pkl` recibe los datos escalados, calcula la distancia geométrica hacia los centroides y retorna el número del clúster asignado.
    * La interfaz renderiza el resultado en lenguaje natural para el usuario final.

*(Nota: Si se cuenta con un diagrama visual creado en la Semana 1, este debe visualizarse a través del archivo `arquitectura.png` en esta misma carpeta).*
