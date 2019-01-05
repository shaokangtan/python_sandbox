def test_var_args(*argv):
    for arg in argv:
        print ("another arg through *argv :", arg)

def test_args_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("%s == %s" %(key,value))

# first with *args
args = ("two", 3,5)
test_var_args(*args)

# now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)
