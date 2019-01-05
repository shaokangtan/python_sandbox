'''
Anagram Check problem
'''
'''
sort two strings, and compare two sorted strings
Big (O) is 2 * the sort Big (O)
'''
def is_anagram_2(string1, string2):
    words = list(string1.split())
    list1 = []
    for word in words:
        list1.extend(list(word))
    words = list(string2.split())
    list2 = []
    for word in words:
        list2.extend(list(word))

    list1.sort()
    print (list1)
    list2.sort()
    print (list2)
    if list1 == list2:
        return True
    else:
        return False

# Big (O) is N if using dictionary
def is_anagram(string1, string2):
    words = list(string1.split())
    list1 = {}
    for word in words:
        for letter in word:
            if letter in list1:
                list1[letter] += 1
            else:
                list1[letter] = 1

    words = list(string2.split())

    for word in words:
        for letter in word:
            if letter in list1:
                if list1[letter] == 1:
                    list1.pop(letter)
                else:
                    list1[letter] -= 1
            else:
                return False

    if len(list1) > 0:
        return False
    else:
        return True

def test_is_anagram():
    print(is_anagram('clint eastwood','old west action'))
    print(is_anagram('dog','god'))
    print (is_anagram('aa','bb') )

# test_is_anagram()

'''
Array Pair Sum problem
'''
from nose.tools import assert_equal


def pair_sum(array, sum):
    match = 0
    match_list =  []
    for i in range (len(array)):
        #if array[i] > sum: the input could be -1 !!!
        #    continue

        for j in range (i + 1, len(array)):
            if (array [i] + array [j]) == sum:
                found = False
                for match_pair in match_list:
                    if [array[i], array[j]] == match_pair or [array[j], array[i]] == match_pair:
                        found = True
                        break
                if not found:
                    match += 1
                    match_list.append ([array[i], array[j]])

    print (match_list)
    return match

def test_array_pair_sum():
    from nose.tools import assert_equal

    class TestPair(object):

        def test(self,sol):
            assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
            assert_equal(sol([1,2,3,1],3),1)
            assert_equal(sol([1,3,2,2],4),2)
            print ('ALL TEST CASES PASSED')

    #Run tests
    t = TestPair()
    t.test(pair_sum)

#test_array_pair_sum()

'''
find missing element
def finder(arr1,arr2):
    
    pass
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
finder(arr1,arr2)

'''
def finder (arr1, arr2):
    map1 = {}
    for i in arr1:
        if i in map1:
            map1[i] += 1
        else:
            map1[i] = 1
    for i in arr2:
        if i in map1:
            if map1[i] == 1:
                map1.pop(i)
            else:
                map1[i] -= 1
        else:
            print ("error")

    missing = []
    for key, value in map1.items():
        for i in range(value): # if there are duplicated numbers
            #print ( "{} ".format(key), end="" )
            return key
            missing.append(key)

def test_finder():
    class TestFinder(object):

        def test(self,sol):
            assert_equal(sol([5,5,7,7],[5,7,7]),5)
            assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
            assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
            print ('ALL TEST CASES PASSED')

    # Run test
    t = TestFinder()
    t.test(finder)

#test_finder()

def large_cont_sum(arr):
    sum = arr[0]
    max = arr[0]
    start = 0
    for i in range (1, len(arr)):
        if sum < 0:
            if arr[i] > sum:
                #sum = arr[i]
                start = i
            sum = arr[i]
        else:
            sum +=  arr[i]
        if sum > max:
            max = sum
            end = i
    print ("{} {} {} ".format(start, end, max) )
    return max


def test_larger_cont_sum():
    class LargeContTest(object):
        def test(self,sol):
            assert_equal(sol([1,2,-1,3,4,-1]),9)
            assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
            assert_equal(sol([-1,1]),1)
            print ('ALL TEST CASES PASSED')

    #Run Test
    t = LargeContTest()
    t.test(large_cont_sum)

#test_larger_cont_sum()

'''
Sentence Reversal
'''
def rev_word(sentence):
    word_list = sentence.split()
    ans = ""
    for i in range(len(word_list), 0, -1):
        ans += word_list[i-1]
        if i > 1:
            ans += " "
    return ans
    # or
    #return " ".join(reversed(word_list))


def test_rev_word():
    class ReversalTest(object):
        def test(self,sol):
            assert_equal(sol('    space before'),'before space')
            assert_equal(sol('space after     '),'after space')
            assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
            assert_equal(sol('1'),'1')
            print ("ALL TEST CASES PASSED")
        # Run and test
    t = ReversalTest()
    t.test(rev_word)

#test_rev_word()

def compress(stream):
    run_length = 0
    code = ''
    compressed_stream = ""
    for i in stream:
        if code != i :
            if run_length :
                compressed_stream += code;
                compressed_stream += str(run_length)
            code = i
            run_length = 1
        else:
            run_length += 1

    if run_length:
        compressed_stream += code;
        compressed_stream +=  str(run_length)
    print (compressed_stream)
    return compressed_stream

def test_compress():

    class TestCompress(object):

        def test(self, sol):
            assert_equal(sol(''), '')
            assert_equal(sol('AABBCC'), 'A2B2C2')
            assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
            print ('ALL TEST CASES PASSED')

    # Run Tests
    t = TestCompress()
    t.test(compress)

#test_compress()

"""
RUN THIS CELL TO TEST YOUR CODE>
"""
def uni_char(sentence):
    dict = set()
    for i in sentence:
        if i == ' ':
            continue
        if i in dict:
            return False
        else:
            dict.add(i)
    return True

def test_unique():
    class TestUnique(object):

        def test(self, sol):
            assert_equal(sol(''), True)
            assert_equal(sol('goo'), False)
            assert_equal(sol('abcdefg'), True)
            print ('ALL TEST CASES PASSED')

    # Run Tests
    t = TestUnique()
    t.test(uni_char)


test_unique()