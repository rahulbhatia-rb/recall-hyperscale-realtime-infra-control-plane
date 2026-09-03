import json, unittest
from src.gate import evaluate

class GateTests(unittest.TestCase):
    def test_prod(self):
        with open('examples/production.json') as f: r=evaluate(json.load(f))
        self.assertTrue(r['allowed']); self.assertEqual(r['findings'], [])

    def test_unsafe(self):
        with open('examples/unsafe.json') as f: r=evaluate(json.load(f))
        self.assertFalse(r['allowed']); self.assertGreaterEqual(len(r['findings']), 70)
