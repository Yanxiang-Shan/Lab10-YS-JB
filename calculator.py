"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/Yanxiang-Shan/Lab10-YS-JB.git
#Partner 1: Yanxiang Shan
#Partner 2: Jiya Bhatt

import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input: a must be > 0, b must be > 0 and != 1")
    return math.log(a, b)

def exp(a,b):
    return a**b

def square_root(a):
    if a<0:
        raise ValueError
    return a**0.5

def hypotenuse(a,b):
    return math.hypot(a,b)

