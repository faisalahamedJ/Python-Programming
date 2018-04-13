num = input("Enter the Number")
fact = 1
if(isinstance(num,int)):
      for i in range (1,num+1):
          fact *= i
      print fact
else:
    print "Invalid Input"
