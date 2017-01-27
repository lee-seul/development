# coding: utf-8
# generator, yield

def generatorEX(n):
    for i in range(n):
        yield i ** 2

gen = generatorEX(4)

for _ in range(4):
    print(next(gen))
