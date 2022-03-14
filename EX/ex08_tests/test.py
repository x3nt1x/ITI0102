"""Python testing."""
import solution
# import EX.ex04_lists.lists as solution

data_types = {"int": int, "float": float, "string": str, "list": list, "tuple": tuple, "dict": dict, "set": set}


def test__generate_list__correct_len():
    """Check length."""
    for key in data_types.keys():
        res = solution.generate_list(5, key)
        assert len(res) == 5


def test__generate_list__correct_type():
    """Check type."""
    for key, value in data_types.items():
        res = solution.generate_list(3, key)
        for data in res:
            assert type(data) == value


def test__generate_list__input_zero():
    """Check input 0."""
    for key in data_types.keys():
        res = solution.generate_list(0, key)
        assert len(res) == 0


def test__generate_list__input_big():
    """Check input big."""
    for key in data_types.keys():
        res = solution.generate_list(10000, key)
        assert len(res) == 10000


def test__generate_combined_list__correct_len():
    """Check length."""
    for key in data_types.keys():
        res = solution.generate_combined_list([(3, key), (5, key), (2, key), (4, key)])
        assert len(res) == 5


def test__generate_combined_list__correct_type():
    """Check type."""
    for key, value in data_types.items():
        res = solution.generate_combined_list([(3, key), (5, key), (2, key), (4, key)])
        for data in res:
            assert type(data) == value


def test__generate_combined_list__empty():
    """Check input 0."""
    for key in data_types.keys():
        res = solution.generate_combined_list([(0, key)])
        assert len(res) == 0


def test__generate_combined_list__input_big():
    """Check input big."""
    for key in data_types.keys():
        res = solution.generate_combined_list([(5000, key), (10000, key), (3000, key)])
        assert len(res) == 10000


def test__generate_combined_list_unique__elements_unique():
    """Check elements uniqueness."""
    for key in ["int", "float", "string"]:
        res = solution.generate_combined_list_unique([(1000, key)])
        assert len(res) == len(set(res))


def test__generate_combined_list_unique__list_empty():
    """Check input 0."""
    for key in ["int", "float", "string"]:
        res = solution.generate_combined_list_unique([(0, key)])
        assert len(res) == 0


def test__generate_combined_list_unique__smaller_numbers():
    """Check smaller numbers."""
    for key in ["int", "float", "string"]:
        res = solution.generate_combined_list_unique([(30, key)])
        assert len(res) == 30


def test__generate_combined_list_unique__bigger_numbers():
    """Check bigger numbers."""
    for key in ["int", "float", "string"]:
        res = solution.generate_combined_list_unique([(10000, key)])
        assert len(res) == 10000
