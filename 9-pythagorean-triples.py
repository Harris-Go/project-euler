for a in range(1000):
    for b in range(1000):
        if (a ** 2) + (b ** 2) == (1000 - b - a) ** 2 and a < b:
                print(a * b * (1000 - a - b))
