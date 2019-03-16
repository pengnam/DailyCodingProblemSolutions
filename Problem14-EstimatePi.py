"""
The area of a circle is defined as (pi)*r^2. Estimate pi to 3 decimal places using a Monte Carlo method.
"""
import random

#I will approximate give r = 1. I will try within x = [0,1], y=[0,1], and check if point in circle (1/4 of a circle)
def solution():
    rounds = 10000000
    count = 0
    for _ in range(rounds):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:
            count += 1

    print(count)
    return ((float(count))/rounds) * 4



print(solution())
