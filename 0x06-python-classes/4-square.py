#!/usr/bin/python3

"""Define a class Square."""

class Square:
	"""Class that defines a square."""

	def __init__(self, size=0):
		self.size = size

	@property
	def size(self):
		"""Retrieves the size of a square"""
		return self.__size

	@size.setter
	def size(self, value):
		"""Sets the size of the square with error checks"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		if value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		"""Returns the current square area"""
		return self.__size ** 2