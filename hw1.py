############################################################
# Name: Yahia Abdelsalam
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 HW 1
#  
############################################################
from functools import reduce

def mult(x, y): 
    return x * y
"""Return the product of x and y"""

def factorial(n):
    if n == 0:
        return 1
    return reduce(mult, range(1, n + 1))
"""Returns the factorial of n (n!)"""

def add(x, y):
    return x + y
"""Returns the sum of x and y"""

def mean(L):
    if len(L) == 0: 
        return 0 
    total = reduce(add, L)
    return total / len(L)
"""Returns the mean value in list L"""

print(factorial(5))
print(mean([1, 2, 3]))
print(mean([1, 1, 1]))
