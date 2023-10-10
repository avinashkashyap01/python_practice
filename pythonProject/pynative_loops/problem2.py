
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print("\n", end="")

print("============below is while loop==========")
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    i = i + 1
    print("\n", end="")

