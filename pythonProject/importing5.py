
from random import randint

randval = randint(0,100)

while(True):
     guess = int(input("please enter your guess :"))
     if guess == randval:
         break
     elif guess < randval:
         print("your guess was too low")
     else:
         print("to high")

print("you guessed correctly with:",guess)
