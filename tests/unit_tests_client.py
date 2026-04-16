import unittest
from velivelo.client import *

class TestPseudoClientConforme(unittest.TestCase):
  def test_exemple(self):
    self.assertEqual(pseudoClientConforme("Rob96"), True)
    self.assertEqual(pseudoClientConforme("Ro"), False)
    self.assertEqual(pseudoClientConforme("Rob96666666"), False)
    self.assertEqual(pseudoClientConforme("rob96"), False)
    self.assertEqual(pseudoClientConforme("Rob96%"), False)

if __name__ == '__main__':
  unittest.main()
