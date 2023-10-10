
vacationspots = ["india","nepal","iran","newyork","iceland"]

vacationfile = open("vacationplaces","w")

for spots in vacationspots:
    vacationfile.write(spots)

vacationfile.close()

vacationfile = open("vacationplaces","r")
thewholefile = vacationfile.read()
print(thewholefile )
