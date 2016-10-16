'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143 ?
'''

import math

def naiveFindLargestPrimeFactor(n):
    maxFactor = int(math.ceil(math.sqrt(n)))
    for i in range(maxFactor, 1, -1):
        if n % i == 0:
            if naiveFindLargestPrimeFactor(i) == i:
                return i
    return n

def smarter_find_largest_prime_factor(num):
    max_factor = int(math.ceil(math.sqrt(num)))
    for factor in range(2, max_factor):
        if check_if_factor(num, factor):
            if factor == num:
                return factor
            num = num/factor

    # num itself is prime
    return num

def check_if_factor(x, y):
    if x % y == 0:
        return True
    return False

num = 600851475143

#print(naiveFindLargestPrimeFactor(num))
print(smarter_find_largest_prime_factor(num))


