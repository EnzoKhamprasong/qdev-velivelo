import unittest
from velivelo.client import *

class TestPseudoClientConforme(unittest.TestCase):
  def test_exemple(self):
    self.assertEqual(True, False)

if __name__ == '__main__':
  unittest.main()
