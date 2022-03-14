"""Solutions."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if (5 <= time <= 17) and coffee_needed:
        return True

    if 18 <= time <= 24:
        return True

    return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    if a == b == c:
        return 5
    if a != b and a != c:
        return 1

    return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if small_baskets + big_baskets * 5 < ordered_amount:
        return -1

    while ordered_amount >= 5 and big_baskets:
        ordered_amount -= 5
        big_baskets -= 1

    count = 0

    if small_baskets >= ordered_amount:
        while ordered_amount > 0:
            ordered_amount -= 1
            small_baskets -= 1
            count += 1
    else:
        return -1

    return count


if __name__ == '__main__':
    print(students_study(19, False))
    print(students_study(1, True))

    print(lottery(5, 5, 5))
    print(lottery(2, 2, 1))
    print(lottery(2, 3, 1))

    print(fruit_order(14, 1, 15))
    print(fruit_order(3, 1, 10))
