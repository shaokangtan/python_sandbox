'''
import os, glob,sys
files = []
files = glob.glob(sys.argv[1])
for f in files:
    statinfo  = os.stat(f)    
    if statinfo.st_size < 100000000:
        print ( "{} is less than 1 MB {}".format( f,  statinfo.st_size ))
'''


def prime(n):
        if n < 2:
                return []
        found_prime = [2]
        for i in range(3,n):
                for p in found_prime:
                        if i%p == 0: # is not prime
                                break
                        if p == found_prime[-1]:
                                found_prime.append(i)   
        return found_prime                             
        
print(prime(100))
