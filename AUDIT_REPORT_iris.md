# Auditoría de Iris — Skill v2
Auditor: Codex, aplicación manual de SKILL.md. Fecha: 5 octubre 2026.
Entrada: App_Comparacion_Clasificadores_Iris.ipynb; SHA256 `6c3b55f5f64204d7b7ec0dd340361a6e555ba5b6ff6182128ff865e7ee1cadef`. Celdas numeradas desde 1. No se modificó el notebook durante esta revisión.

| Criterio | Resultado | Evidencia |
|---|---|---|
| M1 rango | PASA | Celda 29, salida de tabla: medias 0.94–0.9667 y desviaciones 0.0333–0.0554; pruebas de finitud y diez scores. |
| M1 consistencia con matriz | NO SE PUEDE DETERMINAR | Celdas 13 y 29: se guardan scores, no predicciones OOF ni matrices de cinco modelos. No confundir falta de matriz con inconsistencia demostrada. |
| M2 desbalance | PASA | Celda 5 carga Iris: 50 muestras por clase, ninguna supera 60%; accuracy es válida para comparación exploratoria balanceada. |
| M2 costo de errores | NO SE PUEDE DETERMINAR | No se aporta una función de costos del vivero; recomendación previa no demuestra equivalencia económica de errores. |
| P1 partición | PASA | Celda 13 crea diez folds estratificados con shuffle y semilla42 en cada llamada. Celdas 14 y 29 usan idénticos X,y; celda26 verifica índices reproducibles. |
| P2 preprocesamiento | PASA | Celda 29: StandardScaler dentro de Pipeline, este dentro de GridSearchCV evaluado por evaluar_con_cv. No se escala X globalmente. |
| P3 selección KNN | PASA | Celda 29: cinco folds internos eligen k dentro de cada fold externo; k final5 es reajuste y no puntuación de prueba independiente. |
| P3 selección árbol | FALLA | Celda18 compara profundidades en los folds de Iris; la recomendación previa y tabla reutilizan el mejor resultado de esa exploración sin evaluación externa nueva. Limitación declarada en celda 28; el resultado no es confirmatorio. |
| F1 fuga por variables | PASA | Celda5: iris.data contiene cuatro medidas de flores; iris.target es objetivo separado. Celda 29 recibe X,y separados. No se detecta predictor derivado del objetivo en este alcance. |
| S1 subgrupos | NO SE PUEDE DETERMINAR | Celda 28: no hay atributos de procedencia/demográficos. No se inventan grupos ni se usan especies como sustituto de equidad. |

## Resultados y límites
Detectado: sesgo de selección exploratoria del árbol, ausencia de matrices OOF y ausencia de subgrupos. KNN evita fuga mediante búsqueda anidada. No hay referencia independiente completa para medir todas las omisiones o falsos positivos; no se afirma cero errores. No se ejecutó Claude Code.

## Acciones
1. Para conclusiones confirmatorias, anidar también la selección de profundidad o usar datos externos intactos.
2. Conservar predicciones OOF para reconstruir matrices y métricas por clase.
3. Incorporar subgrupos reales relevantes cuando existan y aplicar umbral0.10 con soporte mínimo.
