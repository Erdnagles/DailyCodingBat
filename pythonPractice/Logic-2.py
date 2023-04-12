#1_make_bricks

def make_bricks(small, big, goal):
  bricks_left = goal // 5
  
  if bricks_left > big:
    bricks_left = big

  goal = goal - (bricks_left * 5)
  
  return goal <= small

#2_lone_sum

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c:
    sum += a
  if b != a and b != c:
    sum += b  
  if c != a and c != b:
    sum += c
  return sum

#3_lucky_sum

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c

#4_no_teen_sum

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if 13 <= n <= 14 or 17 <= n <= 19:
    return 0
  return n

#5_round_sum

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(num):
  if num % 10 >= 5:
    return num + 10 - (num % 10)
  return num - (num % 10)
