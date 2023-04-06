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

#5_sorta_sum

def sorta_sum(a, b):
  sum = a + b
  if sum in range(10, 20): # 10 <= sum <= 20
    return 20
  return a + b

#6_alarm_clock

def alarm_clock(day, vacation):
  if day == 0 or day == 6:
    if vacation:
      return "off"
    return "10:00"
  
  if vacation: 
    return "10:00"
  return "7:00"

def alarm_clock(day, vacation):
  weekend = "off"
  weekday = "10:00"
  
  if (vacation == False):
    weekend = "10:00"
    weekday = "7:00"
    
  if day % 6 == 0:
    return weekend
  return weekday

#7_love6

def love6(a, b):
  if (a == 6 or b == 6) or (a + b == 6) or (abs(a-b)==6):
    return True
  return False

#8_in1to10

def in1to10(n, outside_mode):
  if outside_mode: 
    return n <= 1 or n >= 10
  
  return n >= 1 and n <= 10
