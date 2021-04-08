from dataclasses import dataclass, field


@dataclass
class C:
	a: float
	b: float
	# c: float = field(init=False)
	# d: float = field(init=False)

	def __post_init__(self):
		self.c = self.a + self.b
		self.d = self.a * self.b
		self.e = self.a - self.b


my_c = C(1, 2)
print(my_c.c)
print(my_c.d)
print(my_c.e)