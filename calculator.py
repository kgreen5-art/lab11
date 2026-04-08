#https://github.com/kgreen5-art/lab11
'''
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
'''
import math

def square_root(a): # raise ValueError if a < 0
    if a<0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):  # can have negative nums
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    return math.log(b, a)# use math library/raise ValueError

def exponent(a, b):
    return a**b

# p2
def add(a, b):
    return a +b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b
def log(a,b):
    if a<= 0:
        raise ValueError
    if b<= 0:
        raise ValueError
    return math.log(b, a)
def exp(a,b):
    return a**b
