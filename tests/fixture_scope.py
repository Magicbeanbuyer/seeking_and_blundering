import pytest


@pytest.fixture
def letter_list():
    return ["a", "b", "c"]


@pytest.fixture(scope="session")
def num_list():
    return [1, 2, 3]


def test_one(letter_list):
    letter_list.append("d")
    assert letter_list == ["a", "b", "c", "d"]


def test_two(letter_list):
    letter_list.append("e")
    assert letter_list == ["a", "b", "c", "e"]


def test_three(num_list):
    num_list.append(4)
    assert num_list == [1, 2, 3, 4]


def test_four(num_list):
    num_list.append(5)
    assert num_list == [1, 2, 3, 5]


def test_five(num_list):
    num_list.append(6)
    assert num_list == [1, 2, 3, 4, 5, 6]  # num 5 was appended at test_four
