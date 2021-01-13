def tictactoe(rows,columns):
	for row in range(rows):
	 	if row%2==0:
	 		for column in range(1,columns +1):
	 			if column%2==1:
	 				if column != columns:
	 					print(" ",end="")
	 				else:
	 					print(" ")
	 			else:
	 				print("|",end="")		
	 		
	 	else:
	 		print(rows*"-")
	return True

print(tictactoe(9,9))