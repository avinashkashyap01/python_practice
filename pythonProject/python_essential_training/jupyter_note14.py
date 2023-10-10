
# Lists

# List Slicing

mylist = [1,2,3,4,5]
print(mylist[3:])

a = mylist[0:6:2]
print(a)

b = mylist[0:6:3]
print(b)

c = mylist[::2]
print(c)

for i in range(100):
    print(i)

mylist = list(range(100))
print(mylist)
print(mylist[::2])
print(mylist[::5])
print(mylist[::10])
print(mylist[::-10])
print(mylist[::-5])


# Modifying Lists

mylist = [1,2,3,4]
mylist.append(5)
print(mylist)

while len(mylist):
    print(mylist.pop())

mylist.insert(3,'a new value')
print(mylist)
print(mylist.pop())

a = [1,2,3,4,5]
b = a
a.append(6)
print(b)

a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print(a)
print(b)
