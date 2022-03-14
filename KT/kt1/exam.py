"""KT1."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string. The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if not s:
        return str()

    return s[0].capitalize() + s[1:]


def has_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    previous = 0

    if nums.count(7) == 3:
        for num in nums:
            if num != previous:
                previous = num
            else:
                return False
    else:
        return False

    return True


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], [], []]
    """
    result = list()

    for _ in range(amount):
        result.append(initial_list)
        initial_list = initial_list[-factor:] + initial_list[:-factor]

    return result


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    data = dict()

    if not call_log:
        return data

    callers = call_log.split(",")

    for caller in callers:
        caller_log = caller.split(":")

        for i, person in enumerate(caller_log):
            if i == len(caller_log) - 1:
                break

            if person in data:
                if caller_log[i + 1] not in data[person]:
                    data[person] += [caller_log[i + 1]]
            else:
                data[person] = [caller_log[i + 1]]

    return data


if __name__ == '__main__':
    print(capitalize_string("abc"))  # = > "Abc"
    print(capitalize_string("ABc"))  # = > "ABc"
    print(capitalize_string(""))  # = > ""
    print()

    print(has_seven([1, 2, 3]))  # = > False
    print(has_seven([7, 1, 7, 7]))  # = > False
    print(has_seven([7, 1, 7, 1, 7]))  # = > True
    print(has_seven([7, 1, 7, 1, 1, 7]))  # = > False
    print()

    print(list_move(["a", "b", "c"], 3, 0))  # = > [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    print(list_move(["a", "b", "c"], 3, 1))  # = > [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    print(list_move([1, 2, 3], 3, 2))  # = > [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    print(list_move([1, 2, 3], 4, 1))  # = > [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    print(list_move([], 3, 4))  # = > [[], [], []]
    print()

    print(parse_call_log(""))  # = > {}
    print(parse_call_log("ago:kati,mati:malle"))  # = > {"ago": ["kati"], "mati": ["malle"]}
    print(parse_call_log("ago:kati,ago:mati,ago:kati"))  # = > {"ago": ["kati", "mati"]}
    print(parse_call_log("ago:kati:mati"))  # = > {"ago": ["kati"], "kati": ["mati"]}
    print(parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati"))  # = > {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}
