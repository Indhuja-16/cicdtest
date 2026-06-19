def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a/b

def power(a,b):
    return a**b