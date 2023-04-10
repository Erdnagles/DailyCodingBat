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
