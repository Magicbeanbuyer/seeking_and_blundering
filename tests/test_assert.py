"""Lean pytest."""
import pytest


def three():
    """Return 3."""
    return 3


def divide(numerator, denominator):
    """Divide two numbers."""
    return numerator / denominator


def raise_value_error(num):
    """Raise error."""
    raise ValueError(f"Exception 123 raised [{num}].")


def test_three():
    """assert."""
    assert three() % 2 == 0, "value was odd, should be even"


def test_divide_by_zero():
    """Use raises as context manager. Assess exception info."""
    with pytest.raises(ZeroDivisionError) as exception_info:
        divide(1, 0)
    assert "division by zero" in str(exception_info.value)


# test expected exception
pytest.raises(ValueError, raise_value_error, 1)
