num = input("Enter the number of  values\n")
if(isinstance(num, int)):
    num = abs(num)
    num = num * (num + 1) /2
    print(num)
else:
    print("Invalid Input")
