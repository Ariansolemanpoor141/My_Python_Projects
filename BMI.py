weight = float(input("Weight (kg): "))
height_cm = float(input("Height (cm): "))

height_m = height_cm / 100
bmi = round(weight / (height_m ** 2), 1)

print("bmi:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
