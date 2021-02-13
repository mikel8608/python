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


# Run Functions
print('data: ',data)
print("data, Show every 2nd entry: ",data[::2]) #see strings.py for more inof on [:::]
print('random value selected from data:',random.choice(data),'\n')

#show_data()
#concatenate_data()
#append_data()
#insert_data()
#delete_data()
sort_reverse_data()

print('\n*** Lists are indexed collections of non-unique elements ***\n')
