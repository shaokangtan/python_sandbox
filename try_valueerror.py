try:
    #raise ValueError("test vaule error","1","2","3")
    raise Exception ("my exception", "1", "2", "3")
    pass
except ValueError as v:
    print ("ValueError {}".format(v.args))
except Exception as e:
    print("Exception {}".format(e.args))
else:
    print ("no error")
