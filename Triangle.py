a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Yes")
else:
    print("No")
