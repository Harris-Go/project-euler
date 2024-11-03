total = 0
for i in range(1000):
    if i % 3 == 0:
        total += i
        print("Yes 3 is a factor of:",i)
    elif i % 5 == 0:
        total += i
        print("Yes 5 is a factor of:",i)
print(total)
