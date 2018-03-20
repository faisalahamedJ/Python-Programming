num = input("Enter the input\n")
if(isinstance(num,(int,float))):
    if(num % 2 == 0):
        print("The given number is Even")
    else:
        print("The given is Odd")
else:
    print("Invalid input")
