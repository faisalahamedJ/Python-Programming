a = input()
b = input()
if(isinstance((a and b),int)):
    for num in range (a,b):
        temp = num
        i = temp 
        power = 0
        mult = 0
        while(i > 0):
            power += 1  
            i //= 10
        while(num > 0):
            rem = num % 10
            mult += pow(rem,power)
            num //= 10
        if(temp == mult):
            print mult,
else:
    print "Invalid Input"
