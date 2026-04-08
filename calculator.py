"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b):
    return a + b
def sub(a,b):
    return a - b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b ==0:
        raise ZeroDivisionError()
    return a / b
def logarithm(a, b):
    if b <= 0:
        raise ValueError()
    return math.log(a, b)
def exponent(a,b):
    return a ** b