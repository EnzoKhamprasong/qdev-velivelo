import unittest
from velivelo.location import *

class TestHorsForfait(unittest.TestCase):
  def test_SansDepassement(self):
    self.assertEqual(horsForfait(60,90), Verdict.SANS_DEPASSEMENT)
  def test_AvecDepassement(self):
    self.assertEqual(horsForfait(60,30), Verdict.AVEC_DEPASSEMENT)
  def test_Amende(self):
    self.assertEqual(horsForfait(241,380), Verdict.AMENDE)
  def test_Error(self):
    self.assertRaises(ValueError,horsForfait,0,30)

if __name__ == '__main__':
  unittest.main()
