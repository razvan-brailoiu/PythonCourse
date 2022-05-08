months_31_days = [1, 3, 5, 7, 8, 10, 12]
year_prefix = {
    1: "19",
    2: "19",
    3: "18",
    4: "18",
    5: "20",
    6: "20",
    7: "19",
    8: "19",
    9: "19",
}


def get_year(cnp):
    year = int(year_prefix[int(cnp[0])]+cnp[1:3])
    return year


def is_leap_year(year: int):
    if (year % 400 == 0) or (year % 100 !=0 and year % 4 == 0):
        return True
    return False


def check_len(cnp):
    if len(cnp) != 13:
        return False
    return True


def check_county(cnp):
    county = int(cnp[5:7])
    return 1 <= county <= 46 or 51 <= county <= 52


def check_month(cnp):
    month = int(cnp[3:5])
    return 1 <= month <= 12


def check_controldig(cnp):
    checksum = '279146358279'
    sum = 0
    incr = 0
    control_digit_obtained = 0
    for dig in cnp[0:12]:
        sum += int(dig)*int(checksum[incr])
        incr += 1
    sum %= 11
    if sum == 10:
        control_digit_obtained = 1
    else:
        control_digit_obtained = sum

    if control_digit_obtained == int(cnp[12]):
        return True
    else: return False


def check_day(cnp):
    year = get_year(cnp)
    month = int(cnp[3:5])
    day = int(cnp[5:7])
    up_limit = 0
    if month == 2:
        up_limit = 29 if is_leap_year(year) else 28
    else:
        up_limit = 31 if month in months_31_days else 30

    return 1 <= day <= up_limit


def check_all(cnp):
    list_of_validations = [check_day(cnp), check_month(cnp), check_county(cnp), check_controldig(cnp), check_len(cnp)]
    if False in list_of_validations:
        return False
    else: return True


cnp = input("Introduceti un CNP pentru check: ")
print(check_all(cnp))