x = []
N = input()
y = raw_input()
x = y.split(" ")
a = map(int, x)
if(len(a) == N):
    a.sort()
    print a[N-1]
else:
    print "Invalid Input"
