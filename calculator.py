#https://github.com/kgreen5-art/lab11
#Partner 1: Kaesi Green
# Partner 2: Kai West
# First example
import math
def add(a, b):
    return a +b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b
def logarithm(a,b):
    if a<= 0:
        raise ValueError
    if b<= 0:
        raise ValueError
    return math.log(b, a)
def exponent(a,b):
    return a**b





