num = input("Enter the number\n")
count = 0
if(isinstance(num,int)):
    while(num>0):
        num = num // 10
        count += 1
    print(count)
else:
    print("Invalid Input")
