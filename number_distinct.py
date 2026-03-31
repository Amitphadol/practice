# e a 3-digit number and check if all digits are distinct.

num = int(input("Enter a number: ")) # example: 123

if len(str(num)) == 3:
    if len(set(str(num))) == 3:
        print("All digits are distinct.")
    else:
        print("All digits are not distinct.")
else:
    print("Enter a 3-digit number.")