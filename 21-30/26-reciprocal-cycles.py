from decimal import *

LENGTH = 10000

def convert_to_decimal(numb: int) -> int:
    custom_length = LENGTH + 2
    getcontext().prec = custom_length
    getcontext().clear_flags()
    temp = Decimal(1) / Decimal(numb)
    if getcontext().flags[Rounded] == True:
        temp = temp * (10 ** custom_length)
        temp = str(temp).split(".")[0]
    else:
        temp = str(temp).split(".")[1]
    return temp

def calc_cycles(numb: str):
    if len(numb) < LENGTH:
        return(len(numb))
    for start_digit in range(int(LENGTH/6)):
        for digit in range(int(LENGTH/3)):
            true_digit = digit + 1
            item_1 = numb[start_digit:start_digit + true_digit]
            item_2 = numb[start_digit + true_digit:start_digit + (2*true_digit)]
            item_3 = numb[start_digit + (2*true_digit):start_digit + (3*true_digit)]
            if item_1 == item_2 == item_3:
                return(len(item_1))

def main():
    total = [0, 0]
    for i in range(2,1000):
        result = calc_cycles(convert_to_decimal(i))
        print(i, result)
        if result == None:
            print(f"WARNING: {i} returns None")
        elif result > total[1]:
            total = [i, result]
    print(f"RESULT: {total[0]} has the largest cycle of: {total[1]}")
    
if __name__ == "__main__":
    main()
