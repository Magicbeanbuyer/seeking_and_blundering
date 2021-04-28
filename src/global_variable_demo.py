"""Demonstrate difference between global and local variable."""
global_var = "a"


def foo():
    """Print local and global vairables."""
    print(f"foo: {global_var}")
