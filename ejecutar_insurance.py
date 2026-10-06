import os,nbformat
from pathlib import Path
from nbclient import NotebookClient
p=Path(__file__).parent
nb=nbformat.read(p/'App_Auditoria_Insurance.ipynb',as_version=4)
NotebookClient(nb,timeout=60,kernel_name=os.environ.get('AUDIT_KERNEL','python3'),resources={'metadata':{'path':str(p)}}).execute()
nbformat.write(nb,p/'App_Auditoria_Insurance.ipynb')
print('Insurance ejecutado',flush=True)
