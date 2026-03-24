temp = int(input("Enter Temperature: "))
if temp in range(25,50):
    print("Warm")
elif temp > 100 or temp in range(51,100):
    print("Hot")
else:
    print("Cold")