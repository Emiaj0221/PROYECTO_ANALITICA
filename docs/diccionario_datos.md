# Diccionario de Datos

Este documento describe las variables finales utilizadas en el modelo de Machine Learning (K-Means) tras el proceso de limpieza y preparación, reflejando el estado del archivo `dataset_limpio.csv`.

Todas las variables de entrada corresponden a respuestas de una encuesta basadas en una escala Likert discreta del 1 al 5, donde 1 significa "No disfruto en absoluto" y 5 significa "Disfruto mucho".

| Variable | Tipo de Dato | Rol | Descripción |
| :--- | :--- | :--- | :--- |
| **Music** | Entero (1-5) | Característica (Entrada) | Nivel de afinidad general del usuario hacia la música. |
| **Slow songs or fast songs** | Entero (1-5) | Característica (Entrada) | Preferencia del usuario por canciones lentas (valores bajos) o rápidas (valores altos). |
| **Dance** | Entero (1-5) | Característica (Entrada) | Nivel de gusto o preferencia por la música de baile/electrónica. |
| **Folk** | Entero (1-5) | Característica (Entrada) | Nivel de gusto o preferencia por la música folclórica tradicional. |
| **Country** | Entero (1-5) | Característica (Entrada) | Nivel de gusto o preferencia por la música Country. |
| **Cluster_Asignado** | Entero (0-3) | Salida (Predicción) | Categoría o segmento generado por el algoritmo tras evaluar las características de entrada. |

**Nota de limpieza:** Los valores nulos encontrados en las características de entrada fueron imputados con el valor neutro `3` para preservar la estructura geométrica de los datos sin alterar drásticamente la distribución antes del escalado estándar.