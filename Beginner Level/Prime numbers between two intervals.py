a = []
b = raw_input()
a = b.split(" ")
for i in range(int(a[0])+1,int(a[1])):
    for x in range(2,i):
        if (i % x) == 0:
            break
    else:
        print i,
