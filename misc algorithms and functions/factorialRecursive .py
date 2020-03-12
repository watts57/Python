def factorialFirstTwelve(currentNumber):
	##print(str(currentNumber)+"!")
	facList=[]## list used to store numbers to multiply for factorial
	facProduct = 1 # initialize this variable used to multiply...start with 1
	
	# for loop used to add relevant numbers to list
	for i in range(1,currentNumber+1): # from 1 to 13-1 range to produce 
	#	factorials up to 12
		facList.append(i)# add current i to list
		i = i + 1 # increment i by one
		
	# now use elements of list to multiply to get factorials
	for j in facList: # for loop for multiplication
		facProduct = facProduct * j # 1*1...2*1...3*2....4*3....etc
	
	print("!"+str(currentNumber)+ " = " + str(facProduct)) # print factorial
	##print(facList)
	while currentNumber < 12: # while in first 12 factorial range
		return factorialFirstTwelve(currentNumber + 1) # run back through function recursively
		
			
	
	
			

currentNumber = 1
factorialFirstTwelve(currentNumber)
