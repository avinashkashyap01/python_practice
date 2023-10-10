
def drawfield(field):
    for row in range(5):  # 0,1,2,3,4
        if row%2 == 0:
            practicalrow = int(row/2)
            for column in range(5):
                if column%2 == 0:
                    practicalcolumn = int(column/2)
                    if column != 4:
                        print(field[practicalcolumn][practicalrow],end="")
                    else:
                        print(field[practicalcolumn][practicalrow])
                else:
                    print("|",end="")
        else:
             print("-----")
player = 1
currentfield = [[" "," "," "],[" "," "," "],[" "," "," "]]
drawfield(currentfield)
while(True): #True == True
    print("player turn :",player)
    moverow = int(input("please enter the row \n"))
    movecolumn = int(input("please enter the column \n"))
    if player == 1:
        if currentfield[movecolumn][moverow] == " ":
           currentfield[movecolumn][moverow] = 'x'
           player = 2
    else:
        if currentfield[movecolumn][moverow] == " ":
           currentfield[movecolumn][moverow] = 'o'
           player = 1
    drawfield(currentfield)
