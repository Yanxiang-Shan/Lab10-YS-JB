import math

def add(a,b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm. Base must be >0 and ≠ 1, and argument must be > 0.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

