
#  / /
# -----
#  / /
# -----
#  / /
# def drawfield():
#     for row in range(5):  # 0,1,2,3,4
#         if row%2 == 0:
#             for column in range(5):
#                 if column%2 == 0:
#                     if column != 4:
#                         print(" ",end="")
#                     else:
#                         print(" ")
#                 else:
#                     print("|",end="")
#         else:
#              print("-----")
# drawfield()


def drawfield():
    for row in range(5):  # 0,1,2,3,4
        if row%2 == 0:
            for column in range(5):
                if column%2 == 0:
                    if column != 4:
                        print(" ",end="")
                    else:
                        print(" ")
                else:
                    print("|",end="")
        else:
             print("-----")
player = 1
currentfield = [[" "," "," "],[" "," "," "],[" "," "," "]]
print(currentfield)
while(True): #True == True
    print("player turn :",player)
    moverow = int(input("please enter the row \n"))
    movecolumn = int(input("please enter the column \n"))
    if player == 1:
      currentfield[movecolumn][moverow] = 'x'
      player = 2
    else:
       currentfield[movecolumn][moverow] = 'o'
       player = 1
    print(currentfield)
