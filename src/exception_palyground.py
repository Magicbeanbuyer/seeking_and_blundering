class Lala:
	def __init__(self, a):
		self.a = a
		self.b = None

my_lala = Lala("aaa", "ccc")
print(my_lala.a)
my_lala.b = "bbb"
print(my_lala.b)