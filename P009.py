"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from itertools import product
numbers=range(1, 1001)
pyth = lambda x: float(x[0]**2+x[1]**2)**0.5
for pair in product(numbers, repeat=2):
	if pyth(pair)==int(pyth(pair)):
		if sum(pair)+pyth(pair)==1000:
			print(pair[0]*pair[1]*pyth(pair))
			break