'''
  you can have nested objects
  unordered
'''
import random

print('\n*** Dictionaries {} are Key/Value Pairs ***\n')

dict1 = {'one':1,'two':2,'three':3,'four':4}
dict2 = {'list':[5,6,7]}
dict3 = {'dictionary':{'eight':8,'nine':9}}

def basic_output():
  print('dict1:',dict1)
  print('dict2:',dict2)
  print('dict3:',dict3)
  print('\n')
  print('dict1: Value of one = ',dict1['one'])
  print('dict2: List: first value =',dict2['list'][0])
  print('dict3: Dictionary: Value of nine = ',dict3['dictionary']['nine'])
  print('Length of dict1:',len(dict1))


def itterate_dict1():
  print('\nShow Values')
  print(dict1.values())
  cnt=0
  for value in dict1.values():
    print(cnt,':',value)  
    cnt+=1

  print('\nShow Keys')
  print(dict1.keys())
  cnt=0
  for key in dict1.keys():
    print(key.upper())
    cnt+=1

  print('\nShow Items (tuples)')
  print(dict1.items())
  cnt=0
  for i in dict1.items():
    print(cnt,':',i)
    cnt+=1  

def selectvalue_dict1():
  print("\nValue stored in key 'two' is",dict1['two'])

def add_update_dict1():
  dict1['five'] = 5
  print('\nadded a 5th keypair:',dict1)

def delete_dict1():
  del dict1['five']
  print('deleted item:',dict1)

def nested():
  emp = {'fName':'Silva','lName':'Stone','Skills':['aws','ansible','docker']}
  
  print('\nNested values')
  cnt=0
  for e in emp.values():
    print(cnt,':',e)
    cnt+=1

  print("\nIndex 2 of the 'Skills' Key:",emp['Skills'][1])

#basic_output()
#itterate_dict1()
#selectvalue_dict1()    
#add_update_dict1()
#delete_dict1()
#nested()

print('\n*** Dictionaries {} are Key/Value Pairs ***\n')


