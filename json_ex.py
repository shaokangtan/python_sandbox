#https://pythonspot.com/json-encoding-and-decoding-with-python/
'''
Note! Keys in key/value pairs of JSON are always of the type str.
When a dictionary is converted into JSON, all the keys of the dictionary are coerced to strings. 
As a result of this, if a dictionary is converted into JSON and then back into a dictionary, 
the dictionary may not equal the original one. 
That is, loads(dumps(x)) != x if x has non-string keys.
'''

#from json import *
import json
'''
FILE = "test.txt"
my_dict = { "apple": 3, "mongo": 5, "peach": 8 }
f_obj = open(FILE,'w')
items_in_json = json.dump(my_dict, f_obj)
f_obj.close()

with open (FILE, 'r') as f_obj:
    my_dict = json.load(f_obj)
    print (my_dict)

    f_obj.close()


FILE = "test.txt"
my_list = [ "apple", "mongo", "peach" ]
f_obj = open(FILE,'w')
items_in_json = json.dump(my_list, f_obj)
f_obj.close()

with open (FILE, 'r') as f_obj:
    my_list = json.load(f_obj)
    print (my_list)

    f_obj.close()


with open ('test1.txt', 'r') as f_obj:
    my_str = f_obj.read()
    my_dict = json.loads(my_str)
    print (my_dict)

    f_obj.close()


import json
from decimal import Decimal
 
jsondata = '{"number": 1.573937639}'
 
x = json.loads(jsondata, parse_float=Decimal)
y = json.loads(jsondata)
print (x['number'])
print (Decimal(3))


import json
from decimal import Decimal
 
d = {}
d["Name"] = "Luke"
d["Country"] = "Canada"
 
print (json.dumps(d, ensure_ascii=False))
# result {"Country": "Canada", "Name": "Luke"}
'''
import json
 
#json_data = '{"name": "Brian", "city": "Seattle"}'
json_data = '[1,2,3,4,9,8,7,6]'
python_obj = json.loads(json_data)
print (json.dumps(python_obj))
print (json.dumps(python_obj, sort_keys=True, indent=4))
s = json.loads('"\\"foo\\bar"')
print (s)

my_dict = {1:"a", 2:"b", 3:"c"}
your_dict = json.dumps(my_dict)
print (your_dict)