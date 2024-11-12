def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    res = 0
    for _ in range(0,b):
        res += a
    return res

def divide(a,b):
    val = a
    res = 0
    while (val-b>=0):
        val -= b
        res += 1
    return res
