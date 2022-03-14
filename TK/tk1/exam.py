"""TK 1."""


def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) given 112 minutes, return '1h 52min'.
    2) given 23 minutes, return '23min'.
    3) given 180 minutes, return '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    hours = 0

    if minutes < 60:
        return f"{minutes}min"

    while minutes >= 60:
        hours += 1
        minutes -= 60

    if minutes == 0:
        return f"{hours}h"
    else:
        return f"{hours}h {minutes}min"


def lucky_guess(n: int) -> bool:
    """
    Determine whether the given number gives you points for this task or not.

    The number gives you points if it is:
    * either 1, 3 or 7
    * greater or equal than -6 and smaller or equals than 121 and
      divisible by 13 (-6 and 121 are inclusive)
    * smaller than 0 and does not contain number 5 or 6

    print(lucky_guess(7))  # True
    print(lucky_guess(26))  # True
    print(lucky_guess(-35))  # False

    :param n: given number
    :return: boolean - points or no points
    """
    if n == 1 or n == 3 or n == 7:
        return True

    if -6 <= n <= 121:
        if n % 13 == 0:
            return True

    if n < 0:
        for i in str(n):
            if i == str(5) or i == str(6):
                return False
        return True

    return False


def sum_of_a_beach(s: str) -> int:
    """
    Count how many beach elements are in the string.

    Beaches are filled with sand, water, fish, and sun.
    Given a string, calculate how many times the words
    “Sand”, “Water”, “Fish”, and “Sun” appear without
    overlapping (regardless of the case).

    sum_of_a_beach("WAtErSlIde")                    ==>  1
    sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
    sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
    sum_of_a_beach("cItYTowNcARShoW")               ==>  0
    """
    s = s.lower()

    items = ["sand", "water", "fish", "sun"]
    elements = 0

    for item in items:
        elements += s.count(item)

    return elements


def index_index_value(nums: list) -> int:
    """
    Return value at index.

    Take the last element.
    Use the last element value as the index to get another value.
    Use this another value as the index of yet another value.
    Return this yet another value.

    If the the last element points to out of list, return -1.
    If the element at the index of last element points out of the list, return -2.

    All elements in the list are non-negative.

    index_index_value([0]) => 0
    index_index_value([0, 2, 4, 1]) => 4
    index_index_value([0, 2, 6, 2]) => -2  (6 is too high)
    index_index_value([0, 2, 4, 5]) => -1  (5 is too high)

    :param nums: List of integer
    :return: Value at index of value at index of last element's value
    """
    nums_length = len(nums)

    if nums_length < 1:
        return 0

    if nums_length == 1:
        return nums[0]

    last_element = nums[-1]

    if nums_length > last_element:
        last_element = nums[last_element]
    else:
        return -1

    if nums_length > last_element:
        last_element = nums[last_element]
    else:
        return -2

    return last_element


def word_numeration(words: list) -> list:
    """
    For a given list of string, add numeration for every string.

    The input list consists of strings. For every element in the input list,
    the output list adds a numeration after the string.
    The format is as follows: #N, where N starts from 1.
    String comparison should be case-insensitive.
    The case of symbols in string itself in output list should remain the same as in input list.

    The output list has the same amount of elements as the input list.
    For every element in the output list, "#N" is added, where N = 1, 2, 3, ...

    word_numeration(["tere", "tere", "tulemast"]) => ["tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast"]) => ["Tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]) => ["Tere#1", "tere#2", "tulemast#1", "no#1", "tere#3", "TERE#4"]

    :param words: A list of strings.
    :return: List of string with numeration.
    """
    new_list = []
    temp_list = []

    for word in words:
        temp_word = str(word).lower()
        n = temp_list.count(temp_word) + 1
        temp_list.append(temp_word)
        new_list.append(f"{word}#{str(n)}")

    return new_list


if __name__ == '__main__':
    print(format_time(112))  # 1h 52min
    print(format_time(23))  # 23min
    print(format_time(180))  # 3h
    print()

    print(lucky_guess(7))  # True
    print(lucky_guess(26))  # True
    print(lucky_guess(-35))  # False
    print()

    print(sum_of_a_beach("WAtErSlIde"))  # 1
    print(sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN"))  # 3
    print(sum_of_a_beach("gOfIshsunesunFiSh"))  # 4
    print(sum_of_a_beach("cItYTowNcARShoW"))  # 0
    print()

    print(index_index_value([0]))  # 0
    print(index_index_value([0, 2, 4, 1]))  # 4
    print(index_index_value([0, 2, 6, 2]))  # -2 (6 is too high)
    print(index_index_value([0, 2, 4, 5]))  # -1 (5 is too high)
    print()

    print(word_numeration(["tere", "tere", "tulemast"]))  # ["tere#1", "tere#2", "tulemast#1"]
    print(word_numeration(["Tere", "tere", "tulemast"]))  # ["Tere#1", "tere#2", "tulemast#1"]
    print(word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]))  # ["Tere#1", "tere#2", "tulemast#1", "no#1", "tere#3", "TERE#4"]
