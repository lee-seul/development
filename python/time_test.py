
def mul(l):
    result = 1
    for i in l:
        result *= i
    return result 

def factorial(n):
    return mul([i for i in range(n)])

def nn(n):
    return n**n

l = [0, 0, 0]
def time_test(x, y):
    if x > y: 
        l[0] += 1
    elif x < y:
        l[1] += 1
    else:
        l[2] += 1

for i in range(10000000):
    time_test(factorial(i), nn(i))
    print(l)

print(l)

