# check alpha are between a and m or n and z

char = str(input("Enter character: ").lower())

if "a" <= char <= "m":
    print("Character is between a and m")
elif "n" <= char <= "z":
    print("Character is between n and z")
else:
    print("Character is not between a and m or n and z")