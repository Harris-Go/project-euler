import math
cache = {}

def is_prime(numb: int) -> bool:
    for i in range(2, math.ceil(math.sqrt(numb)) + 1):
        if numb % i == 0:
            return False
    return True

def check_prime(numb: int, cache: dict[int: bool] = cache):
    if numb <= 0:
        return False
    elif numb in cache:
        return cache[numb]
    else:
        result = is_prime(numb)
        cache[numb] = result
        return result

def iterate_n(coef_a: int, coef_b: int):
    n: int = 0
    while True:
        result = (n ** 2) + (n * coef_a) + coef_b
        if not check_prime(result):
            return n-1
        n += 1

largest = [0, 0]
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        consecutive_primes = iterate_n(a, b)
        if consecutive_primes > largest[1]:
            largest[0] = a * b
            largest[1] = consecutive_primes

print(largest)
