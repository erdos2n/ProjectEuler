"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from used_functions import is_prime
print(sum(i for i in range(2, 2000000) if is_prime(i)))