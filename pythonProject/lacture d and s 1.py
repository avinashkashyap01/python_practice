
# blackshoes = {7:0,8:4,9:5,10:3,11:1}
# print(blackshoes)
# while(True): #True == True
#     purchessize = int(input("which shoe size would you buy?"))
#     blackshoes[purchessize]-=1
#     print(blackshoes)


# blackshoes = {7:0,8:4,9:5,10:3,11:1}
# print(blackshoes)
# while(True): #True == True
#     purchessize = int(input("which shoe size would you buy?"))
#     if blackshoes[purchessize] > 0:
#         blackshoes[purchessize]-=1
#     else:
#       print("shoes are no longer in stock")
#     print(blackshoes)


blackshoes = {7:0,8:4,9:5,10:3,11:1}
print(blackshoes)
while(True): #True == True
    purchessize = int(input("which shoe size would you buy?\n"))
    if purchessize < 0:
        break
    if blackshoes[purchessize] > 0:
        blackshoes[purchessize]-=1
    else:
      print("shoes are no longer in stock")
    print(blackshoes)
