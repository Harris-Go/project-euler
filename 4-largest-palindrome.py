def is_palindrome(z):
    y=0
    x=z
    while x != 0:
        #print("Y = ",y," X = ",x)
        y = (10 * y) + (x % 10)
        x = int(x / 10)
    if z==y:
        return True
    else:
        return False

highest = 0
for i in range(999):
    if i >= 100:
        for j in range(999):
            if j >= 100:
                test = i * j
                #print(i,j,test)
                if is_palindrome(test) == True:
                    if test > highest:
                        highest = test
                    #print("I = ",i,"J = ",j," and ",test," Is a Palindrome")
            
print(highest)
