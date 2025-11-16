sequence = []
for a in range(2, 101):
    for b in range(2, 101):
        result = a ** b
        if result not in sequence:
            sequence.append(result)

print(len(sequence))
