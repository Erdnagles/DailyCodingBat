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
    if i%2 == 0:
      newStr += str[i]
  return newStr
