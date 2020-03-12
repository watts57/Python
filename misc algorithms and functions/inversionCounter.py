import time;



#This "automates" loading text files and saves a lot of lines of manual coding
def getInputs(sourceText, targetArray):

    # first let's load all the input files up
    ########100########
    for line in open(sourceText, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                targetArray.append(int(i))  # add the integer to list






#Lab 3/4 number 3....merge sort with inversions counted

def mergeSortWithInversionsCounted(inputList): #inputList is array going into function, is loaded using getInput function above
    if len(inputList) == 1: # if only one element, it's already sorted, and no inversions
        return inputList, 0
    else:
        L = inputList[:len(inputList) // 2] ## different approach to slicing this time...other approach did not work...this is more similar to pseudocode on board in lab
        R = inputList[len(inputList) // 2:] ## ^^ see above... L is 1st half....R is 2nd half....
        L, leftI = mergeSortWithInversionsCounted(L) #assign l,Left I value to function
        R, rightI = mergeSortWithInversionsCounted(R) #^^ see above line, same logic
        output = [] ## output array (will be sorted output)


        i = 0 # iterate this variable through left half
        j = 0 # iterate this variable through right half
        inversions = 0 + leftI + rightI # track number of inversions
    while i < len(L) and j < len(R): # while the variable iterating through both halves is in their ranges
        if L[i] <= R[j]: # if R current index is bigger or equal to L
            output.append(L[i]) # add L[i], which is smaller, to output
            i += 1 #increment i by one
        else: # otherwise
            output.append(R[j]) # append R[j], because it is smaller
            j += 1 # increment j
            inversions += (len(L)-i) # this is an inversion, so add it to the inversions counter

    output += L[i:] #append
    output += R[j:] #append

    totalInversionCount.append(inversions) # I use this to print (print last index, gives total, also can be used to debug more easily and see count at each time it is appended since that will match with index of this array
    return output, inversions # "back into rabbit hole"













# SETTING UP GETINPUT FUNCTION THAT FEEDS ARRAYS INTO MERGESORT FUNCTION
####14 inputs from lab 4 (lab 3/4 questions 3 and 4)
numbers10 = []
numbers50 = []
numbers100 = []
numbers150 = []
numbers200 = []
numbers250 = []
numbers300 = []
numbers350 = []
numbers400 = []
numbers450 = []
numbers500 =[]
numbers1000 = []
numbers5000 = []
numbers10000 = []


fileInput10 = "10"
fileInput50 = "50"
fileInput100 = "100"
fileInput150 = "150"
fileInput200 = "200"
fileInput250 = "250"
fileInput300 = "300"
fileInput350 = "350"
fileInput400 = "400"
fileInput450 = "450"
fileInput500 = "500"
fileInput1000 = "1000"
fileInput5000 = "5000"
fileInput10000 = "10000"









#### 14 inputs from lab 4 (lab 3/4 questions 3 and 4)

print("####10 Numbers####")
getInputs(fileInput10, numbers10)
inputList = numbers10
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("10 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime

print("--------")
print("\n Time to sort 10 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 10 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####50 numbers#######")

getInputs(fileInput50, numbers50)
inputList =  numbers50
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("50 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 50 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 50 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####100 numbers#######")

getInputs(fileInput100, numbers100)
inputList = numbers100
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("00 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 100 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 100 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####150 numbers#######")

getInputs(fileInput150, numbers150)
inputList = numbers150
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("150 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 150 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 150 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####200 numbers#######")

getInputs(fileInput200, numbers200)
inputList = numbers200
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("200 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 200 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 200 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####250 numbers#######")

getInputs(fileInput250, numbers250)
inputList = numbers250
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("250 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 250 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 250 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####300 numbers#######")

getInputs(fileInput300, numbers300)
inputList = numbers300
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("300 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 300 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 300 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####350 numbers#######")

getInputs(fileInput350, numbers350)
inputList = numbers350
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("350 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 350 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 350 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####400 numbers#######")

getInputs(fileInput400, numbers400)
inputList = numbers400
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("400 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 400 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 400 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####450 numbers#######")

getInputs(fileInput450, numbers450)
inputList = numbers450
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("450 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 450 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 450 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####500 numbers#######")

getInputs(fileInput500, numbers500)
inputList = numbers500
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("500 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 500 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 500 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####1000 numbers#######")

getInputs(fileInput1000, numbers1000)
inputList = numbers1000
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("1000 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 1000 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 1,000 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####5000 numbers#######")

getInputs(fileInput5000, numbers5000)
inputList = numbers5000
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("5000 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 5,000 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 5,000 Number Array :  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########

print("####10000 numbers#######")

getInputs(fileInput10000, numbers10000)
inputList = numbers10000
startTime = float(time.time_ns())
totalInversionCount = []
mergeSortWithInversionsCounted(inputList)
##print("10000 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 10,000 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
print("Inversions Counted in 10,000 Number Array:  = " +str(totalInversionCount[(len(totalInversionCount) - 1)]))
print("--------")
#########



#####NOTE TO SELF: These do not have .txt extension at the end of their names like the numbers from lab 2 do...omit .txt from names so
##### that they do not conflict with each other's name (keep names the same as they were provided on canvas)


# THE FOLLOWING CODE IS BROKEN AND I ONLY INCLUDED TO SALVAGE THE USEFUL PARTS/ TRY TO FIGURE OUT WHERE I WENT WRONG
'''

def mergeSort(inputList,inversions):


NOTE TO SELF:

OLD CODE: included for referencing while I try to rebuild it in a way that works...approach from number 1 did not work for some reason, unsure why, but it failed to correclty count inversions...
I think it missed split inversions somehow...not sure... kept getting 16 instead of 23 for 10 number input file in tests

    FIX CODE TO CORRECTLY COUNT INVERSIONS... GETTING 16, SHOULD BE 23 for 10 size
    ...just appending a 1 to array and counting length each time inversion occurs

    WHY DOES THIS NOT WORK!!?!! ( below)

    if len(inputList) > 1:
        middle = len(inputList) // 2

        L = inputList[:middle] # set up first half sub array
        R = inputList[middle:] # et up second half sub array

        mergeSort(L,inversions) # call merge sort on first half
        mergeSort(R,inversions) # call merge sort on second half

        leftLength = len(L) #length of first half
        rightLength = len(R) # length of second half
        i = 0 #iterates through L
        j = 0 #iterates through R
        k = 0 # iterates through A



        if i >= leftLength: # if i has reached value greater or equal to length of first half
            inputList[k] = R[j] #default to getting values from second half
            j = j+1 #increment j by one
        if j >= rightLength: # do the same as above for second half, same logic in reverse
            inputList[k] = L[i]
            i = i+1
            #because i would be going to right of last index of j, this would be an inversion since A[i] > A[j]
            #increment inversion count by one
            inversions = inversions + 1


        while (i < leftLength) and (j < rightLength): # while both i and j are within range of 1st and 2nd half arrays
            if L[i] < R[j]: # compare values of current index of 1st and 2nd half arrays
                inputList[k] = L[i] #if L[i] is smaller (if current index of list 1st half is smaller), put that in current index of input list
                i = i+1 # increment i by one
                #not an inversion

            else: # R[j] is smaller...do the same as above for second half of list
                inputList[k] = R[j]
                j = j+1
                #inversion has occurred
                #increment inversion count by one
                inversions += (len(L) - i)
            k += 1
        # if one of the sub arrays has reached last index, default to other array (if one array is finished before other)
        while i < leftLength: # while i is within range of first half list (if j has reached last index)
            inputList[k] = L[i]
            i = i +1
            #this is an inversion since A[i] > A[j], increment inversion count by one
            inversions = inversions + 1
            k = k+1

        while j < rightLength: # while j is within range of second half of list, and i has reached last index
            inputList[k] = R[j]
            j = j+1
            k = k+1
            #not an inversion


'''