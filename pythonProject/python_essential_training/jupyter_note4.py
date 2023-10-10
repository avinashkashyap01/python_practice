
# Control Flow

# If/Else Statments

a = False
if a:
    print('it is true')
    print('also print this')
else:
    print('it is false')
print('always print this')


# a = True
# if a:
#     print('it is true')
#     print('also print this')
# else:
#     print('it is false')
# print('always print this')


a = True
b = True
c = True
if a:
    print('it is true')
    print('also print this')
    if b:
        print('both are true')
        if c:
            print('all three are true')
else:
    print('it is false')
print('always print this')


# For Loops

a =[1,2,3,4,5]
for number in a:
    print(number)

b = 4 in a
print(b)


# While Loop

a = 0
while a < 5:
    print(a)
    a = a + 1
