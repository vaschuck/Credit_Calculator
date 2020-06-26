from math import sqrt

side1 = int(input())
side2 = int(input())
side3 = int(input())

half_perimeter = (side1 + side2 + side3) / 2
area = sqrt(half_perimeter * (half_perimeter - side1)
            * (half_perimeter - side2) * (half_perimeter - side3))

print(area)
