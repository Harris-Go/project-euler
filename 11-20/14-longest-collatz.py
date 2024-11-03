best = [0,0]
for number in range(1000000):
    number += 1
    temp = number
    count = 1
    while True:
        if temp % 2 == 0:
            temp = temp/2
            count+=1
        else:
            if temp == 1:
                break
            else:
                temp = (3 * temp) + 1
                count+=1
    if count >= best[1]:
        best[0] = number
        best[1] = count

print(best)
