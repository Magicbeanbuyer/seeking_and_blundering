"""Scratch and erase."""


def divide(numerator: float, denominator: int) -> float:
    """Divide and conquer.

    Args:
        numerator (float): the dividend
        denominator (int): the divisor, must be integer

    float: the quotient of the division
    """
    return numerator / denominator


c = divide(numerator=3, denominator=int(4.5))
print(c)
