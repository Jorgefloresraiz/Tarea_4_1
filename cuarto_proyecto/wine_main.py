from pathlib import Path
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

DATA = Path(__file__).parent / "data" / "datos.csv"

df = pd.read_csv(DATA)

print("=" * 70)
print("WINE QUALITY: COMPARACIÓN ANTES vs. DESPUÉS")
print("=" * 70)

# ============================================================================
# MODELO ORIGINAL (ANTES) - 4 predictores
# ============================================================================
print("\n[ANTES] Modelo original con 4 predictores")
print("-" * 70)

features_antes = ['alcohol', 'volatile acidity', 'sulphates', 'density']
X_antes = df[features_antes]
y = df["quality"]

X_train_antes, X_test_antes, y_train_antes, y_test_antes = train_test_split(
    X_antes, y, test_size=0.25, random_state=42
)

modelo_antes = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("model", LinearRegression()),
])
modelo_antes.fit(X_train_antes, y_train_antes)
pred_antes = modelo_antes.predict(X_test_antes)

mae_antes = mean_absolute_error(y_test_antes, pred_antes)
rmse_antes = mean_squared_error(y_test_antes, pred_antes) ** 0.5
r2_antes = r2_score(y_test_antes, pred_antes)

print(f"Filas en dataset: {len(df):,}")
print(f"Predictores usados: {len(features_antes)}")
print(f"  {features_antes}")
print(f"\nMétricas de prueba (test_size=0.25, random_state=42):")
print(f"  MAE:  {mae_antes:.4f}")
print(f"  RMSE: {rmse_antes:.4f}")
print(f"  R²:   {r2_antes:.4f}")

# ============================================================================
# MODELO MEJORADO (DESPUÉS) - 10 predictores con ColumnTransformer
# ============================================================================
print("\n[DESPUÉS] Modelo mejorado con 10 predictores + ColumnTransformer")
print("-" * 70)

# Definir los 10 predictores exactos según README.md
numeric_features = [
    'alcohol', 'volatile acidity', 'sulphates', 'density',
    'residual sugar', 'chlorides', 'pH', 'fixed acidity', 'citric acid'
]
categorical_features = ['wine_type']

X_despues = df[numeric_features + categorical_features]

# train_test_split con los mismos parámetros
X_train_despues, X_test_despues, y_train_despues, y_test_despues = train_test_split(
    X_despues, y, test_size=0.25, random_state=42
)

# ColumnTransformer con dos ramas
preprocessor = ColumnTransformer(
    transformers=[
        ('numeric', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), numeric_features),
        ('categorical', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore'))
        ]), categorical_features)
    ]
)

# Pipeline completo
modelo_despues = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Ajustar solo con datos de entrenamiento
modelo_despues.fit(X_train_despues, y_train_despues)
pred_despues = modelo_despues.predict(X_test_despues)

mae_despues = mean_absolute_error(y_test_despues, pred_despues)
rmse_despues = mean_squared_error(y_test_despues, pred_despues) ** 0.5
r2_despues = r2_score(y_test_despues, pred_despues)

print(f"Filas en dataset: {len(df):,}")
print(f"Predictores usados: {len(numeric_features + categorical_features)}")
print(f"  Numéricos ({len(numeric_features)}): {numeric_features}")
print(f"  Categóricos (1): {categorical_features}")
print(f"\nPreprocessing:")
print(f"  • Numéricos: SimpleImputer(median) + StandardScaler")
print(f"  • Categóricos: SimpleImputer(most_frequent) + OneHotEncoder")
print(f"\nMétricas de prueba (test_size=0.25, random_state=42):")
print(f"  MAE:  {mae_despues:.4f}")
print(f"  RMSE: {rmse_despues:.4f}")
print(f"  R²:   {r2_despues:.4f}")

# ============================================================================
# COMPARACIÓN ANTES vs. DESPUÉS
# ============================================================================
print("\n" + "=" * 70)
print("COMPARACIÓN: ANTES vs. DESPUÉS")
print("=" * 70)

print(f"\n{'Métrica':<8} {'ANTES':>12} {'DESPUÉS':>12} {'Cambio':>12} {'% Cambio':>12}")
print("-" * 70)

delta_mae = mae_despues - mae_antes
pct_mae = (delta_mae / mae_antes) * 100 if mae_antes != 0 else 0
print(f"{'MAE':<8} {mae_antes:>12.4f} {mae_despues:>12.4f} {delta_mae:>+12.4f} {pct_mae:>+11.1f}%")

delta_rmse = rmse_despues - rmse_antes
pct_rmse = (delta_rmse / rmse_antes) * 100 if rmse_antes != 0 else 0
print(f"{'RMSE':<8} {rmse_antes:>12.4f} {rmse_despues:>12.4f} {delta_rmse:>+12.4f} {pct_rmse:>+11.1f}%")

delta_r2 = r2_despues - r2_antes
pct_r2 = (delta_r2 / r2_antes) * 100 if r2_antes != 0 else 0
print(f"{'R²':<8} {r2_antes:>12.4f} {r2_despues:>12.4f} {delta_r2:>+12.4f} {pct_r2:>+11.1f}%")

print(f"\n{'Predictores':<8} {len(features_antes):>12} {len(numeric_features + categorical_features):>12}")

print("\n" + "=" * 70)
