"""Tests."""
import solution


# Students study tests
def test__student_study__night_coffee_true():
    """Check night coffee true."""
    assert solution.students_study(2, True) is False


def test__student_study__night_coffee_false():
    """Check night coffee false."""
    assert solution.students_study(3, False) is False


def test__student_study__night_edge_case_coffee_true():
    """Check evening edge case coffee true."""
    assert solution.students_study(1, True) is False
    assert solution.students_study(4, True) is False


def test__student_study__night_edge_case_coffee_false():
    """Check evening edge case coffee false."""
    assert solution.students_study(1, False) is False
    assert solution.students_study(4, False) is False


def test__student_study__day_coffee_true():
    """Check day coffee true."""
    assert solution.students_study(14, True) is True


def test__student_study__day_coffee_false():
    """Check day coffee false."""
    assert solution.students_study(12, False) is False


def test__student_study__day_edge_case_coffee_true():
    """Check day edge case coffee true."""
    assert solution.students_study(5, True) is True
    assert solution.students_study(17, True) is True


def test__student_study__day_edge_case_coffee_false():
    """Check day edge case coffee false."""
    assert solution.students_study(5, False) is False
    assert solution.students_study(17, False) is False


def test__student_study__evening_coffee_true():
    """Check evening coffee true."""
    assert solution.students_study(19, True) is True


def test__student_study__evening_coffee_false():
    """Check evening coffee false."""
    assert solution.students_study(19, False) is True


def test__student_study__evening_edge_case_coffee_true():
    """Check evening edge case coffee true."""
    assert solution.students_study(18, True) is True
    assert solution.students_study(24, True) is True


def test__student_study__evening_edge_case_coffee_false():
    """Check evening edge case coffee false."""
    assert solution.students_study(18, False) is True
    assert solution.students_study(24, False) is True


# Lottery tests
def test__lottery__all_fives():
    """Check all fives."""
    assert solution.lottery(5, 5, 5) == 10


def test__lottery__all_same_positive():
    """Check all same positive."""
    assert solution.lottery(3, 3, 3) == 5


def test__lottery__all_same_negative():
    """Check all same negative."""
    assert solution.lottery(-2, -2, -2) == 5


def test__lottery__all_same_zero():
    """Check all same zero."""
    assert solution.lottery(0, 0, 0) == 5


def test__lottery__a_b_same_c_diff():
    """Check a, b same c different."""
    assert solution.lottery(3, 3, 2) == 0


def test__lottery__a_c_same_b_diff():
    """Check a, c same b different."""
    assert solution.lottery(3, 2, 3) == 0


def test__lottery__b_c_same_a_diff():
    """Check b, c same a different."""
    assert solution.lottery(2, 3, 3) == 1


def test__lottery__all_diff():
    """Check all different."""
    assert solution.lottery(2, 5, 3) == 1


# Fruit order tests
def test__fruit_order__all_zero():
    """Check all zero."""
    assert solution.fruit_order(0, 0, 0) == 0


def test__fruit_order__zero_amount_zero_small():
    """Check zero amount zero small."""
    assert solution.fruit_order(0, 5, 0) == 0


def test__fruit_order__zero_amount_zero_big():
    """Check zero amount zero big."""
    assert solution.fruit_order(4, 0, 0) == 0


def test__fruit_order__zero_amount_others_not_zero():
    """Check zero amount others not zero."""
    assert solution.fruit_order(4, 7, 0) == 0


def test__fruit_order__only_big_exact_match():
    """Check only big exact match."""
    assert solution.fruit_order(0, 2, 10) == 0


def test__fruit_order__only_big_not_enough_but_multiple_of_5():
    """Check not enough but multiple of 5."""
    assert solution.fruit_order(0, 2, 15) == -1


def test__fruit_order__only_big_not_enough():
    """Check only big not enough."""
    assert solution.fruit_order(0, 1, 10) == -1


def test__fruit_order__only_big_more_than_required_match():
    """Check only big more than required match."""
    assert solution.fruit_order(0, 5, 15) == 0


def test__fruit_order__only_big_more_than_required_no_match():
    """Check only big more than required no match."""
    assert solution.fruit_order(0, 5, 17) == -1


def test__fruit_order__only_small_match_more_than_5_smalls():
    """Check only small_match_more_than_5_smalls."""
    assert solution.fruit_order(10, 0, 10) == 10


def test__fruit_order__only_small_not_enough_more_than_5_smalls():
    """Check only small not enough more than 5 smalls."""
    assert solution.fruit_order(11, 0, 14) == -1


def test__fruit_order__only_small_exact_match():
    """Check only small exact match."""
    assert solution.fruit_order(11, 0, 11) == 11


def test__fruit_order__only_small_not_enough():
    """Check only small not enough."""
    assert solution.fruit_order(4, 0, 11) == -1


def test__fruit_order__only_small_more_than_required():
    """Check only small more than required."""
    assert solution.fruit_order(15, 0, 7) == 7


def test__fruit_order__match_with_more_than_5_smalls():
    """Check match with more than 5 smalls."""
    assert solution.fruit_order(13, 0, 13) == 13


def test__fruit_order__all_positive_exact_match():
    """Check all positive exact match."""
    assert solution.fruit_order(3, 2, 13) == 3


def test__fruit_order__use_all_smalls_some_bigs():
    """Check use all smalls some bigs."""
    assert solution.fruit_order(3, 5, 13) == 3


def test__fruit_order__use_some_smalls_all_bigs():
    """Check use some smalls all bigs."""
    assert solution.fruit_order(9, 2, 12) == 2


def test__fruit_order__use_some_smalls_some_bigs():
    """Check use some smalls some bigs."""
    assert solution.fruit_order(6, 5, 13) == 3


def test__fruit_order__not_enough():
    """Check not enough."""
    assert solution.fruit_order(6, 1, 16) == -1


def test__fruit_order__enough_bigs_not_enough_smalls():
    """Check enough bigs not enough smalls."""
    assert solution.fruit_order(3, 14, 64) == -1


def test__fruit_order__not_enough_with_more_than_5_smalls():
    """Check not enough with more than 5 smalls."""
    assert solution.fruit_order(7, 1, 18) == -1


def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Check enough bigs not enough smalls large numbers."""
    assert solution.fruit_order(3, 500, 2474) == -1


def test__fruit_order__match_large_numbers():
    """Check match large numbers."""
    assert solution.fruit_order(627, 282, 2034) == 624
