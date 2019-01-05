def solution(A, B):
    # write your code in Python 3.6
    # A is size
    # B is direction, 0 is upstream 1 is downstream
    if len(A) == 0:
        return 0
    total_fish = 0

    downstream_fish=[]
    downstream_fish_removed=[]
    for index in range(0,len(A),1):
        total_fish += 1

        if B[index] == 1:
            # here comes down stream fish
            downstream_fish.append(A[index])
        else:
            # up stream fish
            downstream_fish_removed.clear()
            for size in  downstream_fish :  # any down stream fish ?
                # down stream fish meets up stream fish
                if size > A[index]:
                    # eat up stream fish
                    total_fish -= 1
                    break
                elif size < A[index]:
                    # eat down stream fish
                    total_fish -= 1
                    # remove downstream fish from stack
                    downstream_fish_removed.append(size)
            for  size in downstream_fish_removed:
                downstream_fish.remove(size)


    return total_fish


"""
A[0] = 4    B[0] = 0
A[1] = 3    B[1] = 1
A[2] = 2    B[2] = 0
A[3] = 1    B[3] = 0
A[4] = 5    B[4] = 0
"""
A = [4,3,2,1,5,1,1,1,1,2,3]
B = [0,1,0,0,0,0,0,1,0,1,0]
print (solution(A, B))
