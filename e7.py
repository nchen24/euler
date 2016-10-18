'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math

def estimate_prime_upper_bound(n):
    """Estimate the upper bound for the nth prime using the Prime Number Theorem
    
    Args:
        n (int): The target prime

    Returns:
        int: The integer ceiling of the upper bound for the nth prime
    """
    return math.ceil(n * (math.log(n) + math.log(math.log(n))))

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

def find_prime(n):
    """Find the nth prime

    Args:
        n (int): The target prime

    Returns:
        int: The nth prime
    """
    primes = gen_primes(estimate_prime_upper_bound(n))
    # -1 to account for 0 indexing
    return primes[n-1]

num = 10001
print(find_prime(num))
