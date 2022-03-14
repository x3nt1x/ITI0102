"""ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.

    :param text: string
    :return: string
    """
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    id_code = str()

    for c in text:
        if c in numbers:
            id_code += c

    if len(id_code) > 11:
        return "Too many numbers!"
    if len(id_code) < 11:
        return "Not enough numbers!"

    return id_code


def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    return gender_number > 0 and gender_number < 7


def get_gender(gender: int) -> str:
    """
    Get gender.

    :param gender: int
    :return: str
    """
    if gender == 1 or gender == 3 or gender == 5:
        return "male"

    return "female"


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    return year_number >= 0 and year_number < 100


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    return month_number > 0 and month_number < 13


def is_valid_birth_number(birth_number: int) -> bool:
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    return birth_number > 0 and birth_number < 1000


def is_leap_year(year: int) -> bool:
    """
    Check if given value is is leap year.

    :param year: int
    :return: boolean
    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    if birth_number <= 0:
        return "Wrong input!"
    if birth_number <= 10:
        return "Kuressaare"
    if birth_number <= 20 or (birth_number > 270 and birth_number <= 370):
        return "Tartu"
    if birth_number <= 220 or (birth_number > 470 and birth_number <= 710):
        return "Tallinn"
    if birth_number <= 270:
        return "Kohtla-Järve"
    if birth_number <= 420:
        return "Narva"
    if birth_number <= 470:
        return "Pärnu"
    if birth_number < 1000:
        return "undefined"

    return "Wrong input!"


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    if gender_number > 0 and gender_number < 3:
        return 1800 + year_number
    if gender_number > 2 and gender_number < 5:
        return 1900 + year_number
    return 2000 + year_number


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    check = 0

    for i in range(10):
        check += a[i % len(a)] * int(id_code[i])

    check %= 11

    if check < 10:
        return check == int(id_code[10])

    check = 0

    for i in range(2, 12):
        check += a[i % len(a)] * int(id_code[i - 2])

    check %= 11

    if check < 10:
        return check == int(id_code[10])

    return 0 == int(id_code[10])


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    year = get_full_year(gender_number, year_number)
    months = []

    if is_leap_year(year):
        months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    return day_number <= months[month_number]


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    id = find_id_code(id_code)

    if len(id) != 11:
        return False

    gender = int(id[0])
    year = int(id[1:3])
    month = int(id[3:5])
    day = int(id[5:7])
    birth = int(id[7:10])

    if not is_valid_gender_number(gender):
        return False
    if not is_valid_year_number(year):
        return False
    if not is_valid_month_number(month):
        return False
    if not is_valid_day_number(gender, year, month, day):
        return False
    if not is_valid_birth_number(birth):
        return False
    if not is_valid_control_number(id):
        return False

    return True


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    gender_number = int(id_code[0])
    year_number = int(id_code[1:3])
    birth_number = int(id_code[7:10])

    gender = get_gender(gender_number)
    month = id_code[3:5]
    day = id_code[5:7]
    year = get_full_year(gender_number, year_number)
    location = get_birth_place(birth_number)

    if not is_id_valid(id_code):
        return "Given invalid ID code!"

    return f"This is a {gender} born on {day}.{month}.{year} in {location}."


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True

    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"
    print(get_birth_place(11))  # -> "Tallinn"

    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
