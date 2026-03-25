side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("It's a triangle")
else:
    print("It's not a triangle")
    
if side1 == side2 == side3:
    print("It's an equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It's an isosceles triangle")
else:
    print("It's a scalene triangle")