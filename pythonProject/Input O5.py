

# participantnumber = 2
# participantdata = []
# ragisterdparticipants = 0
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

participantnumber = 2
participantdata = []
ragisterdparticipants = 0
outputfile = open("participantdata.txt","w")

while(ragisterdparticipants < participantnumber):
    temppartdata = []
    name = input("please enter your name :")
    temppartdata.append(name)
    country = input("please enter your country of oragin :")
    temppartdata.append(country)
    age = int(input("please enter your age :"))
    temppartdata.append(age)
    print(temppartdata)
    participantdata.append(temppartdata)
    print(participantdata)
    ragisterdparticipants += 1

for participant in participantdata:
    for data in participant:
        outputfile.write(str(data))
        outputfile.write(" ")
    outputfile.write("\n")

outputfile.close()
