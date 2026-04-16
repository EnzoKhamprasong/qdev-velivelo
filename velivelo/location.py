from enum import Enum

class Verdict(Enum):
  SANS_DEPASSEMENT = 0,
  AVEC_DEPASSEMENT = 1,
  AMENDE = 2

def horsForfait(dureeLocation : int, tempsRestant : int) -> Verdict:
  if dureeLocation > 240:
    return Verdict.AMENDE
  # dureeLocation <= 240
  if dureeLocation <= tempsRestant:
    return Verdict.SANS_DEPASSEMENT
  else:
    return Verdict.AVEC_DEPASSEMENT
