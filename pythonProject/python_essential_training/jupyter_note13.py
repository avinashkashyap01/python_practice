
# Converting hex to decimal

hexnumbers = {
    '0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,
    'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15
}
def hextodec(hexnum):
    for char in hexnum:
        if char not in hexnumbers:
            return None
    if len(hexnum) == 3:
        return hexnumbers[hexnum[0]] * 256 + hexnumbers[hexnum[1]] * 16 + hexnumbers[hexnum[2]]
    if len(hexnum) == 2:
        return hexnumbers[hexnum[0]] * 16 + hexnumbers[hexnum[1]]
    if len(hexnum) == 1:
        return hexnumbers[hexnum[0]]


print(hextodec('A'))
print(hextodec('0'))
print(hextodec('1B'))
print(hextodec('3C0'))
print(hextodec('A6G'))
print(hextodec('ZZTOP'))


# Second Solution

def hextodec(hexnum):
    for char in hexnum:
        if char not in hexnumbers:
            return None
    exponent = 0
    decimalvalue = 0
    for char in hexnum[::-1]:
        decimalvalue = decimalvalue + hexnumbers[char] * (16**exponent)
        exponent = exponent + 1
    return decimalvalue

print(hextodec('3C0'))
print(hextodec('3C0000'))
