import math

def is_abundant_number(test_number):
    total_of_divisors = 1
    for integer in range(2, 1 + int(test_number/2)):
        if test_number % integer == 0:
            total_of_divisors += integer
    if total_of_divisors > test_number:
        return True
    else:
        return False

def list_of_abundant_numbers():
    list_of_abundant_numbers = []
    for each_number in range(1, 28123):
        if is_abundant_number(each_number):
            list_of_abundant_numbers.append(each_number)
    return list_of_abundant_numbers

abundant_numbers = list_of_abundant_numbers()

sums_of_abundant_numbers = []
for i in abundant_numbers:
    for j in abundant_numbers:
        if j >= i:
            sum1 = i + j
            if sum1 < 28123:
                sums_of_abundant_numbers.append(sum1)

sums_of_abundant_numbers.sort()

non_abundant_sum = 0
previous_number = 0
for number in sums_of_abundant_numbers:
    for difference in range(previous_number + 1, number):
        non_abundant_sum += difference
    previous_number = number

print(non_abundant_sum)

