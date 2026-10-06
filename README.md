# Tarea 4.1 — Auditoría de modelos (en desarrollo)
Autor: Jorge Josué Flores González. Asistencia: Codex, declarada; no se atribuyen ejecuciones a Claude Code.

## Completado
Dos notebooks ejecutados con nombres originales; Skill v1 y refinamiento v2 en commits separados; informe de Iris y caso de prueba que reveló omisión de selección global de hiperparámetros. Biopsias: matriz [27,26;12,78] en orden maligno/benigno, exhaustividad 0.5094, precisión0.6923 y F1 0.5870. Iris: cinco clasificadores con mismos folds externos; KNN selecciona k en CV interna.

## Reproducir
Crear entorno Python, instalar requirements.txt y registrar un kernel con `python -m ipykernel install --user --name tarea41`. Ejecutar `AUDIT_KERNEL=tarea41 python ejecutar_notebooks.py`, o abrir en Colab y ejecutar todas las celdas. Límite60s por celda; no continuar indefinidamente ante fallos.
La Skill se invoca `/auditoria-modelos ruta`, ver .claude/skills/auditoria-modelos/README.md.

## Tercer caso y prueba adicional
Insurance fue elegido por el estudiante entre los datasets compartidos del aula. App_Auditoria_Insurance.ipynb incluye datos en datos/insurance.csv, regresión lineal, referencia, predicciones y residuos. Ejecutar con `AUDIT_KERNEL=tarea41 python ejecutar_insurance.py`; en Colab subir insurance.csv cuando se solicite. AUDIT_REPORT_insurance.md documenta hallazgos sin corregir el notebook durante la auditoría. Wine es la prueba adicional de transferencia (revisión estática).

## Evidencia
En evidencia/ están las dos comprobaciones numéricas, las dos revisiones manuales de Insurance y el resultado de seis pruebas. Ver estabilidad.md para limitaciones: segunda lectura no ciega y sin ejecución de Claude Code. Skill v3 incluye regresión; los commits conservan refinamientos. No se cambiaron las tareas3.1/3.2 originales.

## Pendiente obligatorio
Solo falta el notebook original defectuoso descargado nuevamente desde tarea3.1 para su auditoría. Tras recibirlo se cerrarán los tres informes principales, el informe APA2–3 páginas y bitácora1–2 páginas, y la publicación. No es todavía la entrega final; no confundir Wine adicional con el caso original requerido.
