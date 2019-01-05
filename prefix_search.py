class node :
    def __init__(self, data=None):
       self.key= data
       self.frequency = 0 #  > 1if this node is being used for a word
       self.word = 0   # > 1 if this is a complete word
       self.children = {}
    def node(self, data):
        self.key = data


# think the corner case where you could have duplicate word !
class dictionary:
    def __init__(self):
         self.head = node(None)

    def add_word(self, word):
        h = self.head
        for l in word:
            if l in h.children:
                # keep looking down the tree
                h = h.children[l]
                h.frequency +=1
            else:
                #populate the complete word in the tree
                n = node(l)
                n.frequency = 1
                h.children[l] = n
                h = n

        h.word += 1
        if h.word> 1:
            print ("Warning: duplicate word: {}".format(word))
        return True

    def find_prefix(self,prefix):
        h = self.head
        for l in prefix:
            if l in h.children:
                # keep looking down the tree
                h = h.children[l]
            else:
                return False
        return True

    def find_word(self, word):
        h = self.head
        for l in word:
            if l in h.children:
                # keep looking down the tree
                h = h.children[l]
            else:
                return False
        if h.word:
            return True
        else:
            return False

    def remove_word(self, word):
        h = self.head
        for l in word:
            n = h.children[l]
            if n == None:
                return False
            n.frequency -= 1
            if n.frequency == 0:
                #remove the node if it is no longer used by other words
                h.children.pop(l)
            h = n
        h.word -= 1
        return True

    def print_dictionrary(self): # depth first search
        word = []
        self.print_dictionrary_helper(word, self.head)


    def print_dictionrary_helper(self, word, h):
        if h.key != None:
            word.append(h.key)
        if len(h.children) == 0:
            print ("".join(word))
            return
        for c in h.children.values():
            self.print_dictionrary_helper(word, c)
            word.pop()
        if h.word:
            print ("".join(word))


d = dictionary()

words = ["hello", "how", "are", "you", "yourself", "dictionary"]
for w in words:
    d.add_word(w)

d.print_dictionrary()

print("%d"%(d.find_prefix("dict")))
print("%d"%(d.find_prefix("how1")))

print ("{}".format(d.find_word("you")))
d.add_word("you")
d.add_word("your")
d.add_word("yours")
print ("{}".format(d.find_word("you")))

d.remove_word("you")
d.print_dictionrary()
d.remove_word("yourself")
d.print_dictionrary()