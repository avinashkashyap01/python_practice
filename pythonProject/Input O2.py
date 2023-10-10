
# file = open("filename","r")
# file.close()


# vacationspots = ["india","nepal","bhutan","iceland","usa"]
#
# vacationfile = open("vacationplaces","w")
#
# for spots in vacationspots:
#     vacationfile.write(spots +"\n")
#
# vacationfile.close()
#
# vacationfile = open("vacationplaces","r")
#
# # thewholefile = vacationfile.read()
# # print(thewholefile)
# for line in vacationfile:
#       print (line)
# vacationfile.close()




# vacationspots = ["india","nepal","bhutan","iceland","usa"]
#
# vacationfile = open("vacationplaces","w")
#
# for spots in vacationspots:
#     vacationfile.write(spots +"\n")
#
# vacationfile.close()
#
# vacationfile = open("vacationplaces","r")
#
# firstline = vacationfile.readline()
# print(firstline)
# secondline = vacationfile.readline()
# print(secondline)
# for line in vacationfile:
#       print (line,end="")
# # thewholefile = vacationfile.read()
# # print(thewholefile)
# vacationfile.close()
#
# finalspot = "thailand"
# vacationfile = open("vacationplaces","w")
# vacationfile.write(finalspot)
# vacationfile.close()
#
# vacationfile = open("vacationplaces","r")
# for line in vacationfile:
#       print (line,end="")




vacationspots = ["india","nepal","bhutan","iceland","usa"]

vacationfile = open("vacationplaces","w")

for spots in vacationspots:
    vacationfile.write(spots +"\n")

vacationfile.close()

vacationfile = open("vacationplaces","r")

firstline = vacationfile.readline()
print(firstline)
secondline = vacationfile.readline()
print(secondline)
for line in vacationfile:
      print (line,end="")
# thewholefile = vacationfile.read()
# print(thewholefile)
vacationfile.close()

finalspot = "thailand"
vacationfile = open("vacationplaces","a")
vacationfile.write(finalspot)
vacationfile.close()

vacationfile = open("vacationplaces","r")
for line in vacationfile:
      print (line,end="")

for i in range(5):
    with open("vacationplaces","r")as vacationfile:
         for line in vacationfile:   # range 5 then 5 times print vacationspots
              print (line)
vacationfile.read()
