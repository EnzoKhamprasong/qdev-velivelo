import unittest
from velivelo.location import *

class TestHorsForfait(unittest.TestCase):
  def test_exemple(self):
    self.assertEqual(horsForfait(60,90), Verdict.SANS_DEPASSEMENT)
    self.assertEqual(horsForfait(60,30), Verdict.AVEC_DEPASSEMENT)
    self.assertEqual(horsForfait(241,380), Verdict.AMENDE)

if __name__ == '__main__':
  unittest.main()
