num = 20
z = 20
for i in range(10):
    while num % (20 - i - 1) != 0:
        num += z
    z = num
    print(i,num)
print("The Answer is: ",num)
