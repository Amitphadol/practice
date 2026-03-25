day_time = input("Enter day time : from 0 - 23 :")
if day_time not in range(0,24):
    print("Invalid Input enter values from 0 to 23")
    exit()

if day_time in range(0,12):
    print("Good Morning")
elif day_time in range(12,17):
    print("Good Afternoon")
elif day_time in range(17,21):
    print("Good Evening")
else:
    print("Good Night")