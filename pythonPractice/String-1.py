#1_hello_name

def hello_name(name):
  return "Hello " + name + "!"

#2_make_abba

def make_abba(a, b):
  return a + b + b + a

#3_make_tags

def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'

#4_make_out_word

def make_out_word(out, word):
  return out[:2] + word + out[-2:]

#5_extra_end

def extra_end(str):
  return 3 * str[-2:]

#6_first_two

def first_two(str):
  if len(str) < 2:
    return str
  return str[:2]
