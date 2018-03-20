num = input("Enter the number of  values\n")
if(isinstance(num, int)):
    num = num * (num + 1) /2
    print(num)
else:
    print("Invalid Input")
