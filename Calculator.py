import math

print("1. sqrt")
print("2. sin")
print("3. cos")
print("4. tan")
print("5. cot")
print("6. factorial")

choice = int(input("Choose: "))

if choice == 1:
    x = float(input("Enter number: "))
    print("Result:", math.sqrt(x))

elif choice == 2:
    deg = float(input("Enter degree: "))
    rad = math.radians(deg)
    print("Result:", math.sin(rad))

elif choice == 3:
    deg = float(input("Enter degree: "))
    rad = math.radians(deg)
    print("Result:", math.cos(rad))

elif choice == 4:
    deg = float(input("Enter degree: "))
    rad = math.radians(deg)
    print("Result:", math.tan(rad))

elif choice == 5:
    deg = float(input("Enter degree: "))
    rad = math.radians(deg)
    print("Result:", 1 / math.tan(rad))

elif choice == 6:
    n = int(input("Enter number: "))
    print("Result:", math.factorial(n))

else:
    print("Invalid choice")
