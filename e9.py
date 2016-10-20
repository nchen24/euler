"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Pythagorean triplets can be generated with Euclid's formula of 
a = m^2 - n^2
b = 2mn
c = m^2 + n^2
for integers m,n s.t. m > n > 0

Ergo, to find the triplet such that a+b+c=1000, we can add these terms to form a
quadratic expression:
a + b + c = (m^2 - n^2) + (2mn) + (m^2 + n^2)
= 2(m^2) + 2mn
= 2m(m + n)
1000 = 2m(m + n)
500 = m(m + n)
"""

def find_pythag_trips(x):
    for m in range(2, x):
        for n in range(1, m):
            if 2 * m * (m + n) == x:
                return (m**2 - n**2, 2*m*n, m**2 + n**2)


trips = find_pythag_trips(1000)
print(trips[0] * trips[1] * trips[2])
