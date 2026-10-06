# Prueba de transferencia a un cuarto proyecto
Skill v3 aplicada por Codex a cuarto_proyecto/wine_main.py, copia inalterada del proyecto previo de Wine Quality; SHA256 `6494424397b1409cef6eacd7c8a09a45e7a1cecdef9c57b67657db6d82fe9594`. Revisión estática, sin ejecutar ni cambiar el proyecto original.

| Criterio | Resultado | Evidencia |
|---|---|---|
| R1 fórmula | PASA | Líneas40–42 y96–98 usan mean_squared_error**0.5 y r2_score sobre y_test y predicciones. |
| R1 valores reproducidos | NO SE PUEDE DETERMINAR | No se ejecutó esta prueba externa; no se incluyen predicciones de prueba. |
| R2 interpretación/residuos | FALLA | Líneas47–50,107–110 y119–132 imprimen métricas; no hay análisis de residuos, referencia trivial ni comparación R² entrenamiento/prueba en el archivo. |
| P1 partición | PASA | Líneas25–30 y59–69 seleccionan distintas columnas del mismo df con idéntico orden, tamaño0.25 y semilla42; objetivo quality común. Regresión, sin requisito de estratificar. |
| P2 ajuste | PASA | Líneas33–38 y73–94 contienen imputación/escala en Pipeline ajustado únicamente a X_train. |
| P3 selección | NO SE PUEDE DETERMINAR | Comentario línea58 remite a README para elegir predictores; no se audita aquí el proceso de selección previo. |
| F1 temporalidad | NO SE PUEDE DETERMINAR | Líneas25 y59–65 excluyen quality; no documentan cuándo se midieron las variables. |
| S2 subgrupos | FALLA | wine_type está disponible (línea63), pero líneas96–110 calculan solo métricas globales. Falta RMSE por tipo. |
| D1 duplicados | NO SE PUEDE DETERMINAR | Línea13 carga CSV; no consta control de duplicados ni identificadores en el archivo. |

Transferencia: la Skill se aplicó leyendo sus instrucciones; no fue necesario inventar un criterio para Wine. Se recomienda exportar predicciones, revisar duplicados y documentar unidades, residuos y RMSE por tipo. No se afirma ausencia de falsos positivos ni de omisiones sin referencia independiente. Esta prueba adicional no sustituye ninguno de los tres casos principales.
