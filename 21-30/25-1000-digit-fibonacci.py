import sys
sys.set_int_max_str_digits(0)

def calculate_fibonacci(start1, start2):
    end = start1 + start2
    start1 = start2
    start2 = end
    return start1, start2

st1 = 1
st2 = 1
index = 1
while True:
    if len(str(st1)) >= 1000:
        print(f"Fibonnaci: {index}, {st1}")
        break
    st1, st2 = calculate_fibonacci(st1, st2)
    index += 1

