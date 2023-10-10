rows = 6

for i in range(rows, 1, -1):
    # print(f"i:{i} in outer loop")
    # print(f"rows-i={rows-i}")
    for space in range(0, rows-i):
        # print(f"space in inner value : {space} ")
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

