import unittest
from velivelo.client import *

class TestPseudoClientConforme(unittest.TestCase):
  def test_pseudoConforme(self):
    self.assertEqual(pseudoClientConforme("Rob96"), True)
  def test_pseudoNonConforme(self):
    self.assertEqual(pseudoClientConforme("Ro"), False)
    self.assertEqual(pseudoClientConforme("Rob96666666"), False)
    self.assertEqual(pseudoClientConforme("rob96"), False)
    self.assertEqual(pseudoClientConforme("Rob96%"), False)
  def test_pseudoError(self):
    self.assertRaises(ValueError,pseudoClientConforme,"")

if __name__ == '__main__':
  unittest.main()
