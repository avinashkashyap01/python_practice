
# Dictionary Comprehensions

animallist = [('a','aardvark'),('b','bear'),('c','cat'),('d','dog')]
animals = {item[0]: item[1] for item in animallist}
print(animals)

animals = {key: value for key,value in animallist}
print(animals)
print(animals.items())
a = list(animals.items())
print(a)

print([{'latter':key, 'name':value} for key,value in animals.items()])
