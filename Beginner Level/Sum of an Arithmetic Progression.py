x = []
y = raw_input()
x = y.split(" ")
N = int(x[0])
A = int(x[1])
D = int(x[2])
i = 0
add = 0
while i < N :
    add = add + A
    A = A + D
    i += 1
print add
