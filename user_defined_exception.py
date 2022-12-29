class OurException(Exception):
	def __init__(self, message):
			self.message = message

try:
	a = int(input("a: "))
	b = int(input("b: "))

	if b == 0:
		raise OurException("b should be greater than 0")
	d = a / b
	print("division operation successful with result:", d)
except OurException as err:
	print("user defined exception:", err.message)
