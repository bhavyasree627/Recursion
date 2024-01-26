import sys
from Trace_recursion import trace

sys.path.append("..") # Add higher directory to python modules

def factorial(number):
    if number<=0:
        return 1
    return number*factorial(number-1)

print(factorial(1))
print(factorial(0))
print(factorial(-1))
print(factorial(50))
print(factorial(7))