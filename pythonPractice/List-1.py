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

#5_sum3

def sum3(nums):
  sum = 0

  for i in range(0, len(nums), 1):
    sum = sum + nums[i]

  return sum

#6_rotate_left3

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

#7_reverse3

def reverse3(nums):
  reversed = []
  for i in range(len(nums)-1, -1, -1):
    reversed.append(nums[i])
  return reversed

#8_max_end3

def max_end3(nums):
  bigger = max(nums[0], nums[2])
  return [bigger, bigger, bigger]

#9_sum2

def sum2(nums):
  if len(nums) <= 2:
    return sum(nums)
  if len(nums) > 2:
    return sum(nums[:2])

#10_middle_way

def middle_way(a, b):
  return [a[1], b[1]]
  
  middleArr = []
  middleArr.append(a[1])
  middleArr.append(b[1])
  return middleArr
