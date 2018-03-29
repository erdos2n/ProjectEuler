"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def count_divisor(n):
	divisorSet=set()
	cap = int(n**0.5)+1
	for i in range(1, cap):
		if n%i==0:
			if i<n:
				divisorSet.add(i)
			if n/i < n:
				divisorSet.add(n/i)
	return int(sum(divisorSet))

def check_amicable(a):
	b = count_divisor(a)
	if a!=b and a == count_divisor(b):
		return a + b
	else:
		return 0

print(sum(check_amicable(i) for i in range(1, 10001))/2)