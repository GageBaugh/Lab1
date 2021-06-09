from Lab1 import createDB

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