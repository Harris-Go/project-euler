from math import *

number = 2**1000

number = str(number)

total = 0

for i in range(len(number)):
    total = total + int(number[i])

print(total)
