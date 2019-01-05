#commonly used sgring operators
string1 = " hello  "
string2=string1.strip() # full copy, not a reference copy
print (string1)
print (string2)
string3 = "hello world"
strings = string3.split(" ")
print (strings)
print (string3.find("world"))
print (string3.index("world"))
string4 = "hello how are hello"
print (string4.rfind("hello"))
index = string4.rindex("hello")
print (string4[:index])
print (string4[index:])
print ("-".join(string1))
print ("-".join([string2,string3]))

