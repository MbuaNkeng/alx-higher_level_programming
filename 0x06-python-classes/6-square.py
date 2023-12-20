#!/usr/bin/python3

"""Define a class Square."""

class Square:
	"""Class that defines a square."""

	def __init__(self, size=0, position=(0, 0)):
		self.size = size
		self.position = position

	@property
	def size(self):
		"""Get/set the current size of the square."""
		return self.__size

	@property
	def position(self):
		"""Get/set the current position of the square."""
		return self.__position
	
	@size.setter
	def size(self, value):
		"""Sets the size of the square with error checks"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		if value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	@position.setter
	def position(self, value):
		"""Sets the position of the square with error checks"""
		if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

	def area(self):
		"""Return the current area of the square."""
		return self.__size ** 2

	def my_print(self):
		"""Print the sqaure with the character #."""
		if self.__size == 0:
			print()
		else:
			print("\n" * self.__position[1], end="")
			for _ in range(self.__size):
				print(" " * self.__position[0] + "#" * self.__size)