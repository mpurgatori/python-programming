
def seven():
    for i in range(2000, 3200):
        if (i%7 == 0 and i%5 != 0):
            print (i)

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

def creatDictionary(x):
    numbers = dict()
    for i in range(1, x+1):
        numbers[i] = i*i
    return numbers

print creatDictionary(8)