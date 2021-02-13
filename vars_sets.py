
'''
Sets 
  - No dupicate values
  - Un-ordered collections of unique elements
  - No Indexes, so you can't use positional parameters work with the elements
  - Mutable, so you can add/delete, but not based on an index
'''

print('\n*** Sets are UN-ORDERED collections of UNIQUE elements ***\n')

data = {9,1,2,3,4,5,6,7,8,2,5}
print(data)

def data_add():
  print('\nAdding the value:','A')
  data.add('A')
  print(data)

data_add()

print('\nCast a list of values with duplicates to a Set to remove the dupes')
print(set(data))

print('\n*** Sets are UN-ORDERED collections of UNIQUE elements ***\n')
