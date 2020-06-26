from math import sqrt

side = int(input())

area = round(2 * sqrt(3) * pow(side, 2), 2)
volume = round(sqrt(2) / 3 * pow(side, 3), 2)

print(area, volume)
