from os import getenv


def divide(numerator: float, denominator: int) -> float:
    """
    Args:
        numerator (float): the dividend
        denominator (int): the divisor, must be integer

    float: the quotient of the division
    """
    return numerator / denominator


c = divide(numerator=3, denominator=int(4.5))
print(c)
