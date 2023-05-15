import math
x=600851475143
y=x
for i in range(int(math.sqrt(x))):
    if i > 1:
        while y % i == 0:
            print(i)
            if y/i == 1:
                print(i)
                break
            y = y/i
        
