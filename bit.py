def binarize(number):
    bits = []
    while number:
        bits.insert(0, number % 2)
        number = number // 2
    print ("{}".format( bits) )


binarize(8)
binarize(250)
