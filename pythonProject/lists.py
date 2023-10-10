
#testlist = ["element1","element2","element3"]
#testlist = [0,1,2]

scores = [23,65,76.50,27,43,67,89,76,23]
print(scores[1])

scores = [23,65,76.50,27,43,67,89,76,23]
print(scores[-1])                 # - will be started from back side

scores = [23,65,76.50,27,43,67,89,76,23]
print(scores[1:4])                # in this first one not include after that three digit can be print

scores = [23,65,76.50,27,43,67,89,76,23]
print(scores[0:4])                #in this all four digit print from the first

scores = [23,65,76.50,27,43,67,89,76,23]
print(scores)

scores[1] = 75
print(scores)

scores[0] = "Hello"
print(scores)

scores[2:3] = []
print(scores)

scores[1:3] = []
print(scores)

scores[2] = []
print(scores)

scores[2] = ["Hello","World"]
print(scores)
print(scores[2][0])

scores = [23,65,76.50,27,43,67,89,76,23]
print(scores)
scores.append(99)
print(scores)
