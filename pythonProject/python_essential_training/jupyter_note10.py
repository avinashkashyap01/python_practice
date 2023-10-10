
# Booleans

# Casting Booleans

a = bool(1)
print(a)

b = bool(0)
print(b)

c = bool(-1)
print(c)

d = bool(1j)
print(d)

e = bool(0.0)
print(e)

f = bool(0j)
print(f)

g = bool('True')
print(g)

h = bool('False')
print(h)

i = bool('')
print(i)

j = bool(' ')
print(j)

k = bool([1])
print(k)

l = bool({})
print(l)

m = bool(None)
print(m)

mylist = [1,2]
if bool(mylist) :
    print('my list has some values in it!')


x = 5
y = 5
if a-b:
    print('x and y are not equal!')
print(x == y)


# Boolean Logic

weatherisnice = False
haveumbrella = True
if not haveumbrella or weatherisnice:
    print('stay inside')
else:
    print('go for a walk')


weatherisnice = True
haveumbrella = False
if not (haveumbrella) or weatherisnice:
    print('stay inside')
else:
    print('go for a walk')


weatherisnice = True
haveumbrella = False
if (not haveumbrella) and (not weatherisnice):
    print('stay inside')
else:
    print('go for a walk')


weatherisnice = True
haveumbrella = False
if not (haveumbrella or weatherisnice):
    print('stay inside')
else:
    print('go for a walk')



weatherisnice = True
haveumbrella = False
if haveumbrella or weatherisnice:
    print('go for a walk')
else:
    print('stay inside')
