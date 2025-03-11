digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_list = [0, 1, 2]

def generate_next_permutation(digits):

    for indexk in range(len(digits) - 2,-1,-1):
        digitk = digits[indexk]
        if digitk < digits[indexk + 1]:

            for indexl in range(len(digits)-1, indexk, -1):
                digitl = digits[indexl]
                if digitk < digitl:

                    digits[indexk] = digitl
                    digits[indexl] = digitk

                    sub_list = digits[indexk + 1:]
                    digits[indexk + 1:] = sub_list[::-1]

                    return digits

                    


for i in range(999_999):
    digit_list = generate_next_permutation(digit_list)

print(digit_list)
