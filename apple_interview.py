'''
quiz 1: use one list and no helper method to move 0(s) to the end of list
'''
list_test = [1,2,3,0,5,6,7,0,10,11]


index_z=-1
for i, v in enumerate(list_test):
    if v==0:
        if index_z == -1:
            index_z= i 
    else:
        if index_z != -1:
            list_test[i] ,list_test[index_z ] =  list_test[index_z ], list_test[i] 
            if index_z +1 < len(list_test) and list_test[index_z+1] == 0:
                index_z += 1
            else: 
                index_z = -1    
print (list_test)



'''
quiz 2: design a stack with push, pop and get_min methods
'''

class stack ():
    m_stack = []
    m_stack_min = []
    def __init__(self):
        pass

    def pop(self):
        if len(self.m_stack)==0:
            return None 
        ret =  self.m_stack.pop()  
        if ret == self.m_stack_min[len(self.m_stack_min)-1]:  
            self.m_stack_min.pop()
        return ret 

    def push(self, i):
        self.m_stack.append(i)
        if len(self.m_stack_min)==0:
            self.m_stack_min.append(i)
        else:
            if i <= self.m_stack_min[len(self.m_stack_min)-1]:
                self.m_stack_min.append(i)

    def get_min(self):
        if len(self.m_stack_min) == 0:
            return None
        return self.m_stack_min[len(self.m_stack_min)-1]    

stk = stack()
my_list = [7,6,5,4,2,1,0,2,3,4,5,-1,-1,2,3,4,5,0,5]

for i in my_list:
    stk.push(i)
    print(stk.get_min())

for i in my_list:
    print(stk.pop())
    print(stk.get_min())
