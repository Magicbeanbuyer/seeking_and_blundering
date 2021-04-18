class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} {self.b}"


p_a = Point(1, 2)
p_b = p_a
print(p_b is p_a)
print(p_a)
p_b.a = 3
print(p_a)
