from pathlib import Path
import os, nbformat
from nbclient import NotebookClient
p=Path(__file__).parent
for name in ['App_Diagnostico_Biopsias_Mama.ipynb','App_Comparacion_Clasificadores_Iris.ipynb']:
    nb=nbformat.read(p/name,as_version=4)
    NotebookClient(nb,timeout=60,kernel_name=os.environ.get('AUDIT_KERNEL','python3'),resources={'metadata':{'path':str(p)}}).execute()
    nbformat.write(nb,p/name)
    print(name,'OK',flush=True)
