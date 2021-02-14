'''
  Lists can consist of various data types.
  Ordered
'''
import random

print('\n*** Lists are indexed collections of non-unique elements ***\n')

data = [1,2,'A','B',1]
data_ints = [1,2,6,2,5,4]

def show_data():
  print('Showing Data')
  counter=0
  for val in data:
    print(counter,': ',val)
    counter += 1

  print('Index location of value 2 is: ',data.index(2))

def append_data():
  print('\nappend Output')
  data.append(10.1)
  show_data()

def insert_data():
  print('\nInsert 1st Element')
  data.insert(0,'New Value')
  show_data()

def delete_data():
  print("\nDelete 1st element using 'del'")
  del data[0]
  show_data()

  print("\nDelete element with 'pop()'",'If no index is provided it pops off the last element')
  data.pop(2)
  show_data()

def concatenate_data():
  print('\nConcatinating 2 lists')
  data2 = ['data2','data3']
  print(data+data2)
  show_data()

def sort_reverse_data():
  print('data_ints unsorted',data_ints)
  print("data_ints Sorted Function",sorted(data_ints)) 
  
  print('The .sort() & .reverse() functions update the list, so you can only assign/print the list after using the functions')
  data_ints.sort()
  print('data_ints after .sort()',data_ints)
  data_ints.reverse()
  print('data_ints after .reverse()',data_ints)


def zip_function_examples():
  print('\nUse zip() to generate tuples from various lists that have an equal number of values in each list')
  la = {1,2,3}
  lb = {'a','b','c','d'}
  lc = ('one','two','three')

  print('\nGenerate a list of tuples from:')
  print(la);print(lb);print(lc)

  print('\nShow the Zipped tuple combinations')
  y = zip(la,lb,lc)
  print(y)

  print('\nList of zip')
  print(list(zip(la,lb,lc)))

  # Run Functions
def other_functions():
  print('data list: {}'.format(data_ints))
  print('Every 2nd value: {}'.format(data_ints[::2])) #see strings.py for more inof on [:::]
  print('random value: {}'.format(random.choice(data_ints)))
  print('min: {}'.format(min(data_ints)))
  print('max: {}'.format(max(data_ints)))
  #shuffle(data_ints); print(data_ints)
   

def list_comprehensions():
  print('Create basic list from string')
  string = 'word'
  
  # Long way to gerenerate list
  list_1 = []
  for letter in string:
    list_1.append(letter)
  print('list_1: {}'.format(list_1))

  # Short way to generate list
  # As a sentence this is: Insert the 'letter' for every 'letter' in 'string'.
  list_2 = [letter for letter in string]
  print('list_2: {}'.format(list_2))

  print('\nlist from range')
  list_nums = [x for x in range(1,10)]
  print('list_nums: {}'.format(list_nums))

  print('\nlist from range where there is an action on the value')
  list_nums2 = [x**2 for x in range(1,10)]
  print('list_nums2: {}'.format(list_nums2))

  list_every_second_value = [num for num in range(1,20) if num%2==0]
  print('Every 2nd Value: {}'.format(list_every_second_value))

  # Run in Terminal. Doesn't work properly in code Output
  celcius = [0,10,20,34.5]
  fahrenheit_list = [((9/5)*temp + 32) for temp in celcius]
  print('Celcius: {}\nFahrenheit: {}'.format(celcius,fahrenheit_list))

  print('if, else example')
  results = [x if x%2==0 else 'ODD' for x in range(1,11)]
  print(results)

  print('nested for loops example. Remember to increment range 1 above the value you want.')
  results2 = [x*y for x in range(1,3) for y in [10,100,1000]]
  print(results2)

#show_data()
#concatenate_data()
#append_data()
#insert_data()
#delete_data()
#sort_reverse_data()
#zip_function_examples()
#other_functions()
list_comprehensions() #Generate Lists

print('\n*** Lists are indexed collections of non-unique elements ***\n')
