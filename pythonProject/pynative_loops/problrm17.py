
a = "2"
b = 0
n = int(input("Enter the Number"))
l = []
for i in range(1,n+1):
    d = a*i
    l.append(d)
    b = b +int(d)

print("+".join(l), f"={b}")
