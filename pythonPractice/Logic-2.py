#1_make_bricks

def make_bricks(small, big, goal):
  bricks_left = goal // 5
  
  if bricks_left > big:
    bricks_left = big

  goal = goal - (bricks_left * 5)
  
  return goal <= small