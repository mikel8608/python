def string_multiline():
  print('''
       this is a 
          multi-line string
       ''')

# Strings are objects just like other variables, so they have methods.
def str_Method():
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

string_multiline()
str_Method()
split_example()
string_indexing()