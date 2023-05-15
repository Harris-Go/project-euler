import math

def triangle_number(x):
    number=(x*(x+1))/2
    #print("Triangle",number)
    return(int(number))

def divisors(y):
    count = 0
    for i in range(int(math.sqrt(y))):
        i += 1
        #print(i)
        #print(y/i)
        if y/i == i:
            count += 1
            return(count)
        if y%i == 0:
            #print("True")
            count += 2
    return(count)
            

j = 1
while True:
    tri = triangle_number(j)
    number = divisors(tri)
    if number >= 500:
        print(j,tri,number)
        break
    j += 1
    
