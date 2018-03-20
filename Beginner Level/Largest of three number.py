num1 = input("Enter the first number\n")
num2 = input("Enter the second number\n")
num3 = input("Enter third number\n")
if(num1>=num2):
    if(num1>=num3):
        print(num1, "is Largest")
    else:
        print(num3, "is largest")
elif(num2>=num3):
	      print(num2, "is Largest")
else:
    print(num3, "is Largest")
