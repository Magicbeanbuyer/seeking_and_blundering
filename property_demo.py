class Person:
	def __init__(self):
		self._first_name = None

	@property
	def first_name(self):
		return self._first_name

	@first_name.setter
	def first_name(self, value):
		self._first_name = value


if __name__ == "__main__":
	me = Person()
	print(me.first_name)
	me.first_name = "xiatong"
	print(me.first_name)
