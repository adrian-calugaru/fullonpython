import os

print("Hey there! Please enter the name of the file you want to access")
answer= input("Name of the text file:")


if os.path.isfile(answer):
	print("File found, what would you like to do? input the following letters r=read d=delete a=append")
	answer2 = input("Input the letter:")
	answer2 = answer2.lower()
	if answer2 == "r":
		temp = open(answer,"r")
		print(temp.read())
	if answer2 == "d":
		temp=answer
		os.remove(answer)
		temp2=open(temp,"w")
		temp2.close()
	if answer2 == "a":
		temp =open(answer,"a")
		temp2 = input("Enter the text you want to append:")
		temp.write(temp2)
		temp.close
		print("Done!")


else:
	print("File does not exist. Do you want to create one?")
	answer = input("Y/N:")
	if answer == "Y":
		temp = input("Eneter the name of the file:")
		temp2 = open(temp,"w")
		temp2.close()
		print("Done, file created with the name",temp)






