x=0
k=0
x, k = map(int, input().split())
exp = input()
print (eval(exp))
if eval(exp) == k:
    print ("True")
else:
    print ("False")