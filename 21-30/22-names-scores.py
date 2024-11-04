import csv

with open("names.txt", 'r') as csvfile:
    names = csv.reader(csvfile, delimiter=',')
    for row in names:
        list_of_names = row

alphabet_values = {'A':1,
                   'B':2,
                   'C':3,
                   'D':4,
                   'E':5,
                   'F':6,
                   'G':7,
                   'H':8,
                   'I':9,
                   'J':10,
                   'K':11,
                   'L':12,
                   'M':13,
                   'N':14,
                   'O':15,
                   'P':16,
                   'Q':17,
                   'R':18,
                   'S':19,
                   'T':20,
                   'U':21,
                   'V':22,
                   'W':23,
                   'X':24,
                   'Y':25,
                   'Z':26
                   }

list_of_names.sort()

total_sum = 0
for each_name in list_of_names:
    name_sum = 0
    for each_letter in list(each_name):
        name_sum += alphabet_values[each_letter]
    name_sum = name_sum * (1 + list_of_names.index(each_name))
    total_sum += name_sum

print(total_sum)
