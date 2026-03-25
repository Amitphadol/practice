num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % num2 ==0 or num2%num1 ==0 :
    print("True number is multiple")
else:
    print("False number is not multiple")