# Ficha de formulación del proyecto integrador

## 1. Datos del estudiante
- **Nombre completo:** [Escribe tu nombre aquí]
- **Programa:** Diplomado — Desarrollo Web para Analítica de Datos
- **Fecha:** [Escribe la fecha de entrega aquí]

## 2. Nombre del proyecto
Segmentación Multidimensional de Consumidores Jóvenes para Optimización de Campañas de Marketing Dirigido.

## 3. Planteamiento del problema
En el departamento de Growth Marketing de una plataforma de entretenimiento digital emergente, los analistas de campañas no cuentan con perfiles multidimensionales para ejecutar estrategias de venta cruzada (*cross-selling*) eficientes, lo que ocasiona un desperdicio del presupuesto publicitario en recomendaciones genéricas. El segmento de jóvenes adultos (15 a 30 años) representa un mercado de alto valor, pero es altamente heterogéneo. Utilizando enfoques unidimensionales (como segmentar solo por edad o un género musical favorito), se generan perfiles incompletos y bajas tasas de conversión. 

Para resolverlo, utilizando el dataset *Young People Survey* (1.010 registros, 150 variables), se construirá un modelo de aprendizaje automático que segmente a los usuarios descubriendo patrones ocultos en la intersección de su estilo de vida, pasatiempos, miedos y gustos culturales. Al perfilar estos clústeres, el equipo de campañas y los *Product Managers* podrán tomar la decisión directa de redirigir los presupuestos hacia nichos hiper-personalizados, maximizando el retorno de inversión y mejorando la experiencia del usuario final.

## 4. Pregunta analítica
¿Es posible identificar clústeres de comportamiento y estilo de vida a partir de las preferencias de entretenimiento, pasatiempos y rasgos de personalidad de los usuarios, con el fin de apoyar la personalización de contenidos y la asignación óptima de presupuesto en campañas de *cross-selling*?

## 5. Tipo de tarea y métrica de evaluación
- **Tipo de tarea:** [ ] Clasificación  [ ] Regresión  [x] Clustering
- **Métrica principal:** Coeficiente de Silueta (*Silhouette Score*) y WCSS (*Within-Cluster Sum of Squares*).
- **Justificación de la métrica:** Al ser un modelo no supervisado, carecemos de etiquetas previas de negocio, por lo que las métricas tradicionales (*Accuracy, F1-Score*) son inaplicables. El Coeficiente de Silueta es la métrica óptima porque evalúa la calidad matemática de los clústeres midiendo su cohesión interna (similitud de perfiles dentro del mismo grupo) y su separación externa (diferenciación frente a los otros grupos).

## 6. Descripción del dataset
- **Nombre:** Young People Survey
- **Fuente (URL):** https://www.kaggle.com/datasets/miroslavsabo/young-people-survey
- **Licencia:** CC0: Public Domain (Uso libre para fines académicos y de investigación).
- **Número de filas:** 1.010
- **Número de columnas:** 150
- **Descripción general:** Recopilación de respuestas de encuestas a jóvenes eslovacos (15-30 años) que captura un espectro amplio de su comportamiento mediante escalas ordinales tipo Likert (1-5) y variables categóricas. Documenta gustos musicales, cinematográficos, hábitos de consumo, fobias, demografía y rasgos psicológicos.

## 7. Variables
- **Variable objetivo (y):** No aplica nativamente (Clustering). La salida será una variable latente generada por el modelo (ej. `Cluster_ID`).
- **Variables de entrada principales (X):**
  - `Music / Movies`: Conjunto de escalas ordinales (1-5) que miden la afinidad por subgéneros de entretenimiento (ej. Rock, Terror), actuando como indicadores de consumo.
  - `Hobbies & interests`: Conjunto de 32 variables ordinales que describen en qué invierte su tiempo libre el usuario, definiendo su estilo de vida.
  - `Village - town` / `Gender`: Variables categóricas que aportan el contexto geográfico y demográfico base para cada encuestado.

## 8. Usuario final y decisión
- **Usuario:** Product Managers y Analistas de Campañas (Growth Marketing).
- **Decisión que apoyará:** Definir estratégicamente la distribución del presupuesto publicitario diario y determinar exactamente qué tipo de producto, evento o contenido se debe recomendar a cada segmento específico para maximizar la conversión (*cross-selling*).

## 9. Implicaciones éticas
- **Riesgo:** Sesgo de perfilamiento y exclusión algorítmica (*Digital Redlining*). Al cruzar variables de entorno habitacional (`Village - town`) con variables de gestión de recursos (`Finances`), el modelo podría crear clústeres que refuercen estereotipos, excluyendo de forma automatizada a jóvenes de zonas rurales o de menores recursos de campañas promocionales de alto valor.
- **Acción de mitigación:** Realizar auditorías de equidad (Fairness Audits) sobre los clústeres resultantes antes de lanzar campañas, verificando que la distribución demográfica dentro de los segmentos "premium" no excluya sistemáticamente a grupos minoritarios o rurales, y ajustar los pesos del algoritmo si se detecta un sesgo discriminatorio.

## 10. URL del repositorio GitHub
[https://github.com/Emiaj0221/PROYECTO_ANALITICA]