a = 1


def print_address(var, name):
    print(f"name: {name}, value: {var}, address: {id(var)}")


def zero(x):
    print_address(x, "x")
    x = 0
    print_address(x, "x")


print_address(a, "a")
zero(a)
print_address(a, "a")
print("\n")


def update_list_element(l):
    print_address(l, "l")
    print_address(l[0], "l[0]")
    l[0] = -1
    print_address(l[0], "l[0]")
    print_address(l, "l")


t = [2, 3]
s = t
update_list_element(t)
print_address(t, "t")
print_address(s, "s")
print("\n")


def update_dict_element(d, k, v):
    print_address(d, "d")
    print_address(d[k], "d[k]")
    d[k] = v
    print_address(d, "d")
    print_address(d[k], "d[k]")


y = {1: 1}
u = y
print_address(y, "y")
print_address(u, "u")
update_dict_element(y, 1, 3)
print_address(y, "y")
print_address(u, "u")
print("\n")


class Foo:
    def __init__(self, a):
        self.a = a


f = Foo(1)


def zero_foo(fooo):
    fooo.a = 0

print_address(f, "f")
print_address(f.a, "f.a")
zero_foo(f)
print_address(f, "f")
print_address(f.a, "f.a")
