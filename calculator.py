#https://github.com/kgreen5-art/lab11
#Partner 1: Kaesi Green
# Partner 2: Kai West
import math
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a +b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a
def logarithm(a,b):
    if a<= 0:
        raise ValueError
    if b<= 0:
        raise ValueError
    return math.log(b, a)
def exponent(a,b):
    return a**b





