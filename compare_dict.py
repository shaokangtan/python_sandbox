

dict_1 = {
        "key1": "val1",
        "key2": "val2",
        "key4": "val4",
        "key6": [{"k10": "v13"}, {"k11": "v11"}],
    }
 
dict_2 = {
  "key1": "val1",
  "key2": "val2",
  "key4": "val4",
  "key6": [
    {
      "k10": "v5"
    }
  ]
}
 
'''
 Output:
 
{
  "key6. k10": {
    "dict1": "v13",
    "dict2": "v5"
  },
  "key6.k11": {
    "dict1": "v11",
    "dict2": null
  }
}
'''


def dict_comparer(d1, d2, ctx=""):
    print ("Changes in " + ctx)
    for k in d1:
        if k not in d2:
            print (ctx + "." + k + " removed from d2")
    for k in d2:
        if k not in d1:
            print (ctx + "." + k + " added in d2")
            continue
        if d2[k] != d1[k]:
            if type(d2[k]) not in (dict, list):
                print (ctx + "." + k + " changed in d2 to " + str(d2[k]))
            else:
                if type(d1[k]) != type(d2[k]):
                    print (ctx + "." + k + " changed to " + str(d2[k]))
                    continue
                else:
                    if type(d2[k]) == dict:
                        dict_comparer(d1[k], d2[k], k)
                        continue
                    elif type(d2[k]) == list:
                        dict_comparer(list_to_dict(d1[k]), list_to_dict(d2[k]), k)    
    print ("Done with changes in " + ctx)
    return

def list_to_dict(l):
    return dict(zip(map(str, range(len(l))), l))

type(dict_1)
isinstance(dict_1, dict)

diff_dict = dict_comparer(dict_1, dict_2)
print (diff_dict)