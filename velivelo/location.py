from enum import Enum

class Verdict(Enum):
  SANS_DEPASSEMENT = 0,
  AVEC_DEPASSEMENT = 1,
  AMENDE = 2

def horsForfait(dureeLocation : int, tempsRestant : int) -> Verdict:
  if dureeLocation > 240:
    return Verdict.AMENDE
  if dureeLocation <= 0 :
    raise ValueError("dureeLocation doit être > 0")
  # dureeLocation <= 240
  if dureeLocation <= tempsRestant:
    return Verdict.SANS_DEPASSEMENT
  else:
    return Verdict.AVEC_DEPASSEMENT
