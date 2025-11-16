total = 1
jumpby = 2
i = 1

while jumpby <= 1000:
    for x in range(4):
        i += jumpby
        total += i
    jumpby += 2

print(total)
