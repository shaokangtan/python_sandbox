'''
Check if its empty
Push a new item
Pop an item
Peek at the top item
Return the size
class Stack(object):
'''
class Stack(object):
    def __init__(self):
        self.stack = []
    def Push(self,element):
        self.stack.append(element)
    def Pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()
    def Peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1]
    def size(self):
        return len(self.stack)

def test_Stack():
    stack = Stack()
    for i in range (5):
        stack.Push(i)
    print ("Peek:" + str(stack.Peek()))
    print ("Size:" + str(stack.size()))
    for i in range (6):
        print ("Pop:{}, Size:{}".format(stack.Pop(), stack.size()))
    print (stack.Peek())
    print (stack.size())

#test_Stack()
'''
match parentheses
'''
def is_matched(expression):
    op = ( "[", "(", "{" )
    good_op = ( "[", "(", "{" , ")", "]", "}", " ")
    exp = []
    for i in range (len(expression)):
        if expression[i] not in good_op:
            return False
        if expression[i] == " ":
            continue
        if expression[i] in op:
            exp.append(expression[i])
        else:
            if len(exp) == 0:
                return False
            if expression[i] == "]":
                if exp.pop() != "[":
                    return False
                else:
                    continue
            if expression[i] == ")":
                if exp.pop() != "(":
                    return False
                else:
                    continue
            if expression[i]== "}":
                if exp.pop() != "{":
                    return False
                else:
                    continue
    return True

def is_matched(expression):
    op = ( "[", "(", "{" )
    good_op = ( "[", "(", "{" , ")", "]", "}", " ")
    exp = []
    for i in range (len(expression)):
        if expression[i] not in good_op:
            return False
        if expression[i] == " ":
            continue
        if expression[i] in op:
            exp.append(expression[i])
        else:
            if len(exp) == 0:
                return False
            if expression[i] == "]":
                if exp.pop() != "[":
                    return False
                else:
                    continue
            if expression[i] == ")":
                if exp.pop() != "(":
                    return False
                else:
                    continue
            if expression[i]== "}":
                if exp.pop() != "{":
                    return False
                else:
                    continue
    return True

def is_matched_ruby(expression):
    op = ( "[", "(", "{" )
    good_op = ( "[", "(", "{" , ")", "]", "}", " ", "|")
    exp = []
    for i in range (len(expression)):
        if expression[i] not in good_op:
            return False
        if expression[i] == " ":
            continue
        if expression[i] in op:
            exp.append(expression[i])
        else:
            if  expression[i] != "|"  and len(exp) == 0:
                return False
            if expression[i] == "]":
                if exp.pop() != "[":
                    return False
                else:
                    continue
            if expression[i] == ")":
                if exp.pop() != "(":
                    return False
                else:
                    continue
            if expression[i]== "}":
                if exp.pop() != "{":
                    return False
                else:
                    continue
            if expression[i] == "|":
                if len(exp) and exp[-1] == "|":
                    exp.pop()
                else:
                    exp.append("|")
    for i in range(len(exp)):
        print (exp[i])
    if len(exp):
        return False
    return True

""" tests:
|({()|[]|})|
||||
|||
"""

def test_is_matched():
    t = int(input().strip())

    answer_f = open("c:\\temp\\answer.txt","r")

    for a0 in range(t):
        expression = input().strip()
        if is_matched_ruby(expression) == True:
            ans = "YES"
            print("YES")
        else:
            ans = "NO"
            print("NO")
        ans1 = answer_f.readline()
        if ans1.strip() != ans:
            print ("{}".format(expression))

test_is_matched()