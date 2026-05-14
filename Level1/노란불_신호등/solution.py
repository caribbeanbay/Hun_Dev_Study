from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    periods = [G + Y + R for G, Y, R in signals]
    max_t = reduce(lcm, periods)
    
    for t in range(1, max_t + 1):
        if all(G <= (t - 1) % (G + Y + R) < G + Y for G, Y, R in signals):
            return t
    
    return -1