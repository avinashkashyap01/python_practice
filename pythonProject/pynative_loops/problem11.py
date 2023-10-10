
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")
for i in range(start,end+1):
    if i > 1:
        for j in range(2,i):
            if ( i % 2) == 0:
                break
        else:
            print(i)
