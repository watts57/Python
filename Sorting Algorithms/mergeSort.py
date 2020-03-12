import time;


def getInputs(sourceText, targetArray):

    # first let's load all the input files up
    ########100########
    for line in open(sourceText, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                targetArray.append(int(i))  # add the integer to list






def mergeSort(inputList):



    if len(inputList) > 1:
        middle = len(inputList) // 2

        L = inputList[:middle] # set up first half sub array
        R = inputList[middle:] # et up second half sub array

        mergeSort(L) # call merge sort on first half
        mergeSort(R) # call merge sort on second half

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

        while (i < leftLength) and (j < rightLength): # while both i and j are within range of 1st and 2nd half arrays
            if L[i] < R[j]: # compare values of current index of 1st and 2nd half arrays
                inputList[k] = L[i] #if L[i] is smaller (if current index of list 1st half is smaller), put that in current index of input list
                i = i+1 # increment i by one

            else: # do the same as above for second half of list
                inputList[k] = R[j]
                j = j+1
            k += 1
        # if one of the sub arrays ha reached last index, default to other array (if one array is finished before other)
        while i < leftLength: # while i is within range of first half list (if j has reached last index)
            inputList[k] = L[i]
            i = i +1
            k = k+1

        while j < rightLength: # while j is within range of second half of list, and i has reached last index
            inputList[k] = R[j]
            j = j+1
            k = k+1









####6 inputs from lab 2 (lab 3/4 questions 1 and 2)

numbers100 = []
numbers1000 = []
numbers5000 = []
numbers50000 = []
numbers100000 = []
numbers500000 = []

fileInput100 = "100.txt"
fileInput1000 = "1000.txt"
fileInput5000 = "5000.txt"
fileInput50000 = "50000.txt"
fileInput100000 = "100000.txt"
fileInput500000 = "500000.txt"


#########number 1 (lab 3)

'''

    startTime = float(time.time_ns())
    endTime = float(time.time_ns())
    timeTaken = endTime - startTime
    print("\n Time to sort numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")

'''

####100 numbers#######
getInputs(fileInput100, numbers100)
inputList = numbers100
startTime = float(time.time_ns())
mergeSort(inputList)
##print("100 numbers (from lab 2): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("\n Time to sort 100 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")


####1,000 numbers#######
getInputs(fileInput1000, numbers1000)
inputList = numbers1000
startTime = float(time.time_ns())
mergeSort(inputList)
##print("1000 numbers (from lab 2): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("\n Time to sort 1,000 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")


####5,000 numbers#######
getInputs(fileInput5000, numbers5000)
inputList = numbers5000
startTime = float(time.time_ns())
mergeSort(inputList)
##print("5,000 numbers (from lab 2): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("\n Time to sort 5,000 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")


####50,000 numbers#######
getInputs(fileInput50000, numbers50000)
inputList = numbers50000
startTime = float(time.time_ns())
mergeSort(inputList)
##print("50,000 numbers (from lab 2): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("\n Time to sort 50,000 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")


####100,000 numbers#######
getInputs(fileInput100000, numbers100000)
inputList = numbers100000
startTime = float(time.time_ns())
mergeSort(inputList)
##print("100,000 numbers (from lab 2): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("\n Time to sort 100,000 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")


####500,000 numbers#######
getInputs(fileInput500000, numbers500000)
inputList = numbers500000
startTime = float(time.time_ns())
mergeSort(inputList)
endTime = float(time.time_ns())
timeTaken = endTime - startTime
##print("500,000 numbers (from lab 2): " + str(inputList))
print("\n Time to sort 500,000 numbers with merge sort (in nanoseconds): " + str(+timeTaken) + "\n")
########################


#### 14 inputs from lab 4 (lab 3/4 questions 3 and 4)

#####NOTE TO SELF: These do not have .txt extension at the end of their names like the numbers from lab 2 do...omit .txt from names so
##### that they do not conflict with each other's name (keep names the same as they were provided on canvas)
