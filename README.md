# Tarea 4.1 — Auditoría de modelos (en desarrollo)
Autor: Jorge Josué Flores González. Asistencia: Codex, declarada; no se atribuyen ejecuciones a Claude Code.

## Completado
Dos notebooks ejecutados con nombres originales; Skill v1 y refinamiento v2 en commits separados; informe de Iris y caso de prueba que reveló omisión de selección global de hiperparámetros. Biopsias: matriz [27,26;12,78] en orden maligno/benigno, exhaustividad 0.5094, precisión0.6923 y F1 0.5870. Iris: cinco clasificadores con mismos folds externos; KNN selecciona k en CV interna.

## Reproducir
Crear entorno Python, instalar requirements.txt y registrar un kernel con `python -m ipykernel install --user --name tarea41`. Ejecutar `AUDIT_KERNEL=tarea41 python ejecutar_notebooks.py`, o abrir en Colab y ejecutar todas las celdas. Límite60s por celda; no continuar indefinidamente ante fallos.
La Skill se invoca `/auditoria-modelos ruta`, ver .claude/skills/auditoria-modelos/README.md.

## Pendiente obligatorio
Descargar el original de biopsias desde el aula (la copia local contiene ediciones); obtener el tercer proyecto específico publicado por el profesor. Completar sus informes, repeticiones de estabilidad y prueba en cuarto proyecto, luego redactar bitácora1–2 páginas e informe APA2–3 páginas y publicar. No es todavía la entrega final.
