from Lab1 import createDB
import sys

files = sys.argv

file1 = files[1]
file2 = files[2]

customers = createDB(file1)
zones = createDB(file2)

# Lists all the ids that are in Toronto
ids = []
for id in zones:
    if zones[id] != {} and zones[id]["ZONEDESC"].lower() == "toronto":
        ids.append(id)
    
# Lists the users last names that are active in toronto
users = []
for user in customers:
    if customers[user] != {} and customers[user]["ACTIVE"] == "1" and customers[user]["ZONE"] in ids:
        users.append(customers[user]["LNAME"])

for user in users:
    print(user)
