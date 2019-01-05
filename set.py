def average(array):
    # your code goes here
    plants = set(array)
    sum=0
    for i in plants:
        sum += i
    avg = sum / len(plants)
    print ("{}".format(avg))


def exe_1():
    a = [100,99,90,89,40]
    average(a)

def exe_2():
    m = input()
    m_set = set(map(int, input().split()))
    n = input()
    n_set = set(map(int, input().split()))
    '''
        print (m_set)
        for i in sorted(m_set.difference(n_set)):
            print (i)
        print (n_set)
        for i in sorted(n_set.difference(m_set)):
            print (i)
    '''
    set = m_set.difference(n_set)
    set.update(n_set.difference(m_set))
    for i in sorted(set):
        print (i)

def exe_3():
    m, n = map(int, input().split())
    happy_list = list(map(int, input().split()))
    like_set = set(map(int, input().split()))
    dislike_set = set(map(int, input().split()))
    likes = 0
    dislikes = 0
    for i in happy_list:
        if i in like_set:
            likes += 1
        if i in dislike_set:
            dislikes += 1
    print (likes - dislikes)
    #print(len(happy_set.intersection(like_set)) - len(happy_set.intersection(dislike_set)))

def exe_4():
    countries = int( input().strip())
    country_set = set()
    for i in range(countries):
        country_set.add(input().strip())
    #print (country_set)
    print (len(country_set))

def exe_5():
    '''
    9
    1 2 3 4 5 6 7 8 9
    10
    pop
    remove 9
    remove 9
    discard 8
    remove 7
    pop
    discard 6
    remove 5
    pop
    discard 5
'''
    n = int(input())
    s = set(map(int, input().split()))
    commands = int(input())

    for i in range(commands):
        command = list(input().split())
        if command[0] == "pop":
            s.pop()
        if command[0] == "discard":
            s.discard(int(command[1]))
        if command[0] == "remove":
            try :
                s.remove(int(command[1]))
            except KeyError:
                #print("%s: %d not found" % (command[0], int(command[1])))
                pass
    sum = 0
    for i in s:
        sum += i
    print(sum)

def exe_6():
    m = int(input())
    m_set = set(map(int, input().split()))
    n = int(input())
    n_set = set(map(int, input().split()))
    m_n_union_set = m_set.union(n_set)
    print (len(m_n_union_set))

def exe_7():
    m = int(input())
    m_set = set(map(int, input().split()))
    n = int(input())
    n_set = set(map(int, input().split()))
    m_n_intersection_set = m_set.intersection(n_set)
    print (len(m_n_intersection_set))

def exe_8():
    m = int(input())
    m_set = set(map(int, input().split()))
    n = int(input())
    n_set = set(map(int, input().split()))
    m_n_difference_set = m_set.difference(n_set)
    print (len(m_n_difference_set))

def exe_9():
    m = int(input())
    m_set = set(map(int, input().split()))
    n = int(input())
    n_set = set(map(int, input().split()))
    m_n_sym_difference_set = m_set.symmetric_difference(n_set)
    print ("{} {}".format(m_n_sym_difference_set,len(m_n_sym_difference_set)))

def exe_10():
    n = int(input())
    s = set(map(int, input().split()))
    commands = int(input())

    for i in range(commands):
        command, n = input().split()
        n = int(n)
        s1 = set(map(int, input().split()))
        if command == "update":
            s.update (s1)
            print (s)
        if command == "intersection_update":
            s.intersection_update (s1)
            print (s)
        if command == "difference_update":
            s.difference_update(s1)
            print (s)
        if command == "symmetric_difference_update":
            s.symmetric_difference_update(s1)
            print (s)
    sum = 0
    for i in s:
        sum += i
    print(sum)
if __name__ == "__main__":
    #exe_9()
    A = set([])
    B = set([])
    A.add("1")
    B.add("2")
    C = set()
    C = A.union(B)
    print (C)
    a = set([10,9,8,7])
    b = set([7,6,5,4])
    c = set()
    c = a.union(b)
    print (c)
    c = a.intersection(b)
    print (c)
