
# from random import random
# randval = random()
# # print(randval)
#
# upper = 1.0
# lower = 0.0
# guess = 0.5
# while(True):
#     if guess == randval:
#         break
#     elif guess < randval:
#         lower = guess
#     else:
#         upper = guess
#     guess = (upper + lower)/2
# print(guess)



from random import random
from time import time
randval = random()
print(randval)

upper = 1.0
lower = 0.0
guess = 0.5
starttime = time()
while(True):
    guess = (upper + lower)/2
    if guess == randval:
        break
    elif guess < randval:
        lower = guess
    else:
        upper = guess

endtime = time()
print(guess)
print("it took us :",endtime-starttime," seconds")
