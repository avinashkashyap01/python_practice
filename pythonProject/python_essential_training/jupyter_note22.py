
# For

mylist = [1,2,3,4]
for item in mylist:
    print(item)


# Pass

animallookup = {
    'a' : ['aardvark','antelops'],
    'b' : ['bear'],
    'c' : ['cat'],
    'd' : ['dog'],
}

for latter,animals in animallookup.items():
    pass


# Continue

for latter,animals in animallookup.items():
    if len(animals) > 1:
        continue
    print(f'only one animal! {animals[0]}')


# Break

for latter,animals in animallookup.items():
    if len(animals) > 1:
       print(f'found{len(animals)} animals: {animals}')
    break


# For/Else

for number in range(2,100):
    for facter in range(2,int(number ** 0.5) + 1):
        if number % facter == 0:
            break
    else:
        print(f'{number} is prime!')


for number in range(2,100):
    found_factors = False
    for facter in range(2,int(number ** 0.5) + 1):
        if number % facter == 0:
            found_factors = True
    if not found_factors :
        print(f'{number} is prime!')

