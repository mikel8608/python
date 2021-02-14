
'''
  break:    exit current loop
  continue: go to top of loop
  pass:     do nothing
'''


def for_range():
    # range is a generator function. Pervious vesrions of this function would create a list in memory so you could blow out your ram if the list is too large.
    print('range(3)')
    for x in range(3):
        print(x)

    print('range(1,4)')
    for x in range(1,4):  #python 2.7 uses xrange() which is basd on py3 range()
        print(x)  #print(f'{x}')

    print('range(1,10,2)')
    for x in range(1,10,2):
        print(x)

    print('Itterate a String')
    index = 0
    string = 'abcdefg'
    for letter in string:
        print('Letter {} has value {}'.format(index,letter))
        index += 1

    print('Letters in Word')
    word = 'hello'
    index = 0
    for letter in word:
        print(word[index])
        index += 1

def for_tuple():
    # tuple unpacking.
    example = [(1,2,'a'),(3,4,'b'),(5,6,'c'),(7,8,'d')]
    print('Unpacking tuple pairs')
    for a,b,c in example:
        print(a);print(b); print(c)
        print()

    print('Letters in Word - Enumerate Version')
    word = 'hello'
    for item in enumerate(word):
        print(item)

    print('Individual Tuple Values from Word - Enumerate Version')
    for index,letter in enumerate(word):
        print('index: {}, letter: {}'.format(index,letter))

def while_else():
    # infinite loop
    x = 0
    while x < 5:
        x +=1
    else:
        print('x >= 5')

def while_infinite():
    while True:
        pass
    
#for_range()
for_tuple()
#while_else()
#while_infinite()
