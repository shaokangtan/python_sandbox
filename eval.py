
def my_eval(input):
    stack = []
    operator = ""
    operators = set(["+", "-", "*", "/"])
    for i in input:
        if i in operators:
            #operator
            operator = i
            stack.append(i)
        else:
            #operand
            if operator == "*":
                operator=""
                stack.pop() # operator
                op = stack.pop()
                result = op * int(i)
                stack.append(result)
            elif  operator == "/":
                operator=""
                stack.pop() # operator
                op = stack.pop()
                result = op // int(i)
                stack.append(result)
            else:
                stack.append(int(i))
    sum = 0
    while len(stack):
        if len(stack) == 1:
            sum += stack.pop()
            return sum
        o1 = stack.pop()
        op = stack.pop()
        o2 = stack.pop()
        if op == "+":
            sum += (o1 + o2)
        elif i == "-":
            sum += (o1 - o2)
        else:
            assert ("error")
    return sum

test1 = ["1", "+", "2", "*", "3"]
test2 = ["4", "/", "2", "*", "3"]
test3 = ["1", "/", "2", "*", "3"]
test4 = ["1", "/", "2", "/", "3"]

assert (my_eval(test1) == 7)
assert (my_eval(test2) == 6)
assert (my_eval(test3) == 0)
assert (my_eval(test4) == 0)