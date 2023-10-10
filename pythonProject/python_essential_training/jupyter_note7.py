
# Factorial
num = int(input("enter the number"))
def factorial(num):
    if type(num) is not int :
        return None
    if num < 0:
        return None
    if num == 0 :
        return 1

    i = 0
    f = 1
    while i < num :
        i = i + 1
        f = f * i
    return f
a = factorial(num)
print(a)



# num = int(input("enter the number"))
# def factorial(num):
#     if type(num) is not int :
#         return None
#     if num < 0:
#         return None
#     if num == 0 :
#         return 1
#     return num * factorial(num-1)
#
# n = factorial(num)
# print(n)
