"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    return s[len(s) - 2:] + s[2:len(s) - 2] + s[:2] if len(s) >= 4 else s[::-1]


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    """
    oriignal_leave = leave_count
    original_take = take_count
    new_str = str()

    for i in range(len(text)):
        if leave_count > 0:
            leave_count -= 1
            continue

        if leave_count == 0 and take_count == 0:
            continue

        new_str += text[i]

        take_count -= 1

        if leave_count == 0 and take_count == 0:
            take_count = original_take
            leave_count = oriignal_leave

    return new_str


def min_diff(nums):
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    best = 999999999999

    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i == j:
                continue

            diff = abs(num - num2)

            if best > diff:
                best = diff

    return best


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    result = dict()

    for c in text:
        count = text.count(c)

        if count in result:
            if c not in result[count]:
                result[count] += [c]
        else:
            result[count] = [c]

    return result


if __name__ == '__main__':
    print(switch_lasts_and_firsts("ambulance"))  # = > "cebulanam"
    print(switch_lasts_and_firsts("firetruck"))  # = > "ckretrufi"
    print(switch_lasts_and_firsts("car"))  # = > "rac"
    print()

    print(take_partial("abcdef", 2, 3))  # = > "cde"
    print(take_partial("abcdef", 0, 1))  # = > "abcdef"
    print(take_partial("abcdef", 1, 0))  # = > ""
    print()

    print(min_diff([1, 2, 3]))  # = > 1
    print(min_diff([1, 9, 17]))  # = > 8
    print(min_diff([100, 90]))  # = > 10
    print(min_diff([1, 100, 1000, 1]))  # = > 0
    print()

    print(get_symbols_by_occurrences("hello"))  # = > {1: ['e', 'o', 'h'], 2: ['l']}
    print(get_symbols_by_occurrences("abcaba"))  # = > {2: ['b'], 1: ['c'], 3: ['a']}
