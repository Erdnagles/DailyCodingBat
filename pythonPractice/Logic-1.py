#1_cigar_party

def cigar_party(cigars, is_weekend):
  if cigars in range(40, 61):
    return True
  if cigars >= 40 and is_weekend:
    return True
  return False

def cigar_party(cigars, is_weekend):
  if is_weekend == False:
    return cigars >= 40 and cigars <= 60
  return cigars >= 40

#2_date_fashion

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0

  if you >= 8 or date >= 8:
    return 2
    
  return 1
