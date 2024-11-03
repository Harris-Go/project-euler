def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

months = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
        }

number_of_firsts = 0

def calculate_per_year(year, last_sunday):
    global number_of_firsts
    for month, days in months.items():
        if last_sunday % 7 == 0 and year != 1900:
            number_of_firsts += 1
        if month == 'February' and is_leap_year(year):
            last_sunday += (days + 1) % 7
        else:
            last_sunday += days % 7
    return last_sunday

def calculate_total_number():
    last_sunday = 1
    for year_indice in range(1900,2001):
        last_sunday = calculate_per_year(year_indice, last_sunday)
    print(number_of_firsts)

calculate_total_number()
