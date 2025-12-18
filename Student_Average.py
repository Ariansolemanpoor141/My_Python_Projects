firstname = input("Firstname: ")
lastname = input("Lastname: ")

s1 = float(input("Score 1: "))
s2 = float(input("Score 2: "))
s3 = float(input("Score 3: "))

avg = (s1 + s2 + s3) / 3

if avg >= 17:
    print("دانشجوی ممتاز")
elif avg >= 12:
    print("دانشجوی عادی")
else:
    print("دانشجوی مشروط")
