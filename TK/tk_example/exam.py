"""Example TK."""


def workday_count(days):
    """
    Given number of days.

    Return how many of these days are workdays.
    Workdays are first five days of the weeks, last two are not.
    Always start from the start of the week.

    workday_count(9) => 7
    workday_count(3) => 3
    workday_count(7) => 5
    workday_count(15) => 11

    :param days: given number of days
    :return: workdays in given days
    """
    workdays = 0
    temp = 0

    while days > 0:
        temp += 1

        if temp > 5:
            if temp == 7:
                temp = 0
        else:
            workdays += 1

        days -= 1

    return workdays


def sorta_sum(a: int, b: int) -> int:
    """
    Given 2 ints, a and b, return their sum.

    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

    sorta_sum(3, 4) → 7
    sorta_sum(9, 4) → 20
    sorta_sum(10, 11) → 21

    :param a: Integer
    :param b: Integer
    :return: Sum or 20
    """
    sum = a + b

    if 10 <= sum < 20:
        return 20
    else:
        return sum


def extra_end(s: str) -> str:
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.

    The string length will be at least 2.

    extra_end('Hello') → 'lololo'
    extra_end('ab') → 'ababab'
    extra_end('Hi') → 'HiHiHi'

    :param s: Input string
    :return: 3 copies of last 2 chars.
    """
    return s[-2:] * 3


def last_indices_elements_sum(nums):
    """
    Return sum of elements at indices of last two elements.

    Take element at the index of the last element value
    and take element at the index of the previous element value.
    Return the sum of those two elements.

    If the index for an element is out of the list, use 0 instead.

    The list contains at least 2 elements.

    last_indices_elements_sum([0, 1, 2, 0]) => 2 (0 + 2)
    last_indices_elements_sum([0, 1, 1, 7]) => 1 (just 1)
    last_indices_elements_sum([0, 1, 7, 2]) => 7 (just 7)
    last_indices_elements_sum([0, 1, 7, 8]) => 0 (indices too large, 0 + 0)

    :param nums: List of non-negative integers.
    :return: Sum of elements at indices of last two elements.
    """
    nums_length = len(nums)

    if nums_length < 1:
        return 0

    if nums_length == 1:
        return nums[0]

    last_element = nums[-1]
    second_last = nums[-2]

    if nums_length > last_element:
        last_element = nums[last_element]
    else:
        last_element = 0

    if nums_length > second_last:
        second_last = nums[second_last]
    else:
        second_last = 0

    return last_element + second_last


def divisions(numbers: list) -> int:
    """
    You are given a list of unique integers.

    Find how many pairs of numbers there are in that list, such that for each pair, one of it's members is divisible by the other.

    Note that "n and m" is considered the same pair as "m and n".

    divisions([]) => 0
    divisions([5]) => 0

    divisions([3, 14, 12, 6]) => 3 (The pairs are {3, 12}, {3, 6} and {12, 6})
    divisions([2, 3, 8]) => 1 (The only valid pair is {2, 8})
    divisions([25, 22, 4, 400, 50]) => 4 (The pairs are {25, 400}, {25, 50}, {4, 400} and {400, 50})

    divisions([5, 7, 1]) => 2 (The pairs are {5, 1} and {7, 1})

    :param numbers: List of integers
    :return: Amount of pairs
    """
    count = 0
    pairs = dict()

    for i in numbers:
        for num in numbers:
            if num != i:
                if i % num == 0:
                    if (i, num) not in pairs.items():
                        pairs[i] = num
                        count += 1
    return count


if __name__ == '__main__':
    print(workday_count(9))  # 7
    print(workday_count(3))  # 3
    print(workday_count(7))  # 5
    print(workday_count(15))  # 11
    print()

    print(sorta_sum(3, 4))  # 7
    print(sorta_sum(9, 4))  # 20
    print(sorta_sum(10, 11))  # 21
    print()

    print(extra_end('Hello'))  # 'lololo'
    print(extra_end('ab'))  # 'ababab'
    print(extra_end('Hi'))  # 'HiHiHi'
    print()

    print(last_indices_elements_sum([0, 1, 2, 0]))  # 2 (0 + 2)
    print(last_indices_elements_sum([0, 1, 1, 7]))  # 1 (just 1)
    print(last_indices_elements_sum([0, 1, 7, 2]))  # 7 (just 7)
    print(last_indices_elements_sum([0, 1, 7, 8]))  # 0 (indices too large, 0 + 0)
    print()

    print(divisions([]))  # 0
    print(divisions([5]))  # 0
    print(divisions([3, 14, 12, 6]))  # 3 (The pairs are {3, 12}, {3, 6} and {12, 6})
    print(divisions([2, 3, 8]))  # 1 (The only valid pair is {2, 8})
    print(divisions([25, 22, 4, 400, 50]))  # 4 (The pairs are {25, 400}, {25, 50}, {4, 400} and {400, 50})
    print(divisions([5, 7, 1]))  # 2 (The pairs are {5, 1} and {7, 1})
