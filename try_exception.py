try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print ("finally")
#else:
#    print ("else")

print("exit")