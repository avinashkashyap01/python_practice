
# Ints and Floats
from decimal import Decimal,getcontext

getcontext().prec=4
print(getcontext())

a = int('100')
print(a)

b = int('100',2)
print(b)

c = int('100',16)
print(c)

d = 1.2 - 1.0
print(d)

e = int('100',5)
print(e)


# Decimal

g = Decimal(1)/Decimal(3)
print(g)

h = Decimal(3.14)
print(h)

i = Decimal('3.14')
print(i)

j = round(1.2-1.0,2)
print(j)

getcontext().prec=2
k = Decimal(1)/Decimal(3)
print(k)

l = Decimal(3.14)
print(l)

getcontext().prec=2
print(getcontext())

