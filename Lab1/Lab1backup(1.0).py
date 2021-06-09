def createDB(fileName):
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

def q1(file1, file2):
    # Find all active users last names who live in Toronto

    db1 = createDB(file1)
    db2 = createDB(file2)

    # Lists all the ids that are in Toronto
    ids = []
    for id in db2:
        if db2[id] != {} and db2[id]["ZONEDESC"].lower() == "toronto":
            ids.append(db2[id]["ZONEID"])
    print(ids)
    # Lists the users last names that are active in toronto
    users = []
    for user in db1:
        if db1[user] != {} and db1[user]["ACTIVE"] == "1" and db1[user]["ZONE"] in ids:
            users.append(db1[user]["LNAME"])

    for user in users:
        print(user)

#def q2(file1, file2):

q1("customer.txt", "zonecost.txt")