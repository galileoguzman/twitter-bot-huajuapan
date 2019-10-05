cadena = "Esto es una cadena"

# print(cadena)

# for c in cadena:
# 	print(c)


class Dog:
	"""
	OOP for a Dog class
	"""
	def __init__(self, name, age):
		self.name = name
		self.age = age


	def say_hello(self):
		return f'Hi I am {self.name}'


# Instance
puppet = Dog("Mr Teodoro", 10)

# Gettter
print(len(puppet.say_hello()))







