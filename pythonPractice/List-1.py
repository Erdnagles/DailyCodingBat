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
