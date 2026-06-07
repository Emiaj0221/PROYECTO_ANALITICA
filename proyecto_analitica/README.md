# Segmentación Multidimensional de Consumidores Jóvenes 📊

Este repositorio contiene la Entrega 1 del proyecto integrador para el Diplomado en Desarrollo Web para Analítica de Datos. 

El objetivo principal es construir un modelo de aprendizaje automático no supervisado (Clustering) para segmentar a jóvenes adultos basándose en sus preferencias de entretenimiento, pasatiempos y personalidad. Esto permitirá a los equipos de Growth Marketing optimizar la asignación de presupuesto y la personalización de contenidos en campañas de cross-selling (venta cruzada).

## 📁 Estructura del Repositorio

El proyecto está organizado siguiendo las buenas prácticas de la industria para ciencia de datos:

* data/raw/: Contiene la materia prima del proyecto. Aquí se aloja el dataset original responses.csv (Young People Survey extraído de Kaggle).
* docs/: Documentación estratégica y visual del negocio.
  * ficha_proyecto.md: Formulación del problema, pregunta analítica, objetivos y métricas.
  * analisis_dataset.md: Análisis cualitativo, narrativo de los datos y auditoría de limitaciones metodológicas.
  * wireframe_dashboard.png: Boceto de la interfaz final propuesta para los tomadores de decisiones.
* notebooks/: Entornos de experimentación y código fuente.
  * 01_exploracion.ipynb: Código en Python/Pandas para el Análisis Exploratorio de Datos (EDA) inicial y generación de visualizaciones.
* requirements.txt: Listado explícito de dependencias y librerías de Python necesarias para ejecutar el modelo.
* .gitignore: Reglas para excluir archivos de caché y entornos virtuales del control de versiones.

## 🛠️ Instalación y Configuración (Para Evaluadores)

Para replicar este entorno de trabajo y ejecutar el código de los notebooks en una máquina local, sigue estos pasos:

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/proyecto_analitica.git](https://github.com/TU_USUARIO/proyecto_analitica.git)
   cd proyecto_analitica