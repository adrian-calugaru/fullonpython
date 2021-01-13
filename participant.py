# ParticipantNumber = 2
# participantData = []
# registeredParticipants = 0
# outputFile = open("participantData.txt","w")

# while (registeredParticipants < ParticipantNumber):
# 	tempPartData = []
# 	name = input("Please enter your name: ")
# 	tempPartData.append(name)
# 	country = input("Please enter your country of origin: ")
# 	tempPartData.append(country)
# 	age = int(input("Please enter your age:"))
# 	tempPartData.append(age)
# 	print(tempPartData)
# 	participantData.append(tempPartData)
# 	print(participantData)

# 	registeredParticipants += 1

# for participant in participantData:
# 	for data in participant:
# 		outputFile.write(str(data))
# 		outputFile.write(" ")
# 	outputFile.write("\n")	



# outputFile.close()

inputFile = open("participantData.txt","r")

inputList = []

for line in inputFile:
	tempParticipant = line.strip().split()
	print(tempParticipant)
	inputList.append(tempParticipant)
	print(inputList)

Age = {}
for part in inputList:
	tempAge = int(part[-1])
	if tempAge in Age:
		Age[tempAge] += 1
	else:
		Age[tempAge] = 1

print(Age)

Oldest = 0
Youngest = 100
mostOccuringAge = 0
counter = 0

for tempAge in Age:
	if tempAge > Oldest:
		Oldest = tempAge
	if tempAge < Youngest:
		Youngest = tempAge
	if Age[tempAge]>= counter:
		counter = Age[tempAge]
		mostOccuringAge = tempAge
print("OLdest is: ",Oldest)
print("Youngest is: ",Youngest)
print("Most Occuring age is: ",mostOccuringAge,"with",counter)

inputFile.close()

list = [1,2]
for i in list:
    print (i)

age = input("Enter your age: ")
age += "6"
print(age)