n, k = 5, 5
for i in range(0, n+1):
    for j in range(0, k):
        print(end=" ")
    k -= 1

    for l in range(i+1):
        print("* ", end="")

    print("\n")


n = 5
for i in range(n):
     for j in range(i,n):
        print("",end='')
     for j in range(i):
        print("*",end='')
     for j in range(i+1):
        print("",end='')
print()
