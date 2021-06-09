from Lab1 import createDB, createDBNoID
import sys

files = sys.argv

file1 = files[1]
file2 = files[2]

purchases = createDBNoID(file1)
products = createDB(file2)

for purchase in purchases:
    if purchases[purchase] != {} and int(purchases[purchase]["QUANTITY"]) >= 2:
        print(purchases[purchase]["BARCODE"] + " " + products[purchases[purchase]["BARCODE"]]["PRODDESC"] + "\n")
