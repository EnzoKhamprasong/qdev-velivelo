def pseudoClientConforme(pseudo : str) -> bool:
  if pseudo == "":
    raise ValueError("Le pseudo ne doit pas être vide")
  elif len(pseudo)<3 or len(pseudo)>10:
    return False
  elif pseudo[0].isupper() == False: # s'il ne commence pas par une MAJ
    return False
  elif pseudo.isalnum() == False: #Ne contient pas que des caractères alphanumériques
    return False
  else :
    return True
