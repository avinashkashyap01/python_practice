
# Files
# Reading Files

# f = open('10_01_file.txt','r')
# print(f)
# print(f.readline())
#
#
# f = open('10_01_file.txt','r')
# print(f.readlines())
# for line in f.readlines():



# Writing Files

f = open('10_01_outout.txt','w')
print(f)

f.write('Line1\n')
f.write('Line2\n')

f.close()


# Appending File
f = open('10_01_outout.txt','a')
f.write('Line3\n')
f.write('Line4\n')


with open('10_01_outout.txt','a') as f:
     f.write('some stuff\n')
     f.write('some other stuff\n')
print(f)
