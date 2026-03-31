# Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.

num = int(input("Enter a 3-digit number: "))
if len(str(num)) == 3:
    num_str = str(num)
    num_list = list(map(int, num_str))
    if num_list[1] > num_list[0] and num_list[1] > num_list[2]:
        print("The middle digit is the largest")
    elif num_list[1] < num_list[0] and num_list[1] < num_list[2]:
        print("The middle digit is the smallest")
    else:
        print("The middle digit is neither the largest nor the smallest")
