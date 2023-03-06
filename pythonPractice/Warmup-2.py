#1_string_times

def string_times(str, n):
  if n >= 0:
    return n * str
  
def string_times(str, n):
  result = ""
  for i in range(n): 
    result += str  
  return result

#2_front_times

def front_times(str, n):
  frontLen = 3
  if frontLen > len(str):
    frontLen = len(str)
  front = str[:frontLen]

  result  = ""
  for i in range(n):
    result = result + front
  return result

#3_string_bits

def string_bits(str):
  return str[::2]

def string_bits(str):
  newStr = ""
  for i in range(len(str)):
    if i % 2 == 0:
      newStr += str[i]
  return newStr

#4_string_splosion

def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result += str[:i+1]
  return result

#5_last2

def last2(str):
  if len(str) < 2:
    return 0
  
  count = 0
  for i in range(len(str) - 2):
    if (str[i:i+2] == str[-2:]):
      count += 1
  return count

#6_array_count9

def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count += 1
  return count

#7_array_front9

def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  for i in range(end):
    if nums[i] == 9:
      return True
  return False