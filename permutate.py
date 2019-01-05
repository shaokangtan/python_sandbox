"""
{A,B,C} subset
            A                                           NULL
    [A,B]               [A,None]                       [B,None]         [None, None]
    [A,B,C] [A,B,None]  [A,None,C] [A, None, None]      [B, None, C] [None, None, C]
"""

class All_SubsetsSolution(object):
    def all_subsets(self, given_array):
        subset = [None]  * len(given_array)
        self.res = []
        self.helper(given_array,subset, 0)
        return self.res


    def helper(self, given_array, subset, i):
        if i == len(given_array):
            print("{}".format(subset))
            # self.res.append(subset) pointer copy wont work !!!
            # Note: make a private copy before append to list. otherwise subset is a pointer and is overwirtten
            self.res.append(subset[:])
        else:
            subset[i] = None # {} empty
            self.helper(given_array, subset, i+1) # recursive on the {} and next element
            subset[i] = given_array[i]  # this element
            self.helper(given_array, subset, i+1) #  recursive on this element and next element

#A = [1,2,3,4,5]
A = list("ABCD")
test = All_SubsetsSolution()
test.all_subsets(A)
print ("{}: total sets: {} \n{}".format(A, len(test.res), test.res))



class Permutate_Solution(object):
    def permute(self, nums):
        res = []
        self._permuteHelper( nums, 0, res)
        return res

    def _permuteHelper(self, nums, start, results):  #helper method
        if start >= len(nums):
            results.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i] # exchange
                self._permuteHelper(nums, start +1, results) # recursive on next element
                nums[start], nums[i] = nums[i], nums[start] # restore

test = Permutate_Solution()
#nums = [1, 2, 3, 4]
nums = list("ABC")
res = test.permute(nums)
print ("{}: total permuatations{}\n{}".format(nums, len(res), res))



def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):

                # Add it to output
                #out += [let + perm]
                # print ("{}, {}, {} ".format(type(out), type(let), type(perm)))
                # print ("append {}".format(let + "".join(perm)))
                out.append([let + "".join(perm)])

    return out

nums = list("ABC")
res = permute(nums)
print ("{}: total permuatations{}\n{}".format(nums, len(res), res))