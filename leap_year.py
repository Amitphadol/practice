
def checkyear(n):
    if n % 4 ==0:
        if n %100==0 and n % 400==0:
            return True
    return False

year = int(input("Enter year: "))
if checkyear(year):
    print("TRUE")
else:
    print("FALSE")