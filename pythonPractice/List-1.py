#1_first_last6

def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  return False

#2_same_first_last

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  return False

#3_make_pi

def make_pi():
  list = []
  list.append(3)
  list.append(1)
  list.append(4)
  
  return list

#4_common_end

def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  return False

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
