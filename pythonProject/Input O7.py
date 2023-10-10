
# participantnumber = 5
# participantdata = []
# ragisterdparticipants = 0
# outputfile = open("participantdata.txt","w")
#
# while(ragisterdparticipants < participantnumber):
#     temppartdata = []
#     name = input("please enter your name :")
#     temppartdata.append(name)
#     country = input("please enter your country of oragin :")
#     temppartdata.append(country)
#     age = int(input("please enter your age :"))
#     temppartdata.append(age)
#     print(temppartdata)
#     participantdata.append(temppartdata)
#     print(participantdata)
#     ragisterdparticipants += 1
#
# for participant in participantdata:
#     for data in participant:
#         outputfile.write(str(data))
#         outputfile.write(" ")
#     outputfile.write("\n")
#
# outputfile.close()



inputfile = open("participantdata.txt","r")

inputlist = []

for line in inputfile:
     temparticipant = line.strip().split()
    # print(temparticipant)
     inputlist.append(temparticipant)
    # print(inputlist)

age = {}
print(inputlist)
for part in inputlist:
    tempage = int(part[-1])
    if tempage in age :
        age [tempage] += 1
    else:
         age [tempage] = 1

countries = {}
for part in inputlist:
    tempcountry = part[1]
    if tempcountry in country :
        country[tempcountry] += 1
    else:
         country [tempcountry] = 1

print("countries that attendent ",countries)

oldesst = 0
youngest = 1
mostoccuringage = 0
counter = 0

for tempage in age:
    if tempage>oldesst:
        oldesst = tempage
    if tempage<youngest:
        youngest=tempage
    if age [tempage]>=counter
        counter = age[tempage]
        mostoccuringage = tempage

print(oldesst)
print(youngest)
print("mostoccuring age is :",mostoccuringage,"with",counter,"participants")
inputfile.close()
