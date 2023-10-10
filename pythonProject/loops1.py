
Word = "hello"
latters = []

for w in Word:
    print(w)
    if w == "e":
     print("What a funny later")

    latters.append(w)
     # ["h","e","l","l","o"]
print(latters)


Word = "hello"
latters = []
numbers = [1,2,3,4,5]
for l in numbers:
    print(l)

Word = "hello"
latters = []
numbers = [1,2,3,4,5]
# 1%2 = 1
# 2%2 = 0
# 3%2 = 1
for l in numbers:
       if 1%2 == 1:
          print(l)


#range (start,stopping,steps)
numbers = []
for num in range (100):
    numbers.append(num)
    print(num)
print(numbers)

numbers = []
for num in range (1,15,2):
    numbers.append(num)
    print(num)
print(numbers)

numbers = []
for num in range (-1,-100,-4):
    numbers.append(num)
    print(num)
print(numbers)

numbers = []
for num in range (-1,100,3):
    numbers.append(num)
    print(num)
print(numbers)

