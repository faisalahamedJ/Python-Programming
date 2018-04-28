x = []
N = input()
a = raw_input()
x = a.split(" ")
x = map(int, x)
if(len(x) == N):
    x.sort()
    for i in x:
        print i,
else :
    print "Invalid Input"
