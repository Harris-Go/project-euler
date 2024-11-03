import math

def is_prime(x):
    for i in range(int(math.sqrt(x))):
        #print(x,i,int(math.sqrt(x)))
        if x % (i + 2) == 0:
            #print("x % (i + 1)")
            return False
    return True

primes = 0
j = 0
while True:
    j += 1
    if j == 2 or j == 3:
        primes += j
        #print(j, primes)
    if is_prime((6 * j) - 1) == True:
        if ((6 * j) - 1) < 2000000:
            primes += ((6 * j) - 1)
            #print((6 * j) - 1, primes)
        else:
            print(primes)
            break
    if is_prime((6 * j) + 1) == True:
        if ((6 * j) + 1) < 2000000:
            primes += ((6 * j) + 1)
            #print((6 * j) + 1, primes)
        else:
            print(primes)
            break
        
    
