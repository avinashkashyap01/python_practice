
# List Comprihensions

mylist = [1,2,3,4,5]
[2*iteam for iteam in mylist]
print(mylist)

mylist = list(range(100))
filteredlist = [iteam for iteam in mylist if iteam % 10 == 0]
print(filteredlist)

filteredlist = [iteam for iteam in mylist if iteam % 10 < 3]
print(filteredlist)

# List Comprihensions with Functions

mystring = 'My Name is Avinash Kashyap. I live in Bilaspur'
print(mystring.split('.'))
print(mystring.split())

def cleanword(word):
    return word.replace('.', '').lower()
print([cleanword(word) for word in mystring.split()])
print([cleanword(word) for word in mystring.split() if len(cleanword(word)) < 3])


# Nested List Comprihensions
print([[cleanword(word) for word in sentence.split()] for sentence in mystring.split('.')])

