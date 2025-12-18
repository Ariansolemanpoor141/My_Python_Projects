import math

r = float(input("Enter radius: "))

area = round(math.pi * r * r, 2)
perimeter = round(2 * math.pi * r, 2)

print("Area:", area)
print("Perimeter:", perimeter)
