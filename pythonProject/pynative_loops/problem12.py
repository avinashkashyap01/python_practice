
num1 = 0
num2 = 1
print("Fibonacci sequence:")
for i in range(15):
    print(num1,end=' ')
    a = num1 + num2
    print(f" = {a}")
    num1 = num2
    num2 = a
    print(f" + {num2}")
