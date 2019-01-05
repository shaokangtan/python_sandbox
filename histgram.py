# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
print ("hi")


class Histgram():
    def __init__(self, min, max, buckets):
        self.min = min
        self.max = max
        self.buckets = buckets
        self.his ={}
        for i in range(buckets):
            self.his[i] = 0
            print (i)

    def add (self, value):
        if value < self.min or value > self.max:
            assert ("input is invalid")
        i = (value-self.min)//self.buckets
        print (i)
        self.his[i] += 1

    def my_print (self):
        for i in range(self.buckets):
            print ("{} - {}: {}".format(self.min, self.max, self.his[i]) )



# edge test
my_histgram=Histgram(0,99,10)
for i in range (0,100):
    my_histgram.add(i)
my_histgram.my_print()

# stress test
my_histgram = histgram(0,99,10)











