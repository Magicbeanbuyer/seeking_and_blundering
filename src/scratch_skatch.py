"""Demonstrate linters."""
import os


def divide(numerator: float, denominator: int) -> float:
    """Divide two numbers.

    Args:
        numerator (float): numerator
        denominator(float): denominator

    Returns:
        float: quotient
    """
    return numerator / denominator


def print_env():
    env_dict = dict(os.environ)
    print(env_dict)
    return env_dict


if __name__ == "__main__":
    c = divide(5.4, int(1.9))
    print(f"value  {c}")
    print_env()
