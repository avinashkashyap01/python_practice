
#  / /  0
# ----- 1
#  / /  2
# ----- 3
#  / /  4

# for row in range(5):  # 0,1,2,3,4
#      if row%2 == 0:
#         print(" / / ")
#         #     "12345"
#      else:
#         print("-----")

# for row in range(5):  # 0,1,2,3,4
#      if row%2 == 0:
#          for column in range(1,6):
#              if column%2 == 1:
#                  print(" ",end="")
#              else:
#                   print("|",end="")
#          #print(" / / ")
#          #     "12345"
#      else:
#         print("-----")

for row in range(5):  # 0,1,2,3,4
     if row%2 == 0:  # 0,2,4
         for column in range(1,6):  # 1,2,3,4,5
             if column%2 == 1:
                 if column != 5:
                   print(" ",end="")  # 1,3
                 else:
                   print(" ")  # 5
             else:
                  print("|",end="")  # 2
         #print(" / / ")
         #     "12345"
     else:
        print("-----")
