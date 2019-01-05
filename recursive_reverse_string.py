def reverse_string0(str, n):
    if n == 0:
        return str[n]
    else:
        return str[n] + reverse_string(str, n-1)

def reverse_string(string, n):
    s = list(string)
    l = 0
    r = len(s) -1
    reverse_string_helper(s, l,r)
    return "".join(s)

def reverse_string_helper(str, l,r):
    if l >= r:
        return
    str[l], str[r] = str[r], str[l]
    reverse_string_helper(str, l+1, r-1)


''' 
string exercise
str = "hello" + " world"
print (str)
print (str[6])
str1 = str + str[6]
print (str1) '''

my_string = "hello world"
print (reverse_string(my_string, len(my_string)-1))





#list = ["1","2","3","4"]
#print (list[:-1])
