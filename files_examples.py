writeMe = "line 1"
appendMe = "line 2"


def writeFile():
    FileName = open("C:/Users/michael.lean/AppData/Local/Documents_Work/python/files_test.txt", "w")
    FileName.write(writeMe)
    FileName.close()


def appendFile():
    FileName = open("C:/Users/michael.lean/AppData/Local/Documents_Work/python/files_test.txt", "a")
    FileName.write("\n" + appendMe)
    FileName.close()


def readFile():
    FileName = open("C:/Users/michael.lean/AppData/Local/Documents_Work/python/files_test.txt", "r").read()
    print("Output Raw data from file")
    print(FileName)

    # Extract Lines into a LIST
    # option 1
    splitLines = FileName.split("\n")
    print("\nGenerate a LIST from the lines in the file: ", splitLines)
    print("\nPrint second value in the LIST: ", splitLines[1])
    # option 2
    readLines = open(
        "C:/Users/michael.lean/AppData/Local/Documents_Work/python/files_test.txt", "r"
    ).readlines()
    print(
        "\nUse the readlines Function to create a LIST (NB: RETURN Char is also listed): ",
        readLines,
    )


# writeFile()
# appendFile()
#readFile()

