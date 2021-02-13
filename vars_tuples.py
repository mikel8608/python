'''
  similar to lists
  values are immutable
  values stored inside (), instead of {}
  tuples can have repeated values
'''
print('\n*** Tuples () are IMMUTIABLE ***\n')

tuple1 = ('t1','t2','t3','t1')

print('tuple1',tuple1)
print(type(tuple1))

msg = 'Index 1: {}, Index -1: {}'.format(tuple1[1],tuple1[-1])
print(msg)

print('t1 appears',tuple1.count('t1'),'times')
print('First Index location of t1:',tuple1.index('t1'))

print('\n*** Tuples are IMMUTIABLE ***\n')
