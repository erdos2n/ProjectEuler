"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from time import time
from used_functions import isDeficient, isAbundant
from itertools import product, permutations, combinations_with_replacement


def get_non_abundant_list(n)->list:
    non_abundant_list = []
    for number in range(1, n + 1):
        if isDeficient(number):
            non_abundant_list.append(number)
    return non_abundant_list


def get_abundant_list(n)->list:
    abundant_list = []
    for number in range(1, n + 1):
        if isAbundant(number):
            abundant_list.append(number)
    return abundant_list


def sum_abundant_number(n):
    check_list = set()
    pairs_list = get_abundant_list(n)
    for p in combinations_with_replacement(pairs_list, 2):
        if sum(p) <= n:
            check_list.add(sum(p))
    print(check_list)
    return sum(check_list)


def sum_non_abundant_number(n):
    non_abundant_sum = 0
    for number in range(1, n + 1):
        if isDeficient(number):
            non_abundant_sum += number
    return non_abundant_sum


def sum_pairs_non_abundant(n):
    check_list = set()
    pairs_list = get_non_abundant_list(n)
    for p in combinations_with_replacement(pairs_list, 2):
        if sum(p)<=n:
            check_list.add(sum(p))
    print(check_list)
    return None


def get_non_abundant_sum(n):
    total_list = sum(range(1, n + 1))
    sum_of_abundant = sum_abundant_number(n)
    print(total_list, sum_of_abundant)
    return total_list - sum_of_abundant


def get_abundant_sum_final(n):
    total_set = set(range(1, n))
    abundant_pairs = get_abundant_list(n)
    for p in combinations_with_replacement(abundant_pairs, 2):
        s = sum(p)
        if s<=n:
            try:
                total_set.remove(s)
            except KeyError as e:
                continue
    return sum(total_set)



if __name__ == "__main__":
    start = time()
    print(get_abundant_sum_final(28123))
    print(start - time())
