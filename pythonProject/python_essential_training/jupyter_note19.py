

def encodestring(stringval):
    encodedlist = []
    prevchar = stringval[0]
    count = 0
    for char in stringval:
        if prevchar != char:
            encodedlist.append((prevchar,count))
            count = 0
        prevchar = char
        count = count + 1

    encodedlist.append((prevchar,count))
    return encodedlist

def decodestring(encodedlist):
    decodestr = ''
    for item in encodedlist:
        decodestr = decodestr + item[0] * item[1]
        return decodestr
print(encodestring('AAAAABBBBCCC'))
print(decodestring([('A',5),('B',4),('C',3)]))

art = '''




















'''
encodestring = encodestring(art)
print(decodestring(encodestring()))
