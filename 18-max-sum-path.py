triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

j = 0
row = []
##for i in range(15):
##    number = ""
##    row.append([])
##    while True:
##        selected = triangle[j]
##        if selected != " " and selected != "\n":
##            number = number + selected
##        if selected == " ":
##            row[i].append(int(number))
##            number = ""
##        if selected == "\n":
##            row[i].append(int(number))
##            j += 1
##            break
##        j += 1
##print(row)

pyramid = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

def check_highest_combinations(list1, list2):
    for index1 in range(len(list1)):
        combo1 = list1[index1] + list2[index1]
        combo2 = list1[index1] + list2[index1 + 1]
        if combo1 > combo2:
            list1[index1] = combo1
        else:
            list1[index1] = combo2
    return list1

def largest_combo(pyramid_list):
    for pyramid_level in range(len(pyramid_list) - 1):
        current_level = len(pyramid_list) - (pyramid_level + 2)
        pyramid_list[current_level] = check_highest_combinations(pyramid_list[current_level], pyramid_list[current_level + 1])
    print(pyramid_list[0])

largest_combo(pyramid)
