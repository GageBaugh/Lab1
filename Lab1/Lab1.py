def createDBNoID(fileName):
    # Returns a dictionary based on whats in the file in fileName

    file = open(fileName, "r")

    # Stores the attributes from the first line of the file
    fileAttributes = file.readline().split()

    # Declares the dictonaries used for storing info
    fileInfo = {}
    currentFileInfo = {}

    # Finds max length of strings for each attribute and store them in a list
    fileMaxLength = file.readline().split()
    index = 0
    for dash in fileMaxLength:
        fileMaxLength[index] = len(dash)
        index += 1

    # Creates the dictionary of the elements in the file
    currentUser = 1
    while file:
        index = 0
        fileInfo[currentUser] = {}
        for attribute in fileAttributes:
            user = file.read(fileMaxLength[index])
            file.read(1)
            if user == "":
                return fileInfo
            fileInfo[currentUser][attribute] = user.strip()
            index += 1
        currentUser += 1

def createDB(fileName):
    # Returns a dictionary based on whats in the file in fileName

    file = open(fileName, "r")

    # Stores the attributes from the first line of the file
    fileAttributes = file.readline().split()
    fileAttributes.pop(0)

    # Declares the dictonaries used for storing info
    fileInfo = {}
    currentFileInfo = {}

    # Finds max length of strings for each attribute and store them in a list
    fileMaxLength = file.readline().split()
    index = 0
    for dash in fileMaxLength:
        fileMaxLength[index] = len(dash)
        index += 1

    # Creates the dictionary of the elements in the file
    while file:
        index = 0
        currentUser = file.read(fileMaxLength[index]).strip()
        file.read(1)
        fileInfo[currentUser] = {}
        index += 1
        for attribute in fileAttributes:
            user = file.read(fileMaxLength[index])
            file.read(1)
            if user == "":
                return fileInfo
            fileInfo[currentUser][attribute] = user.strip()
            index += 1