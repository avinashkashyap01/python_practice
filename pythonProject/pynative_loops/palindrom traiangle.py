
n = 5
for i in range(1,5):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i,i+i):
        print(k,end=" ")
    for l in range(1,i):
        print(l,end=" ")
    print()
