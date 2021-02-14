
file='C:/Users/michael.lean/Downloads/test2.txt'

#f = open(file,"w")
#f.write('hi')

f = open(file,"r")
output = f.read()
print(output)
f.seek(0)
out2 = f.read()
print(out2)
