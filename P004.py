"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from itertools import product

def is_palindrome(n):
	return str(n)==str(n)[::-1]
three_digit_numbers=list(range(100, 1000))
max_=0

for pair in product(three_digit_numbers, repeat=2):
	if is_palindrome(pair[0]*pair[1]) and pair[0]*pair[1]>max_:
		max_=pair[0]*pair[1]
print(max_)