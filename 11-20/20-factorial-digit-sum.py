fact = 1
def one_hundred_fact():
    global fact
    for numb in range(1,101):
        fact = fact * numb

one_hundred_fact()

fact_list = list(map(int, str(fact)))

total = 0
for number in fact_list:
    total += number

print(total)
