# Auditoría del archivo de biopsias recibido como original
Skill v3, aplicada por Codex el6 de octubre de2026. Entrada: originales/App_Diagnostico_Biopsias_Mama.ipynb. SHA256 `f1217ac90e48e5b702cb2b38bfd125924c94c340d68083d7e2f4eeb9f478a0d5`. Archivo recibido por el estudiante como material del profesor; no se verificó descarga directa del aula. Se conserva intacto; ejecución aislada guardada en evidencia/original_ejecucion.ipynb. Celdas numeradas desde1.

| Criterio | Resultado | Evidencia |
|---|---|---|
| M1 métricas reproducibles | NO SE PUEDE DETERMINAR | Celda11 se detiene con NameError al llamar construir_caracteristicas antes de su definición en13; no se alcanza entrenamiento. Ver evidencia/original_error.txt. |
| M2 métricas apropiadas | FALLA | Celda17 solo calcula accuracy; diagnóstico maligno0 es minoritario (212/569 en load_breast_cancer). Faltan precisión, recall y F1 para malignos. |
| P1 partición | FALLA | Celda17 usa semilla42 y prueba25%, pero no stratify=y. |
| P2 preprocesamiento aprendido | PASA | Celdas13 y17 no ajustan escaladores/imputadores globales; la característica es una división fila a fila. Esto no aprueba la validez numérica ni la fuga semántica. |
| P3 selección | NO SE PUEDE DETERMINAR | No se documenta cómo se seleccionaron predictores; max_iter5000 no demuestra búsqueda ni fuga por sí mismo. |
| F1 fuga | FALLA | Celda5 construye sesiones_tratamiento_programadas directamente de diagnostico; celda17 la incluye en X. Evidencia causal de fuga, no mera correlación. |
| S1 subgrupos | FALLA | num_biopsias_previas está disponible en celda5, pero17–19 reportan solo métricas globales. Su carácter sintético impide una conclusión de equidad clínica. |
| D1 independencia | NO SE PUEDE DETERMINAR | No existe comprobación de repetición de pacientes entre particiones. |
| Adicional orden de ejecución | FALLA | Celda11 usa función definida en13 y COLUMNAS_PREDICTORAS definida en17; el primer error impide continuar. |
| Adicional finitud | FALLA | Celda5 permite num_biopsias_previas=0; celda13 divide sin protección. Celda15 oculta no finitos solo en el histograma, no en datos de entrenamiento. |

## Qué detectó y qué omitió
Detectó fuga del objetivo, ausencia de estratificación, métricas insuficientes, falta de análisis por subgrupos, orden inválido y división por cero. Frente a los dos defectos conocidos de tarea3.1 (fuga y división por cero) detectó2/2; esto no mide exhaustividad general. No se identificó falso positivo confirmado en esos dos controles. El alcance de omisiones desconocidas no puede cuantificarse sin una referencia independiente exhaustiva.

## Acciones recomendadas
Reordenar definiciones; controlar denominador cero; excluir sesiones del modelo efectivo; estratificar; calcular métricas de malignos y soportes. Auditar una copia corregida separada, no modificar esta entrada. La versión corregida en la raíz del repositorio ya contiene la evaluación ampliada y es un artefacto distinto.
