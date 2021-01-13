myUniqueList = []
myLeftovers = []
def check_and_add (item):
	if item in myUniqueList:
		myLeftovers.append(item)
		return False
	else:
		myUniqueList.append(item)
		return True
	

check_and_add(1)
print ("My Unique list contains:",myUniqueList)
print ("My Leftover list contains:",myLeftovers)
check_and_add(4)
print ("My Unique list contains:",myUniqueList)
print ("My Leftover list contains:",myLeftovers)
check_and_add(7)
print ("My Unique list contains:",myUniqueList)
print ("My Leftover list contains:",myLeftovers)
check_and_add(1)
print ("My Unique list contains:",myUniqueList)
print ("My Leftover list contains:",myLeftovers)
check_and_add("cat")
print ("My Unique list contains:",myUniqueList)
print ("My Leftover list contains:",myLeftovers)
check_and_add("mouse")
print ("My Unique list contains:",myUniqueList)
print ("My Leftover list contains:",myLeftovers)
check_and_add("cat")
print ("My Unique list contains:",myUniqueList)
print ("My Leftover list contains:",myLeftovers)
