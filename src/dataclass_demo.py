from dataclasses import dataclass, field, InitVar


class A:
	def __init__(self, a):
		self.a = a


@dataclass
class C(A):
	a: float
	b: float

	# c: float = field(init=False)
    # d: float = field(init=False)

	def __post_init__(self):
		self.c = self.a + self.b
		self.d = self.a * self.b
		self.e = self.a - self.b


class Position:
	def __init__(self, foo):
		self.foo = foo

@dataclass
class Capital(Position):
	a: int
	c: InitVar[int]
	b: str = field(init=False)

	def __post_init__(self, c):
		self.e = c
		super().__init__("lala")
		self.b = self.foo


x = Capital(a=2, c=3)
print(x.__dict__)
x.foo = "booo"
print(x)
print(x.__dict__)
print(x.__dir__)
print(x.__init_subclass__)

# my_c = C(1, 2)
# print(my_c.c)
# print(my_c.d)
# print(my_c.e)
