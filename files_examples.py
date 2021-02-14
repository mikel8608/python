writeMe = "line 1"
appendMe = "line 2"
file = "C:/Users/michael.lean/AppData/Local/Documents_Work/python/files_test.txt"

def writeFile():
    fileName = open(file, "w")
    fileName.write(writeMe)
    fileName.close()


def appendFile():
    fileName = open(file, "a")
    fileName.write("\n" + appendMe)
    fileName.close()


def readFile():
    fileName1 = open(file, "r").read()
    print('\nReading file using: open(file,"r").read() allows you to re-read the file multiple times without setting seek(0)')
    print(fileName1)

    print('\n *** NOTE: .read() must be assigned to a variable !!')
    fileName2 = open(file,"r")
    f2 = fileName2.read()
    print('\nReading file using: f2 = fileName2.read()')
    print(f2)
    print('\nTo Re-Read file you need to set Seek(0)')
    fileName2.seek(0)
    print(f2)

    fileName2.close()


def splitlinesFile():
    # Extract Lines into a LIST
    
    # option 1
    fileName = open(file,"r").read()
    splitLines = fileName.split("\n")
    print("\nUse '.split('\\n')' to generate a LIST from the lines in the file: ")
    print(splitLines)
    print("\nPrint second value in the LIST: ")
    print(splitLines[1])
    
    # option 2
    readLines = open(file , "r").readlines()
    print("\nUse readlines() to create a LIST (NB: RETURN Char is also listed): ")
    print(readLines)



def readlines_file():
    print('Output each line into a list that includes the RETURN char')
    f = open(file,"r").readlines()
    print(f)

def open_with_file():
    print("When using 'with, you don't need to close the file after")
    with open(file) as f:
        contents = f.read()
    print(contents)


# writeFile()
# appendFile()
# readFile()
# readlines_file()
# splitlinesFile()
open_with_file()
