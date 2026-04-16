def pseudoClientConforme(pseudo : str) -> bool:
  if pseudo == "":
    raise ValueError("Le pseudo ne doit pas être vide")
  elif len(pseudo)<3 or len(pseudo)>10:
    return False
