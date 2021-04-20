"""Demonstrate linters."""


def divide(numerator: float, denominator: int) -> float:
    """Divide two numbers.

    Args:
        numerator (float): numerator
        denominator(float): denominator

    Returns:
        float: quotient
    """
    return numerator / denominator


c = divide(5.4, int(0.9))
print(f"value  {c}")
