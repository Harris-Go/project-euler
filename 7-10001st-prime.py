import math
primes = 1
z = 2

def is_prime(x):
    for i in range(int(math.sqrt(x))):
        #print(x,i,int(math.sqrt(x)))
        if x % 2 == 0:
            #print("x % 2")
            return False
        if x % (i + 2) == 0:
            #print("x % (i + 1)")
            return False
    return True

while primes != 10001:
    #print(is_prime(z))
    z += 1
    if is_prime(z) == True:
        primes += 1
        #print(primes,z)
print(z)
    
