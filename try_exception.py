# exception is run-time error and test error
# assert is test fail

err_is = None
try:
    # assert False
    raise AssertionError
    raise ValueError
    print(5/0)
# except ZeroDivisionError:
#     err_is = ZeroDivisionError
#     print("You can't divide by zero")
except  AssertionError:
    err_is = AssertionError
    print("AssertionError handler")
except Exception:
    # any errors beside assert
    err_is = Exception
    print("Exception handler")
finally:
    print ("finally, do clean up here, do account or settings restore")
    # raise exception  again
    # if err_is == ZeroDivisionError:
    #     raise ZeroDivisionError
    if err_is == AssertionError:
        raise AssertionError
    if err_is == Exception:
        raise Exception
#else:
#    print ("else")

print("exit")
