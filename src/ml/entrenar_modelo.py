import pandas as pd
import json
import joblib
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split

# --- Configuración de rutas seguras ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / 'data' / 'processed' / 'dataset_limpio.csv'
MODEL_DIR = BASE_DIR / 'models'

# 1. Cargar datos
df = pd.read_csv(DATA_PATH)

# 2. Separar en train/test (Requisito de la rúbrica)
X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)

# 3. Escalar (Ajustar solo en train, aplicar en test para evitar fuga de datos)
escalador = StandardScaler()
X_train_scaled = escalador.fit_transform(X_train)
X_test_scaled = escalador.transform(X_test)

# 4. Entrenar el modelo final
modelo = KMeans(n_clusters=4, random_state=42, n_init='auto')
modelo.fit(X_train_scaled)

# 5. Evaluar en conjunto de prueba (Test)
predicciones_test = modelo.predict(X_test_scaled)
sil_score = silhouette_score(X_test_scaled, predicciones_test)
inercia = modelo.inertia_

# 6. Guardar artefactos (.pkl)
joblib.dump(modelo, MODEL_DIR / 'modelo_final.pkl')
joblib.dump(escalador, MODEL_DIR / 'escalador.pkl')

# 7. Generar JSON de metadatos exacto a la rúbrica
metadata = {
    "modelo": "KMeans",
    "version": "1.0",
    "fecha_entrenamiento": "2026-06-15",
    "metrica_principal": "silhouette_score",
    "valor_metrica": round(sil_score, 4),
    "inercia": round(inercia, 2),
    "variables_entrada": list(df.columns),
    "observaciones": "Entrenado con sklearn 1.3.2, semilla 42. Separación train/test aplicada sin fugas."
}

with open(MODEL_DIR / 'model_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=4)

print("¡Artefactos y JSON generados con éxito en la carpeta models/!")