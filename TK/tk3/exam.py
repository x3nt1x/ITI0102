"""TK 3."""


def make_ends(nums: list) -> list:
    """
    Given an array of ints, return a new array length 2 containing the first and last elements from the original array.

    The original array will be length 1 or more.

    make_ends([1, 2, 3]) → [1, 3]
    make_ends([1, 2, 3, 4]) → [1, 4]
    make_ends([7, 4, 6, 2]) → [7, 2]

    :param nums: List of integers.
    :return: List with the first and the last element from the input list.
    """
    return [nums[0], nums[len(nums) - 1]]


def is_sum_of_two(a: int, b: int, c: int) -> bool:
    """
    Whether one parameter is a sum of other two.

    is_sum_of_two(3, 2, 1) => True
    is_sum_of_two(3, 1, 1) => False
    is_sum_of_two(3, 2, 5) => True
    """
    test1 = a + b
    test2 = a + c
    test3 = b + c

    if test1 == c or test2 == b or test3 == a:
        return True

    return False


def first_half(text: str) -> str:
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    size = int(len(text) / 2)
    return text[0:size]


def non_decreasing_list(nums: list) -> bool:
    """
    Given a list of numbers.

    If given list is a non-decreasing list, return True, otherwise False.
    Non-decreasing means every next element in the list must not be smaller than the previous one.

    non_decreasing_list([0, 1, 2, 3, 98]) => True
    non_decreasing_list([50, 49]) => False
    non_decreasing_list([12, 12]) => True

    :param nums:
    :return:
    """
    new_list = []

    for num in nums:
        for num2 in new_list:
            if num < num2:
                return False

        new_list.append(num)

    return True


def mirror_ends(s: str) -> str:
    """
    Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string.

    In other words, zero or more characters at the very beginning of the given string,
    and at the very end of the string in reverse order (possibly overlapping).

    For example, the string "abXYZba" has the mirror end "ab".

    mirrorEnds("abXYZba") → "ab"
    mirrorEnds("abca") → "a"
    mirrorEnds("aba") → "aba"

    :param s: String
    :return: Mirror image string
    """
    new_string = ""
    i = -1
    for c in s:
        if c == s[i]:
            new_string += c
            i -= 1
        else:
            break

    return new_string


if __name__ == '__main__':
    print(make_ends([1, 2, 3]))  # [1, 3]
    print(make_ends([1, 2, 3, 4]))  # [1, 4]
    print(make_ends([7, 4, 6, 2]))  # [7, 2]
    print()

    print(is_sum_of_two(3, 2, 1))  # True
    print(is_sum_of_two(3, 1, 1))  # False
    print(is_sum_of_two(3, 2, 5))  # True
    print()

    print(first_half('HaaHoo'))  # 'Haa'
    print(first_half('HelloThere'))  # 'Hello'
    print(first_half('abcdef'))  # 'abc'
    print()

    print(non_decreasing_list([0, 1, 2, 3, 98]))  # True
    print(non_decreasing_list([50, 49]))  # False
    print(non_decreasing_list([12, 12]))  # True
    print()

    print(mirror_ends("abXYZba"))  # "ab"
    print(mirror_ends("abca"))  # "a"
    print(mirror_ends("aba"))  # "aba"
