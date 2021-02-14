
#file='C:/Users/michael.lean/Downloads/test2.txt'

print('Use zip() to generate tuples from various lists that have an equal number of values in each list')
la = {1,2,3}
lb = {'a','b','c','d'}
lc = ('one','two','three')

print('Generate a list of tuples from:')
print(la);print(lb);print(lc)

print('\nShow the Zipped tuple combinations')
y = zip(la,lb,lc)
print(y)

print('list of zip')
print(list(zip(la,lb,lc)))

#print('read the list of tuples')
