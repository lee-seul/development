# coding: utf-8
# test_random_1.py

import random

position = 0
walk = [position]
steps = 1000

for i in range(steps):
	step = 1 if random.randint(0, 1) else -1
	position += step
	walk.append(position)
