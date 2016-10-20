"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math
from functools import reduce

def gen_primes(limit):
    """Generates a list of primes using the Sieve of Eratosthenes

    Args:
        limit (int): The maximum number to sieve to

    Returns:
        list of int: The list of all primes up to `limit` 
    """
    primes = [True] * limit
    primes[0] = False
    primes[1] = False

    for i in range(2, limit):
        if not primes[i]:
            continue
        for j in range(i ** 2, limit, i):
            primes[j] = False
    return [i for i, j in enumerate(primes) if j]

def find_prime_sum(n):
    """Find the sum of all primes less than n

    Args:
        n (int): The largest prime to sum up to

    Returns:
        int: The sum of all primes less than n

    """
    return reduce(lambda x, y: x+y, gen_primes(n))

num = 2000000
print(find_prime_sum(num))
