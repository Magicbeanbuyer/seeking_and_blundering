import pytest


@pytest.fixture
def order():
    return []


@pytest.fixture
def outer(order, inner):
    order.append("outer")


# class TestOne:
@pytest.fixture
def inner(order):
    order.append("one")


def test_order(order, outer):
    assert order == ["one", "outer"]


# class TestTwo:
#     @pytest.fixture
#     def inner(self, order):
#         order.append("two")
#
#     def test_order(self, order, outer):
#         assert order == ["two", "outer"]
#
#
# def test_inner_from_outside_a_class(order, outer):
#     assert order == ["outer"]
#     assert order == ["one", "outer"]
#     assert order == ["two", "outer"]
