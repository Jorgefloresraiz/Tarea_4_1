# Estabilidad observada
Insurance: dos lecturas manuales completas del SKILL.md v3 aplicadas al mismo notebook y en la misma conversación de Codex; los9 veredictos y el SHA256 coinciden. Ver insurance_revision_1.json e insurance_revision_2.json. Es una comprobación limitada: la segunda lectura no es ciega ni una sesión independiente de Claude Code. No se interpreta como garantía de estabilidad universal.

Componente numérico: dos procesos separados para cada CSV (Insurance y biopsias) producen JSON idénticos; hashes de entrada antes/después coinciden. Se guardan ambos archivos. Seis pruebas automáticas pasan: R² negativo, objetivo constante, clase positiva0, soporte insuficiente, disparidad y valores no finitos. No se equipara determinismo del script con estabilidad semántica completa.

Fallo/refinamiento: v1 omitía un criterio específico para elegir hiperparámetros antes de la CV externa; el caso pruebas/seleccion_global.py lo expuso en revisión manual y v2 agregó P3. v2 excluía regresión de su alcance; Insurance motivó v3 con R1/R2/S2, que verifica R² negativo válido y errores por región. No se inventaron ejecuciones de Claude ni prompts fallidos.
