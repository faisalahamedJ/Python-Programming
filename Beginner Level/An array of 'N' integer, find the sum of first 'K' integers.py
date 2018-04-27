from array import *
N = input()
my_array =[]
for i in range (0,N) :
    x = input()
    my_array.append(x)
K = input()
add = 0
for s in range (0,K):
    add = add + my_array[s]
print(add)
