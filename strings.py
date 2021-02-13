
def formatting_output():
  '''
      %d -> Integer
      %e -> exponential
      %f -> Float
      %o -> Octal
      %x -> Hexadecimal
  '''
  print("Float value of 5 is: %f" %5)

  var1='Value 1'; var2='Value 2'; var3=6
  print("Output mutliple variables: %s, %s - %d" %(var1,var2,var3))


def string_multiline():
  print('''
       this is a 
          multi-line string
       ''')

# Strings are objects just like other variables, so they have methods.
def str_methods():
  str1 = 'string 1'.upper()
  print(str1,'\n')

def split_example():
    str2 = 'one two three'.split()
    for value in str2:
      print(value)

def string_indexing():
  str3 = '123456789'
  print('Print from the 3rd letter to the end: ',str3[2:])
  print('Print from the begining to the 3rd letter: ',str3[:2])

  # The 3rd element in [] is a step size. So here we return every 2nd element
  print('Print every second letter from begining to end: ',str3[::2])
  # Reverse the step order
  print('Print every second letter from the end to begining: ',str3[::-2])

def format_function():
  msg = '{} - {}'.format('val1','val2')
  print('format():',msg)

def var_substitution():
  #var1='value1'; var2='value2'
  #print(f"{var1} - {var2}")
  val = 'Geeks'
  print(f"{val}for{val} is a portal for {val}.")

var_substitution()
exit()

formatting_output()
string_multiline()
str_methods()
split_example()
string_indexing()
format_function()
