total = 0
for numb in range(2, 1000000):
    if sum([int(n) ** 5 for n in str(numb)]) == numb:
        total += numb

print(total)



