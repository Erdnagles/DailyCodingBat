#1_sleep_in

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  return False

#2_monkey_trouble

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  return False

#3_sum_double

def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum

#4_diff21

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

#5_parrot_trouble

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

#6_makes10

def makes10(a, b):
  return (a + b == 10 or a == 10 or b == 10)

#7_near_hundred

def near_hundred(n):
  if n in range(90, 111) or n in range(190, 211):
    return True
  return False

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#8_pos_neg

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

