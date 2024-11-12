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

#print(f"4+2 = {add(4,2)}")
#print(f"10-3 = {substract(10,3)}")
#print(f"9*3 = {multiply(9,3)}")
#print(f"10*15 = {multiply(10,15)}")
#print(f"7*9 = {multiply(7,9)}")
#print(f"45/5 = {divide(45,5)}")
#print(f"37/2 = {divide(37,2)}")
#print(f"105/7 = {divide(105,7)}")