sosq = 0
sqos = 0
for i in range(101):
    sosq += i ** 2
    sqos += i
    print(i,sosq,sqos)
print("Difference: ",(sqos ** 2) - sosq)
