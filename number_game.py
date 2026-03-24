# Check number is Positive or Negative

num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

if num %2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

if num % 5 ==0 and num % 3 ==0: 
    print("Number is Divisible by 5 and 3")
else:
    print("Number is not Divisible by 5 and 3")