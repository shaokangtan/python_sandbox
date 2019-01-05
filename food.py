def balance(food):
    sum = {}
    for (key,value) in food:
        if key in sum:
            sum[key] = sum[key] + value
        else:
            sum[key] = value
    return sum

def sort_by_key(food):
    for key in sorted(food.keys()):
        print ("%s: %s" % (key, food[key]))

def sort_by_value(food):
    for key, value  in sorted(food.items(), key=lambda x :x[1] ):
        print ("%s: %s" % (key, value))


if __name__ == "__main__":
    food = [ ("apple", 7), ("banana", 3), ("lemon", 8), ("orange", 3), ("kiwi", 2), ("apple", 1), ("banana", 2), ("lemon", 3), ("orange", 4) , ("kiwi", 5)]
    sum = balance(food)
    print ("sum {}".format(sum))
    #print ("sort by key", end=None)
    #sort_by_key(sum)
    print ("sort by value", end=None)
    sort_by_value(sum)


