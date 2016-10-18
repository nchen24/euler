'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
from functools import reduce


## Constant time solution ##
def sum_of_squares(n):
    # More general form can be determined using Faulhaber's Formula
    return int(((2 * (n ** 3)) + (3 * (n ** 2)) + n) / 6)

def sum_to(n):
    return int(((n ** 2) + n)/2)

def square_of_sums(n):
    return sum_to(n) ** 2

def sum_square_difference(n):
    return square_of_sums(n) - sum_of_squares(n)

## List comprehension + map/reduce ##
def naive_sum_square_difference(n):
    sum_of_sq = reduce(lambda x, y: x + y, map(lambda x: x**2, [i for i in range(1, n+1)]))
    sq_of_sum = reduce(lambda x, y: x + y, [i for i in range(1, n+1)]) ** 2
    return sq_of_sum - sum_of_sq

## Naive solution ##
def super_naive_sum_square_difference(n):
    sq_sum = 0
    sum = 0

    for i in range(1, n+1):
        sum += i
        sq_sum += (i**2)

    return (sum**2)-sq_sum

num = 100
#print(super_naive_sum_square_difference(num))
#print(naive_sum_square_difference(num))
print(sum_square_difference(num))

