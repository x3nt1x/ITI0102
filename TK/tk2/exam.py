"""TK 2."""


def rotate_left3(nums):
    """
    Given an array of ints length 3, return an array with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].

    rotate_left3([1, 2, 3]) → [2, 3, 1]
    rotate_left3([5, 11, 9]) → [11, 9, 5]
    rotate_left3([7, 0, 0]) → [0, 0, 7]

    :param nums: List of integers of length 3.
    :return: Rotated list.
    """
    return nums[1:] + nums[:1]


def caught_speeding(speed, is_birthday):
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if speed <= 60:
        return 0

    if is_birthday:
        if speed >= 86:
            return 2
        if 66 <= speed <= 85:
            return 1

        return 0

    if speed > 81:
        return 2

    if 61 <= speed <= 80:
        return 1

    return 0


def without_end(s):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".

    The string length will be at least 2.

    without_end('Hello') → 'ell'
    without_end('java') → 'av'
    without_end('coding') → 'odin'

    :param s: String
    :return: String without first and last char.
    """
    return s[1:len(s) - 1]


def min_index_value(nums: list) -> int:
    """
    Take the first and the last element as indices of two elements and return the smaller of those elements.

    If at least one index is out of range, return -1.
    All the values are non-negative integers.

    min_index_value([1, 2, 3]) => -1 (3 is out of range)
    min_index_value([1, 2, 1]) => 2 (both elements point to 2)
    min_index_value([1, 2, 0]) => 1 (have to take minimum of 2 and 1)

    :param nums: List of non-negative integers.
    :return: Minimum value of two elements at positions of the first and the last element value.
    """
    size = len(nums)
    first = nums[0]
    last = nums[size - 1]

    if size > first:
        first = nums[first]
    else:
        return -1

    if size > last:
        last = nums[last]
    else:
        return -1

    return min(first, last)


def count_clumps(nums: list) -> int:
    """
    Return the number of clumps in the given list.

    Say that a "clump" in a list is a series of 2 or more adjacent elements of the same value.

    count_clumps([1, 2, 2, 3, 4, 4]) → 2
    count_clumps([1, 1, 2, 1, 1]) → 2
    count_clumps([1, 1, 1, 1, 1]) → 1

    :param nums: List of integers.
    :return: Number of clumps.
    """
    size = len(nums)
    clumps = 0
    i = 0

    while i < (size - 1):    
        had_clump = 0
        
        while (i + 1) < size and nums[i] == nums[i + 1]:
            had_clump = 1
            i += 1
 
        if had_clump:
            clumps += 1
             
        i += 1
 
    return clumps


if __name__ == '__main__':
    print(rotate_left3([1, 2, 3]))  # [2, 3, 1]
    print(rotate_left3([5, 11, 9]))  # [11, 9, 5]
    print(rotate_left3([7, 0, 0]))  # [0, 0, 7]
    print()

    print(caught_speeding(60, False))  # 0
    print(caught_speeding(65, False))  # 1
    print(caught_speeding(65, True))  # 0
    print()

    print(without_end('Hello'))  # 'ell'
    print(without_end('java'))  # 'av'
    print(without_end('coding'))  # 'odin'
    print()

    print(min_index_value([1, 2, 3]))  # -1 (3 is out of range)
    print(min_index_value([1, 2, 1]))  # 2 (both elements point to 2)
    print(min_index_value([1, 2, 0]))  # 1 (have to take minimum of 2 and 1)
    print()

    print(count_clumps([1, 2, 2, 3, 4, 4]))  # 2
    print(count_clumps([1, 1, 2, 1, 1]))  # 2
    print(count_clumps([1, 1, 1, 1, 1]))  # 1
