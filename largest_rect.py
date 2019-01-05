import sys

"""
test data:
5
1 2 3 4 5

9
1 2 3 4 5 4 3 2 1

10
1 2 3 4 5 0 4 3 2 1

5
6873 7005 1372 5438 1323

6
6873 7005 1372 5438 1323 9238

7
6873 7005 1372 5438 1323 9238 9184 

8
6873 7005 1372 5438 1323 9238 9184 2396

100
6873 7005 1372 5438 1323 9238 9184 2396 4605 162 7170 9421 4012 5302 6277 2438 4409 3391 4956 4488 622 9365 5088 6926 2691 6909 1050 2824 3538 5801 8468 411 9158 9841 2201 481 5431 1385 2877 36 1547 48 5809 1911 1702 8439 4349 6111 1830 5657 6951 8804 5022 8391 2083 7713 5300 3133 6890 5190 5286 1710 1953 4445 7903 4154 4926 3335 5539 4156 9723 3438 556 1885 5349 2258 324 6050 4722 8506 1707 1673 7310 3081 65 9393 7147 1717 8878 389 6908 4165 2099 5213 8610 3 9368 3536 9690 1259
expected: 51060

10
6873 7005 1372 5438 1323 9238 9184 2396 4605 162

"""


def largestRectangle(h):
    # Complete this function
    stack = []
    max_rect = 0
    blocks =0
    if len(h) == 0:
        return max_rect
    max_rect = h[0]
    if len(h) == 1:
        return max_rect
    h.append(0)
    stack.append([0, h[0]])
    for i in range(1, len(h)):
        if len(stack)==0:
            stack.append([i, h[i]])
            continue
        i1, h1 = stack[-1]
        if h[i] == h1:
            continue
        if h[i] > h1:
            stack.append([i,h[i]])
        else:
            # remove element in stack where h  > h[i]
            i1,h1 = stack.pop()
            while len(stack) and h1 >= h[i]:
                max_rect = max(max_rect, (i - i1) * h1)
                i2, h2 = stack[-1]
                if h2 < h[i]:
                    stack.append([i1, h[i]])
                    break
                i1, h1 = stack.pop()

            if len(stack) == 0:
                blocks += 1
                max_rect = max(max_rect,(i - i1) * h1)
                stack.append([0,h[i]])
    #print ("no. of min. blocks {}".format(blocks))
    return max_rect


def largestRectangle_min_blocks(h):
# Complete this function
    stack = []
    max_rect = 0
    blocks =0
    if len(h) == 0:
        return max_rect
    max_rect = h[0]
    if len(h) == 1:
        return max_rect
    h.append(0)
    stack.append([0, h[0]])
    for i in range(1, len(h)):
        if h[i] == h[i-1]:
            continue
        if h[i] > h[i-1]:
            stack.append([i,h[i]])
        else:
            if len(stack)==0:
                stack.append([i, h[i]])
                continue
        # remove element in stack where h  > h[i]
            i1,h1 = stack.pop()
            while len(stack) and h1 > h[i]:
                i2, h2 = stack.pop()
                if h[i] == h2:
                    max_rect = max(max_rect, (i - i1) * (h1 - h[i]))
                    stack.append([i2,h2])
                    blocks += 1
                    break
                if h[i] > h2:
                    max_rect = max(max_rect, (i - i1) * (h1 - h[i]))
                    stack.append([i2,h2])
                    stack.append([i1,h[i]])
                    blocks += 1
                    break
                else:
                    max_rect = max(max_rect, (i - i1) * (h1 - h2))
                    i1, h1 = i2, h2
                    blocks += 1
            if len(stack) == 0:
                blocks += 1
                max_rect = max(max_rect,(i - i1) * (h1 - h[i]))
    print ("no. of min. blocks {}".format(blocks))
    return max_rect


def largestRectangleArea(height):
    increasing, area, i = [], 0, 0
    while i <= len(height):
        if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
            increasing.append(i)
            i += 1
        else:
            last = increasing.pop()
            if not increasing:
                area = max(area, height[last] * i)
            else:
                area = max(area, height[last] * (i - increasing[-1] - 1 ))
    return area

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h)
    print (result)

    result = largestRectangleArea(h)
    print (result)