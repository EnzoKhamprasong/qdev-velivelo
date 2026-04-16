import unittest
from velivelo.location import *

class TestHorsForfait(unittest.TestCase):
  def test_exemple(self):
    self.assertEqual(horsForfait(60,90), "SansDépassement")
    self.assertEqual(horsForfait(60,30), "AvecDépassement")
    self.assertEqual(horsForfait(241,380), "Amende")

if __name__ == '__main__':
  unittest.main()
