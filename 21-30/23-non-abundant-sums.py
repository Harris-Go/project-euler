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
    for each_number in range(1, 1 + int(28123/2)):
        if is_abundant_number(each_number):
            list_of_abundant_numbers.append(each_number)
    return list_of_abundant_numbers

abundant_numbers = list_of_abundant_numbers()
print("Found all abundant numbers")

final_sum = 0
for all_numbers in range(28123):
    for every_number in abundant_numbers:
        if all_numbers // every_number not in abundant_numbers:
            final_sum += all_numbers

print(final_sum)

#final_sum = 0
#for every_number in range(sum_of_all_abundant_numbers[-1]):
#    if every_number not in sum_of_all_abundant_numbers:
#        final_sum += every_number
#
#print(final_sum)
