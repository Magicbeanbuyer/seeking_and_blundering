"""Demonstrate difference between global and local variable."""
global_var = "a"
shadow_global_var = "b"


def foo():
    """Print local and global variables."""
    print(f"foo: {global_var}")


def bar():
    """Print local and global variables."""
    global shadow_global_var
    shadow_global_var = shadow_global_var * 2
    print(f"bar: {global_var}\nshadow: {shadow_global_var}")


# try:
foo()
# except UnboundLocalError:
bar()
