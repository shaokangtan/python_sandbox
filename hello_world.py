print("hello world %c" % '!')


class Dog():
    """Represent a dog."""

    def __init__(self, name):
        """Initialize dog object."""
        self.name = name

    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")


class SARDog(Dog):
    """Represent a search dog."""
    def __init__(self, name):
        """Initialize the sardog."""
        super().__init__(name)


    def search(self):
        """Simulate searching."""
        print(self.name + " is searching.")


a = 1
def test ():
    a = 1
v = memoryview(a)
print (v[0])
print (locals()['a'])
print (locals())

my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()

my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()
list = (1,2,3)
print ("list[-3]=%d" % list[-3])
str = "123    "
print ("str=%s !" % str.strip(" "))
hello="hello world"
print ("hello=%s" % hello[3:5])



