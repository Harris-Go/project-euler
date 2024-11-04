import math

def sum_of_divisors(number):
    divisor_total = 1
    for num in range(2,int(math.sqrt(number))+1):
        if number % num == 0:
            divisor_total += (num + (number // num))
    return divisor_total

total_sum = 0
already_found = []
for numbers in range(1,10000):
    divisor_sum = sum_of_divisors(numbers)
    divisor_sum2 = sum_of_divisors(divisor_sum)
    if divisor_sum2 == numbers and divisor_sum != divisor_sum2 and numbers not in already_found:
        already_found.append(divisor_sum)
        print(numbers, divisor_sum, divisor_sum2)
        total_sum += (divisor_sum + divisor_sum2)
print(total_sum)
