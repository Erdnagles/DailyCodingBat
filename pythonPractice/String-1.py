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