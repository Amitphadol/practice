num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even")
elif num1 % 2 == 0:
    print("{} is even and {} is odd".format(num1, num2))
elif num2 % 2 == 0:
    print("{} is even and {} is odd".format(num2, num1))
else:
    print("Both numbers are odd")