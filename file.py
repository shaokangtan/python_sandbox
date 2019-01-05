#
# 1. file open
# 2. file read
# 3. file write
#

FILE = "test.txt"
items = { "apple": 3, "mongo": 5, "peach": 8 }
with open(FILE,'w') as f_obj:
    for name,price in items.items():
        f_obj.write(name)
        f_obj.write(":")
        f_obj.write(str(price)+"\n")

with open (FILE, 'r') as f_obj:
    line = f_obj.readline()
    while line != "" :
        name, price = line.split(":")
        price = price.strip("\n")
        print ("{} : {}".format(name, price))
        line = f_obj.readline()
        f_obj.tell()

    f_obj.close()