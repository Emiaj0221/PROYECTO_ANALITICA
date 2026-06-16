# Reflexión Ética Final

El desarrollo e implementación de este modelo de segmentación basado en preferencias musicales conlleva responsabilidades éticas que deben ser documentadas y monitoreadas. A continuación, se detallan las consideraciones aplicadas al proyecto:

## 1. Riesgos identificados
* **Sesgo de Autoreporte:** Los datos provienen de encuestas donde los individuos evalúan sus propios gustos (escala Likert). Esto puede generar sesgos si los usuarios responden de acuerdo con la "deseabilidad social" (ej. afirmar que les gusta la música clásica para parecer cultos) en lugar de sus hábitos de escucha reales.
* **Reduccionismo:** Clasificar a una persona en un único clúster basándose en solo 5 variables musicales corre el riesgo de simplificar excesivamente la complejidad y fluidez de los gustos humanos.

## 2. Grupos o personas potencialmente afectados
* **Usuarios de nicho:** Las personas con gustos musicales muy diversos o atípicos (que no encajan claramente en los perfiles mayoritarios) podrían ser clasificados erróneamente en clústeres genéricos. Si este modelo se usara para recomendaciones comerciales, estos usuarios recibirían sugerencias irrelevantes o estereotipadas, afectando su experiencia de usuario.

## 3. Acciones de mitigación implementadas
* **Exclusión de variables sensibles:** El modelo de K-Means se entrenó estrictamente utilizando variables de preferencias musicales, excluyendo deliberadamente cualquier variable demográfica, de género, raza o nivel socioeconómico que pudiera generar discriminación algorítmica.
* **Transparencia en la interfaz:** Se incluyó una advertencia estática en el dashboard que informa al usuario sobre la naturaleza probabilística del modelo.

## 4. Limitaciones conocidas del sistema
* El modelo representa una "fotografía" en el tiempo (basada en el momento en que se recolectaron los datos) y no tiene la capacidad de adaptarse dinámicamente a la evolución de las tendencias musicales a menos que sea reentrenado.
* El algoritmo K-Means asume clústeres esféricos de tamaño similar, lo que matemáticamente podría no ser la representación perfecta de la distribución real de los gustos musicales.

## 5. Declaración explícita de uso
**Este sistema y los resultados de sus predicciones son estrictamente una herramienta de apoyo analítico. En ningún caso las clasificaciones generadas por el modelo constituyen una decisión automática, definitiva o vinculante. Cualquier acción comercial o estratégica derivada de este dashboard debe ser revisada y validada por una persona responsable.**