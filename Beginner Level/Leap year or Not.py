year = input("Enter the year\n")
if(isinstance(year, int)):
    if(year % 4 == 0):
        if((year % 100 != 0) or (year % 400 == 0)):
            print(year,"is a Leap year")
        else:
            print(year, "is not a Leap year")
    else:
        print(year, "is not a Leap year")
else:
    print("Invalid Input")
