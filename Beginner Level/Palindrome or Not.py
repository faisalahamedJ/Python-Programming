value = input("Enter the number \n")
rev = 0
temp = value 
if(isinstance(value,int)):
    if(value <= 1000):
        while(value > 0):
            rem = value % 10
            rev = rev*10 + rem
            value //= 10
        if(temp == rev):
            print("Its a Palindrome")
        else:
            print("Its Not a Palindrome")
    else:
        print "Input should be less than or equal to 1000"
else:
    print "Invalid Input"
