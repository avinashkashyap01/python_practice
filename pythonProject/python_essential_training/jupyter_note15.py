
# Sets

myset = {'a','b','c'}
print(myset)

myset = set(('a','b','c'))
myset.add('d')
print(myset)
a = 'a' in myset
print(a)
b = 'z' in myset
print(b)
c = len(myset)
print(c)


while len(myset):
    print(myset.pop())


mylist = ['a','b','b','c','c']
mylist = list(set(mylist))
print(mylist)

myset = {'a','b','c'}
myset.discard('a')
print(myset)



# Tuples

mytuples = ('a','b','c')
print(mytuples)

a = mytuples[0]
print(a)

def returnsmultiplevalues():
    return 1,2,3,
type(returnsmultiplevalues())
mytuples = (1,2,3)
print(type(mytuples))
a,b,c = returnsmultiplevalues()
print(a)
print(b)
print(c)
