import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'.claude/skills/auditoria-modelos/scripts'))
from auditar_predicciones import regresion,clasificacion,auditar
class AuditoriaTests(unittest.TestCase):
 def test_r2_negativo_es_valido(self):
  m=regresion([{'y_true':0,'y_pred':10},{'y_true':1,'y_pred':10}]); self.assertLess(m['R2'],0); self.assertAlmostEqual(m['RMSE']**2,m['MSE'])
 def test_objetivo_constante_indefinido(self):
  self.assertIsNone(regresion([{'y_true':2,'y_pred':2}]*20)['R2'])
 def test_matriz_clase_cero(self):
  m=clasificacion([{'y_true':'0','y_pred':'0'}]*27+[{'y_true':'0','y_pred':'1'}]*26+[{'y_true':'1','y_pred':'0'}]*12+[{'y_true':'1','y_pred':'1'}]*78)
  self.assertAlmostEqual(m['recall'],27/53); self.assertAlmostEqual(m['precision'],27/39); self.assertAlmostEqual(m['F1'],54/92)
 def test_grupo_pequeno_no_aprueba(self):
  r=auditar([{'y_true':i,'y_pred':i,'subgrupo':'A'} for i in range(5)],'regresion'); self.assertEqual(r['subgrupos'][0]['resultado'],'NO SE PUEDE DETERMINAR')
 def test_disparidad_detectada(self):
  rows=[{'y_true':i,'y_pred':i,'subgrupo':'A'} for i in range(30)]+[{'y_true':i,'y_pred':i+20,'subgrupo':'B'} for i in range(30)]
  self.assertTrue(any(g['resultado']=='FALLA' for g in auditar(rows,'regresion')['subgrupos']))
 def test_no_finitos_rechazados(self):
  with self.assertRaises(ValueError): regresion([{'y_true':1,'y_pred':float('inf')}])
if __name__=='__main__': unittest.main(verbosity=2)
