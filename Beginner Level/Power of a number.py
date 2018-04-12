num = input("Enter the number ")
power = input("Enter the power value")
if(isinstance((num or power),(int,float))):
    print(pow(num,power))
else:
    print("Invalid Input")
  
