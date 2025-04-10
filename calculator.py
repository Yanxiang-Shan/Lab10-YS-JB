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

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

def logarithm(a,b):
    if b<=0:
        raise ValueError
    return math.log(b,2)

def expo(a,b):
    return a**b

def square_root(a):
    if a<0:
        raise ValueError
    return a**0.5

def hypotenuse(a,b):
    return math.hypot(a,b)


   def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,2),6)
        self.assertEqual(mul(3,4),12)
        self.assertEqual(mul(3,3),9)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(6,2),3)
        self.assertEqual(div(6,4),1.5)
        self.assertEqual(div(6,3),2)