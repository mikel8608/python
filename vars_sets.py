
'''
Sets 
  - No dupicate values
  - Un-ordered collections of unique elements
  - No Indexes, so you can't use positional parameters work with the elements
  - Mutable, so you can add/delete, but not based on an index
'''

print('\n*** Sets are un-ordered collections of unique elements ***\n')

data = {9,1,2,3,4,5,6,7,8,2,5}
print(data)

def data_add():
  data.add('A')
  print(data)

data_add()

print('\n*** Sets are un-ordered collections of unique elements ***\n')
