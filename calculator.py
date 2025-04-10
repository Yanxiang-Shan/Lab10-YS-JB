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

   def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,2),6)
        self.assertEqual(mul(3,4),12)
        self.assertEqual(mul(3,3),9)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(6,2),3)
        self.assertEqual(div(6,4),1.5)
        self.assertEqual(div(6,3),2)