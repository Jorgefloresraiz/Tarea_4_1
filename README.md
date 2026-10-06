# Tarea 4.1 Auditoría de modelos

Autor: Jorge Josué Flores González. MAI 540, Atlantis University.
Repositorio: https://github.com/Jorgefloresraiz/Tarea_4_1

## Entrega

- Informe_Tarea_4_1.docx y PDF: informe técnico de tres páginas.
- Bitacora_Tarea_4_1.docx y PDF: bitácora de dos páginas.
- .claude/skills/auditoria-modelos/SKILL.md: auditoría reutilizable, versión 3; README propio y verificador numérico.
- AUDIT_REPORT_biopsias_original.md, AUDIT_REPORT_iris.md, AUDIT_REPORT_insurance.md: tres auditorías principales.
- AUDIT_REPORT_wine_adicional.md: transferencia a un cuarto proyecto, revisión estática.
- App_Diagnostico_Biopsias_Mama.ipynb y App_Comparacion_Clasificadores_Iris.ipynb: clasificación actualizada y ejecutada.
- App_Auditoria_Insurance.ipynb: tercer caso construido con el dataset compartido del aula.
- evidencia/ y pruebas/: predicciones verificadas, estabilidad observada y seis pruebas automatizadas.

## Reproducción

Desde la carpeta del repositorio, con Python y un entorno virtual:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name auditoria41
AUDIT_KERNEL=auditoria41 python ejecutar_notebooks.py
AUDIT_KERNEL=auditoria41 python ejecutar_insurance.py
python -m unittest discover -s pruebas -v
```

Los notebooks de clasificación usan datasets de scikit-learn. Insurance usa datos/insurance.csv; en Colab, subir ese archivo y ajustar su ruta si es necesario. Los archivos ejecutores guardan resultados: trabajar en una copia si se desea conservar la evidencia entregada.

## Uso de la Skill

En Claude Code, desde este repositorio, solicitar auditar un notebook usando auditoria-modelos y proporcionar el archivo, objetivo, clase positiva, partición y subgrupos. La Skill exige evidencia y estados PASA, FALLA o NO SE PUEDE DETERMINAR; no modifica el proyecto auditado. El script numérico no sustituye la revisión de fuga causal, temporalidad o selección de hiperparámetros.

## Procedencia y límites

La asistencia realizada fue Codex, no Claude Code. Insurance se construyó para la auditoría y no se presenta como notebook suministrado por el profesor. El original de biopsias se recibió por correo y se conserva byte por byte en originales/; no se verificó descarga directa del aula. Su ejecución aislada falló por una referencia anticipada a una función. Se documentaron defectos mediante lectura del código, sin inventar métricas de ejecución.

Las repeticiones manuales conservaban contexto y no son pruebas ciegas. Los umbrales de subgrupos son exploratorios. Los modelos no están validados para decisiones clínicas. Esta entrega corresponde a la tarea 4.1; no completa la tarea 4.2.
