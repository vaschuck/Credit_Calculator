from math import exp

x = int(input())
sigmoid = 1 / (1 + exp(-x))

print(round(sigmoid, 2))
