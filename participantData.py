ParticipantNumber=5
ParticipantData = []
registeredParticipants = 0
outputFile=open("ParticipantData.txt","w")

while(registeredParticipants < ParticipantNumber):
    
    tempParticipantData= []
    name=input("Enter your Name: ")
    tempParticipantData.append(name)
    country=input("Enter your country of origin: ")
    tempParticipantData.append(country)
    age=int(input("Please Enter your Age: "))
    tempParticipantData.append(age)
    print(tempParticipantData)
    ParticipantData.append(tempParticipantData)
    print(ParticipantData)

    registeredParticipants+=1

for participant in ParticipantData:
    for data in participant:
        outputFile.write(str(data))
        outputFile.write(" ")
    outputFile.write("\n")
outputFile.close()
inputFile=open("ParticipantData.txt","r")

inputList=[]

for line in inputFile:
    tempParticipant=line.strip("\n").split()
    print(tempParticipant)
    inputList.append(tempParticipant)
    print(tempParticipant)
    print(inputList)



Age = {}
print(inputList)
for part in inputList:
    tempAge=int(part[-1])
    if tempAge in Age:
        Age[tempAge]+=1 
    else:
        Age[tempAge] =1
print(Age)

Countries = {}
for part in inputList:
    tempCountry=int(part[-1])
    if tempCountry in Countries:
        Countries[tempCountry]+=1 
    else:
        Countries[tempCountry] =1
print("Countries that attended: ",Countries)
Oldest=0
Youngest=0
MostOccuringAge=0
Counter=0

for tempAge in Age:
    if(tempAge>Oldest):
        Oldest=tempAge
    if(tempAge<Youngest):
        Youngest=tempAge
    if(Age[tempAge]>=Counter):
        Counter=Age[tempAge]
        MostOccuringAge=tempAge
print(Oldest)
print(Youngest)
print("Most occuring Age is: ",MostOccuringAge,"with",Counter,"Participants")
inputFile.close()