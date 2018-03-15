"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def is_divisible_1_20(n):
	return all(n%i==0 for i in range(1, 21))

num=1000
while True:
	if is_divisible_1_20(num):
		break
	num+=20
print(num)