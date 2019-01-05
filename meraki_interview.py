# quiz: find the version where bug is found
test_versions = [1.0,2.0,3.0,4.0,4.1,4.2,4.3,4.4,4.5,5.0,5.1]
def is_broken(ver):
    if ver >= 6.1:
        return True
    else:
        return False


def find_broken_version(versions):
    if len(versions) < 1:
        return - 1
    total_version = len(versions)
    if is_broken(versions[total_version//2]):
        ret = find_broken_version(versions[:total_version//2])
        if ret == -1:
            print ("broken version starts from {}".format(versions[total_version//2]))
            ret = 0
    else:    
        ret = find_broken_version(versions[total_version//2+1:])
        if ret == -1:
            #print ("no broken version found")
            ret = -1
    return ret         

ret = find_broken_version(test_versions)
if ret == -1:
    print ("no broken version found")
