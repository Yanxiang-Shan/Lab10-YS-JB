"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

def logarithm(a,b):
    if b<=0:
        raise ValueError
    return math.log(b,2)

def exponent(a,b):
    return a**b

def square_root(a):
    if a<0:
        raise ValueError
    return a**0.5

def hypotenuse(a,b):
    return math.hypot(a,b)


