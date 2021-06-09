from Lab1 import createDB, createDBNoID

def q2(file1, file2):
    # Outputs barcode and product desciption of each item bought at least twice
    createDBNoID(file1)
    createDB(file2)


q2("lineitem.txt", "products.txt")