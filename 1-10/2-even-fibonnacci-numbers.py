fib1 = 1
fib2 = 2
total = 2

for i in range(1000000):
    fibtemp = fib1 + fib2
    if fibtemp <= 4000000:
        if fibtemp % 2 == 0:
            total += fibtemp
    fib1 = fib2
    fib2 = fibtemp
print(total)
        
