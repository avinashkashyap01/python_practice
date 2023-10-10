
# name = input("please enter your name :")
# print(name)
#
# age = input("please enter your age :")
# print(age)

# age = input("please enter your age :")
# print(age+"1")

# scores = []
# for i in range(5):
#     currentscores = int(input("please enter your scores :"))
#     scores.append(currentscores)
# print(scores)

# scores = []
# for i in range(5):
#     currentscores = int(input("please enter your scores " +str(i+1)+" :"))
#     scores.append(currentscores)
# print(scores)

scores = []
for i in range(5):
    currentscore = float(int(input("please enter your scores " +str(i+1)+" :")))
       # for decimal numbers
    scores.append(currentscore)
    print("the scores you entered was :\n"+str(currentscore))
print(scores)

