'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers
'''

def is_palindrome(num):
    word = str(num)
    if word == word[::-1]:
        return True
    return False

largest = 0
for i in range(999, 100, -1):
    for j in range(999, i, -1):
        new = i * j
        if new > largest and is_palindrome(new):
            largest = new
print(largest)

