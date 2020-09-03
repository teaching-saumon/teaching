class Linear(object):
	"""Friteman asked me for this class, so I did it"""
	"""Class which mesures the distance between two points a and b, given in arguments of the class"""
	"""The arguments of the class MUST be either tuples of the same length or floats """
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def change_a(self, new_a):
		self.a = new_a


	def change_b(self, new_b):
		self.b = new_b


	def compute_dist(self):
		if type(self.a) == float and type(self.b) == float:
			return abs(self.a - self.b)

		if type(self.a) == tuple and type(self.b)==tuple:
			if len(self.a)==len(self.b):
				res = 0.
				for i in range(len(self.a)):
					res += (self.b[i] - self.a[i])**2
				return res**(0.5)
			else:
				return 'Wrong dimension'

		elif type(self.a) == float and type(self.b) == tuple or type(self.a) == tuple and type(self.b) == float:
			return 'Wrong dimension'

		else:
			return 'Wrong datatype'
