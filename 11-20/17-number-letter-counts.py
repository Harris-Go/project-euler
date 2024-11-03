letters = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8}
count = {"And":0, 1000:0}

for j in range(19):
    j += 1
    count[j] = 0
for k in range(10):
    k = (k+1)*10
    count[k] = 0

def hundreds_val(x):
    if x > 99 and x < 1000:
        runningtotal = 0
        hundreds = (x//100)
        runningtotal += letters[hundreds]
        count[hundreds] = count[hundreds] + 1
        runningtotal += letters[100]
        count[100] = count[100] + 1
        if x%100 != 0:
            runningtotal += 3
            count["And"] = count["And"] + 1
        return(runningtotal)
    else:
        return(0)

def tens_val(y):
    runningtotal1 = 0
    if y > 19 and y < 1000:
        if y > 99:
            y = y - ((y//100)*100)
    if y > 19:
        tens = (y//10)*10
        runningtotal1 = letters[tens]
        count[tens] = count[tens] + 1
        return(runningtotal1)
    elif y > 9 and y < 20:
        runningtotal1 = letters[y]
        count[y] = count[y] + 1
        return(runningtotal1)
    else:
        return(0)

def units_val(z):
    runningtotal2 = 0
    if z > 99 and z < 1000:
        z = z - ((z//100)*100)
    if z > 19 and z < 100:
        z = z - ((z//10)*10)
    if z != 0 and z < 10:
        runningtotal2 = letters[z]
        count[z] = count[z] + 1
        return(runningtotal2)
    else:
        return(0)

total = 0
for p in range(1000):
    p += 1
    if p == 1000:
        total = total + letters[1] + letters[1000]
        count[1] = count[1] + 1
        count[1000] = count[1000] + 1
        break
    h_val = hundreds_val(p)
    t_val = tens_val(p)
    u_val = units_val(p)
    numtotal = h_val + t_val + u_val
    total += numtotal
    #print(p,h_val,t_val,u_val,numtotal,total)
print(total)
print(count)




user_input = "q"
#user_input = input("Input Numbers? (y/n)")
if user_input == "y":
    while True:
        number = input("What number? (q)")
        if number == "q":
            print(letters)
            break
        print("How do you spell",number)
        how_many = input()
        count = 0
        for i in range(len(how_many)):
            count += 1
        print(count)
        letters[int(number)] = count
elif user_input == "n":
    total = 0
    tens = 0
    unit = 0
    hundreds = 0
    for h in range(1000):
        semitotal = 0
        h += 1
        if h <= 20:

            total += letters[h]
            
        elif h <= 99:
            
            tens = (h//10)*10
            semitotal += letters[tens]
            
            unit = h%10
            if unit != 0:
                semitotal += letters[unit]
            
        elif h <= 999:
            semitotal += letters[100]
            hundreds = (h//100)
            semitotal += letters[hundreds]
            if h%100 != 0:
                semitotal += 3
            tens = ((h - hundreds*100)//10)*10
            
            if tens != 0:
                semitotal += letters[tens]
            unit = (h - hundreds*100)%10

            if unit != 0:
                semitotal += letters[unit]
                            
            #print(h, hundreds, tens, unit, semitotal, total)
            
        else:
            semitotal += letters[1000]
            semitotal += letters[1]
            
        total += semitotal
        print(h, hundreds, tens, unit, semitotal, total)
    print(total)
