from nose.tools import assert_equal

def test_rev(sentence):
    if len(sentence) == 1:
        return sentence[0]
    return sentence[-1] + test_rev(sentence[:-2])
    #return test_rev(sentence[1:]) + sentence[0]

def test_reverse():

    class TestReverse(object):

        def test_rev(self,solution):
            assert_equal(solution('hello'),'olleh')
            assert_equal(solution('hello world'),'dlrow olleh')
            assert_equal(solution('123456789'),'987654321')

            print ('PASSED ALL TEST CASES!')

    # Run Tests
    test = TestReverse()
    test.test_rev(reverse)

#test_reverse()

def change_maker(coins, n):
    assert len(coins) > 0
    for i in range(len(coins) -1, -1, -1):
        q = n // coins[i]
        r = n % coins[i]
        if q:
            print ("${}: {}".format(coins[i], q))
        if r == 0:
            return q
        else:
            #print (coins[:-1], sep=" ")
            return  q + change_maker(coins[:-1], r)

def test_change_maker():
    coins = [10,3,2,1]
    coins.sort()
    #print (change_maker(coins, 35))
    #print (change_maker(coins, 100))
    #print (change_maker(coins, 33))
    print (change_maker(coins, 21))

from itertools import permutations
def perm(l):
    # A Python program to print all
    # permutations using library function

    # Get all permutations of [1, 2, 3]
    perm_list = permutations(l)

    # Print the obtained permutations
    for i in list(perm_list):
        print (i)
    perm_list = permutations(l)
    print ("size {}".format(len(list(perm_list))))

#perm([1, 2, 3])
#perm([1, 2, 3, 4])


class Solution(object):
    def permute(self, nums):
        res = []
        self._permuteHelper( nums, 0, res)
        return res

    def _permuteHelper(self, nums, start, results):  #helper method
        if start >= len(nums):
            results.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                self._permuteHelper(nums, start +1, results)
                nums[start], nums[i] = nums[i], nums[start]

s = Solution()
nums = [1, 2, 3, 4]
print (s.permute(nums))

