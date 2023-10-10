
# Strings

# Slicing

name = 'My name is Avinash Kashyap'
print(name[0])
print(name[1])
print(name[0:7])
print(name[11:])
print(name[0:])

mylist = [1,2,3,4,5]
print(mylist[2:4])
print(len(mylist))
print(len(name))


# Formating

import math
a = 'my number is : ' +str(5)
print(a)

b = f'my number is : {5}'
print(b)

c = f'my number is : {5} and twice that is {2*5}'
print(c)

d = f'pi is : {math.pi:.2f}'
print(d)

e = 'pi is : {}'.format(math.pi)
print(e)


# Multiline Strings

mystring = '''
here is long block of text
i can add newlines!
the text doesn't stop untill it sees \'\'\'
'''
print(mystring)
