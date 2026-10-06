# Auditoría de Insurance
Skill v3; aplicación por Codex, 6 octubre 2026. Fuente: App_Auditoria_Insurance.ipynb, SHA256 `a39bacf64d0fa5b2e465f8766d8963d96c2228468d7de365fb120eb7b1a0f10f`. Celdas desde1. Proyecto construido con el dataset del aula por elección del estudiante; no se presenta como un notebook entregado por el profesor.

| Criterio | Resultado | Evidencia |
|---|---|---|
| R1 coherencia numérica | PASA | Celda4: RMSE5940.0272 y R²0.7959403 para lineal. Celda6 exporta predicciones. evidencia/insurance_numerica_1.json recalcula los valores desde335 casos; RMSE²=MSE. El R² negativo del Dummy es válido. |
| R2 interpretación y residuos | FALLA | Celda6 grafica bandas residuales y cola derecha, pero celda7 solo enumera límites generales: falta interpretar esos patrones observados y comparar explícitamente R² de entrenamiento/prueba. evidencia/insurance_numerica_1.json identifica3 predicciones negativas. Moneda/período no confirmados (celda1). FALLA por interpretación incompleta, no por exigir residuos perfectos. |
| P1 partición | PASA | Celda4: único train_test_split, test_size0.25 y random_state42, índices disjuntos; ambos modelos usan los mismos1002/335 casos. No corresponde estratificar un objetivo continuo. |
| P2 preprocesamiento | PASA | Celda4: imputadores, codificación y escalado dentro del Pipeline; fit sobre X_train únicamente. |
| P3 selección | PASA | Celda4: modelos y parámetros fijados, sin búsqueda en prueba. Comparación exploratoria; no se promete una estimación independiente posterior a elegir modelo. |
| F1 temporalidad | NO SE PUEDE DETERMINAR | Celdas3–4 excluyen charges de X; no hay variable derivada del objetivo. Celda3 declara que no existen fechas que demuestren disponibilidad previa de todas las variables. |
| S2 disparidad regional | PASA | Celda6: tamaños71–95; brechas relativas4.11%,6.19%,4.55%,19.38%, todas <=20%. Este umbral no certifica equidad y southwest queda cerca del límite. |
| D1 duplicados exactos | PASA | Celda2: se elimina1 fila idéntica antes de dividir;1337 filas finales. |
| D1 independencia por paciente | NO SE PUEDE DETERMINAR | Columnas del CSV y celda3: no hay identificador personal para verificar repetición de pacientes. |

## Hallazgos, omisiones y falsos positivos
Se detecta estructura residual y limitación de predicciones negativas. Se desconoce temporalidad y repetición por persona. La primera Skill no tenía reglas de regresión, por lo que omitía esta evaluación; v3 añade R1,R2,S2. No se dispone de una referencia completa independiente para asegurar ausencia de omisiones o falsos positivos.

## Acciones
Confirmar unidades y temporalidad; estudiar interacciones y restricciones de predicción en una fase posterior; mantener evaluación por región y ampliar a otros subgrupos predefinidos. No usar esta herramienta para decisiones de cobertura o atención. No se modifica el notebook auditado.
