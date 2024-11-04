import math

def sum_of_divisors(number):
    divisor_total = 1
    for num in range(2,int(math.sqrt(number))+1):
        if number % num == 0:
            divisor_total += (num + (number // num))
    return divisor_total

total_sum = 0
for numbers in range(1,10000):
    divisor_sum = sum_of_divisors(numbers)
    divisor_sum2 = sum_of_divisors(divisor_sum)
    if divisor_sum2 == numbers and divisor_sum != divisor_sum2:
        total_sum += (numbers)
print(total_sum)
