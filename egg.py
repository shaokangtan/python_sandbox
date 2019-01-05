# eggs: 2
def function(floors, skip):
    my_try = 0
    my_try = (floors//skip -1) + (skip-1)
    return my_try
for skip in range(1,100):
    my_try = function(100, skip)
    print ("skip: {}, worst O= {}".format(skip, my_try))

# eggs: unlimited
floor = 100
tries = 0
while floor :
    tries += 1
    floor //= 2
print ("unlimited eggs try", tries)

'''
best, avg, worst
output :
skip: 1, worst O= 99
skip: 2, worst O= 50
skip: 3, worst O= 34
skip: 4, worst O= 27
skip: 5, worst O= 23
skip: 6, worst O= 20
skip: 7, worst O= 19
skip: 8, worst O= 18
skip: 9, worst O= 18
skip: 10, worst O= 18
skip: 11, worst O= 18
skip: 12, worst O= 18
skip: 13, worst O= 18
skip: 14, worst O= 19
skip: 15, worst O= 19
skip: 16, worst O= 20
skip: 17, worst O= 20
skip: 18, worst O= 21
skip: 19, worst O= 22
skip: 20, worst O= 23
skip: 21, worst O= 23
skip: 22, worst O= 24
skip: 23, worst O= 25
skip: 24, worst O= 26
skip: 25, worst O= 27
skip: 26, worst O= 27
skip: 27, worst O= 28
skip: 28, worst O= 29
skip: 29, worst O= 30
skip: 30, worst O= 31
skip: 31, worst O= 32
skip: 32, worst O= 33
skip: 33, worst O= 34
skip: 34, worst O= 34
skip: 35, worst O= 35
skip: 36, worst O= 36
skip: 37, worst O= 37
skip: 38, worst O= 38
skip: 39, worst O= 39
skip: 40, worst O= 40
skip: 41, worst O= 41
skip: 42, worst O= 42
skip: 43, worst O= 43
skip: 44, worst O= 44
skip: 45, worst O= 45
skip: 46, worst O= 46
skip: 47, worst O= 47
skip: 48, worst O= 48
skip: 49, worst O= 49
skip: 50, worst O= 50
skip: 51, worst O= 50
skip: 52, worst O= 51
skip: 53, worst O= 52
skip: 54, worst O= 53
skip: 55, worst O= 54
skip: 56, worst O= 55
skip: 57, worst O= 56
skip: 58, worst O= 57
skip: 59, worst O= 58
skip: 60, worst O= 59
skip: 61, worst O= 60
skip: 62, worst O= 61
skip: 63, worst O= 62
skip: 64, worst O= 63
skip: 65, worst O= 64
skip: 66, worst O= 65
skip: 67, worst O= 66
skip: 68, worst O= 67
skip: 69, worst O= 68
skip: 70, worst O= 69
skip: 71, worst O= 70
skip: 72, worst O= 71
skip: 73, worst O= 72
skip: 74, worst O= 73
skip: 75, worst O= 74
skip: 76, worst O= 75
skip: 77, worst O= 76
skip: 78, worst O= 77
skip: 79, worst O= 78
skip: 80, worst O= 79
skip: 81, worst O= 80
skip: 82, worst O= 81
skip: 83, worst O= 82
skip: 84, worst O= 83
skip: 85, worst O= 84
skip: 86, worst O= 85
skip: 87, worst O= 86
skip: 88, worst O= 87
skip: 89, worst O= 88
skip: 90, worst O= 89
skip: 91, worst O= 90
skip: 92, worst O= 91
skip: 93, worst O= 92
skip: 94, worst O= 93
skip: 95, worst O= 94
skip: 96, worst O= 95
skip: 97, worst O= 96
skip: 98, worst O= 97
skip: 99, worst O= 98
'''