from enum import Enum

class Verdict(Enum):
  SANS_DEPASSEMENT = 0,
  AVEC_DEPASSEMENT = 1,
  AMENDE = 2

def horsForfait(duree_location : int, temps_restant : int) -> Verdict:
  pass
