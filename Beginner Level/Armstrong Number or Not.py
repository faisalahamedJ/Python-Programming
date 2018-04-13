value = input("Enter the number \n")
rev = 0
temp = value
i = temp
power = 0
mult = 0
if(isinstance(value,int)):
    if(value <= 100000):
        while(i > 0):
            power += 1  
            i //= 10
        while(value > 0):
            rem = value % 10
            mult += pow(rem,power)
            value //= 10
        if(temp == mult):
            print("yes ")
        else:
            print("No")
    else:
        print "Input should be less than or equal to 100000"
else:
    print "Invalid Input"
