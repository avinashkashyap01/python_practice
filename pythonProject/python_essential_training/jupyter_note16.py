
# Dictionaries

animals = {
    'a' : 'aardvark',
    'b' : 'bear',
    'c' : 'cat'
}
print(animals)
print(animals['a'])
animals['d'] = 'dog'
print(animals)
animals['a'] = 'antelop'
print(animals)

a = animals.keys()
print(a)
b = animals.values()
print(b)
c = list(animals.keys())
print(c)
print(animals.get('a'))
print(len(animals))


animals = {
    'a' : ['aardvark','antelop'],
    'b' : ['bear'],
}
animals['b'].append('bison')
animals['c'] = ['cat']

if 'c' not in animals:
    animals['c'] = []
animals['c'].append('cat')
print(animals)


# The Default Dict
from collections import defaultdict
animals = defaultdict(list)
print(animals)
animals['e'].append('elephant')
print(animals)
animals['e'].append('emu')
print(animals)
animals['f']
print(animals)
