'''
  Lists can consist of various data types.
  Ordered
'''
import random

print('\n*** Lists are indexed collections of non-unique elements ***\n')

data = [1,2,'A','B',1]

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
  print('\nDelete 1st element')
  del data[0]
  show_data()

# Run Functions
print('data: ',data)
print("data, Show every 2nd entry: ",data[::2]) #see strings.py for more inof on [:::]
print('random value selected from data:',random.choice(data),'\n')

show_data()
#append_data()
#insert_data()
#delete_data()

print('\n*** Lists are indexed collections of non-unique elements ***\n')
