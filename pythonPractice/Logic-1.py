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

#3_squirrel_play

def squirrel_play(temp, is_summer):
  if temp in range(60, 91):
    return True
  if temp in range(60, 101) and is_summer:
    return True 
  return False

def squirrel_play(temp, is_summer):
  if is_summer == True:
    return 60 <= temp <= 100
  return 60 <= temp <=90

#4_caught_speeding

def caught_speeding(speed, is_birthday):
  bd_speed = 0
  
  if is_birthday == True:
    bd_speed = 5
  
  if speed < 61 + bd_speed:
    return 0
  if speed < 81 + bd_speed:
    return 1
  return 2
