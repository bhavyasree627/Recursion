
def fibonacci_sequence(n):
    if n<2:
        return n
    return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)

print(fibonacci_sequence(10))

def fibonacci_iterative(n):
    a=0
    b=1
    for i in range(n):
        a,b = b,a+b
    return a

print(fibonacci_iterative(10))