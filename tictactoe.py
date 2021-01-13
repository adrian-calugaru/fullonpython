#01234
# | | 0
#-----1
# | | 2
#-----3
# | | 4


def drawField(filed):
	for row in range(5):
		if row%2==0:
			practicalRow = int(row/2)
			for column in range(5):
				if column%2==0:
					practicalColumn = int(column/2)
					if column !=4:
						print(filed[practicalColumn][practicalRow],end="")
					else:
						print (filed[practicalColumn][practicalRow])
				else:
					print("|",end="")
		else:
			print("-----")



Player = 1
currentFiled = [[" "," "," "],[" "," "," "],[" "," "," "]]
drawField(currentFiled)
while (True):
	print("Player turn: ", Player)
	MoveRow = int(input("Please enter row:\n"))
	MoveColumn = int(input("Please enter column:\n"))
	if Player==1:
		#make move for p1
		if currentFiled[MoveColumn][MoveRow]== " ":
			currentFiled[MoveColumn][MoveRow] = "X"
			Player = 2
	else:
		#make move for p2
		if currentFiled[MoveColumn][MoveRow]== " ":
			currentFiled[MoveColumn][MoveRow] = "O"
			Player = 1
	drawField(currentFiled)