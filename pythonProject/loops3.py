
participants = ["avi","aadi","paras","shubhi","dipali","tanu"]

position = 1

for name in participants:
    if name == "shubhi":
        print("about to break")
        break
    print("about to increment")
    position = position + 1

print(position)


participants = ["avi","aadi","paras","shubhi","dipali","tanu"]

position = 1
for currentinbox in range(len(participants)):
    if participants [currentinbox] == "paras":
        print("have breaked")
        break
    print("not breaked")

print(currentinbox+1)


participants = ["avi","aadi","paras","shubhi","dipali","tanu"]

position = 1
for number in range(10):
    if number%3 == 0:
        print(number)
        print("divisible by 3")
        continue
    print(number)
    print("not divisible by 3")

participants = ["avi","aadi","paras","shubhi","dipali","tanu"]

position = 1
for number in range(50):
    if number%3 == 0:
        print(number)
        print("divisible by 3")
        continue
    print(number)
    print("not divisible by 3")
