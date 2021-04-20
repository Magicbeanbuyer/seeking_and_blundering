class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} {self.b}"


# modify p_a via p_b
p_a = Point(1, 2)
p_b = p_a
print(p_b is p_a)
print(p_a)
p_b.a = 3
print(p_a)

# delete p_b doesn't delete p_a
del p_b
print(p_a)
