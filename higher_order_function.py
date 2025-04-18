"""
higher order function, which takes another function as an argument or return a function .
"""

def add(a,b):
    return a + b


def multiply(a,b):
    return a*b


def calculator(a,b,fun):
    return fun(a,b)


print(calculator(10,5,add))


print(calculator(10,5,multiply))