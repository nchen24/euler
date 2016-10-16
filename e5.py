'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import collections

def prime_factorization(n):
    factors = []
    divisor = 2
    while divisor <= n:
        while n / divisor >= 1:
            if n % divisor != 0:
                break
            factors.append(divisor)
            n /= divisor
        divisor += 1
    return factors

def find_smallest_multiple(max):
    nums = [i for i in range(max+1)]
    factors = collections.Counter()
    for num in nums:
        factors |= collections.Counter(prime_factorization(num))
    smallest_multiple = 1
    for k, v in factors.items():
        smallest_multiple *= k**v
    return smallest_multiple

print(find_smallest_multiple(20))
