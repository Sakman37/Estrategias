import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from router import *

class RouterTests(unittest.TestCase):
 def setUp(self): self.r=Router(campus_graph())
 def test_fastest_route_found_and_positive(self):
  x=self.r.route('Entrada','Laboratorios',FastestStrategy()); self.assertTrue(x['found']); self.assertGreater(x['minutes'],0)
 def test_accessible_route_avoids_stairs(self):
  x=self.r.route('Entrada','Laboratorios',AccessibleStrategy()); self.assertTrue(x['found']); self.assertEqual(x['stairs'],0)
 def test_closure_changes_or_preserves_valid_route(self):
  x=self.r.route('Entrada','Laboratorios',FastestStrategy(),closed=[('Plaza','Biblioteca')]); self.assertTrue(x['found']); self.assertNotIn('Biblioteca',x['path'])
 def test_same_origin_destination(self):
  x=self.r.route('Plaza','Plaza',FastestStrategy()); self.assertEqual(x['path'],['Plaza']); self.assertEqual(x['minutes'],0)
 def test_unknown_node_rejected(self):
  with self.assertRaises(ValueError): self.r.route('X','Plaza',FastestStrategy())
 def test_no_path(self):
  x=self.r.route('Entrada','Laboratorios',AccessibleStrategy(),closed=[('Entrada','Plaza'),('Entrada','Jardin')]); self.assertFalse(x['found'])
if __name__=='__main__': unittest.main()
