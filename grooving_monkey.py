from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def find_time(monkeys):
    N = len(monkeys)
    visited = [False] * N
    cycles = []

    for i in range(N):
        if not visited[i]:
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = monkeys[j] - 1  
                length += 1
            cycles.append(length)

   
    return reduce(lcm, cycles)


monkeys = [3,6,5,4,1,2]
print(find_time(monkeys))  
