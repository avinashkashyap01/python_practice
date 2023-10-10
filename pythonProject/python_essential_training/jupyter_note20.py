# If Statment with Fizz Buzz

for n in range(1,101):
    if n % 15 == 0:
        print('FizzBuzz')
    else:
        if n % 3 == 0:
            print('Fizz')
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print(n)


# Elif Statment
for n in range(1,101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
            print('Fizz')
    elif n % 5 == 0:
         print('Buzz')
    else:
        print(n)


# Single Line if Statment
n = 5
print('Fizz' if n % 3 == 0 else n)

fizzbuzz = 'Fizz' if n % 3 == 0 else n
print('Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n)

print('FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n)

print(['FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n for n in range(1,101)])

