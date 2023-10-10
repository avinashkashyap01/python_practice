

# row = 5
# column = 5
# for i in range(0,row+1):
#     for j in range(column-i,0,-1):
#         print(j,end=' ')
#     print("\n",end='')

i = 5
while i >= 1:
    j = i
    while j >= 1:
         print(j,end=' ')
         j -= 1
    i -= 1
    print("\n", end='')
