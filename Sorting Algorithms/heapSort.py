import time

def getInputs(sourceText, targetArray):
    # first let's load all the input files up
    ########100########
    for line in open(sourceText, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                targetArray.append(int(i))  # add the integer to list

def maxHeapify(inputList, length, i):
    largestItem = i
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2

    #check if root has children and fix if they are larger than parent
    if leftChild < length and inputList[i] < inputList[leftChild]:
        largestItem = leftChild

    if rightChild < length and inputList[largestItem] < inputList[rightChild]:
        largestItem = rightChild

    #Swap items if appropriate to maintain max heap property
    if largestItem != i:
        inputList[i],inputList[largestItem] = inputList[largestItem], inputList[i] #switches largestItem with i
        maxHeapify(inputList, length, largestItem) #call maxHeapify on new root


def buildMaxHeap(inputList):
    length = len(inputList)
    for i in range(length, -1, -1):
        maxHeapify(inputList,length, i)

def heapSort(inputList):
    length = len(inputList)
    #need a max heap to start on, sp call build max heap function
    buildMaxHeap(inputList)
    #now begin sorting
    for i in range(length-1, 0, -1): #remove largest  item each loop...decrement down to 0
        inputList[i], inputList[0] = inputList[0], inputList[i] #first index and i switch places
        maxHeapify(inputList, i, 0)
    #this should now be heapSorted

####################BELOW: CALL FUNCTIONS AND TEST##########

num100= []
num1000= []
num5000= []
num50000 = []
num100000 = []
num500000 = []

getInputs("100.txt",num100)
getInputs("1000.txt",num1000)
getInputs("5000.txt",num5000)
getInputs("50000.txt",num50000)
getInputs("100000.txt",num100000)
getInputs("500000.txt",num500000)

print("Will Watts....CS303...Lab7....heapSort")


###############################################
print("Performing heapSort(inputList on 100 numbers...")
print("heapSort(100.txt)")
inputList = num100
#print("\nUnsorted inputList:            " + str(inputList))
startTime = time.time_ns()
heapSort(inputList)
length = len(inputList)
endTime = time.time_ns()
timeTaken = endTime - startTime
print("Time taken to complete heapSort(num100):")
print(str(timeTaken)+" nanoseconds")
#print("\nResult of heapSort(inputList): "+ str(inputList))
print("\n##########################################\n")

###############################################
print("Performing heapSort(inputList on 1000 numbers...")
print("heapSort(1000.txt)")
inputList = num1000
#print("\nUnsorted inputList: "+str(inputList))
startTime = time.time_ns()
heapSort(inputList)
length = len(inputList)
endTime = time.time_ns()
timeTaken = endTime - startTime
print("Time taken to complete heapSort(num1000):")
print(str(timeTaken)+" nanoseconds")
#print("\nResult of heapSort(inputList): "+ str(inputList))
print("\n##########################################\n")

###############################################
print("Performing heapSort(inputList on 5000 numbers...")
print("heapSort(5000.txt)")
inputList = num5000
#print("\nUnsorted inputList: "+str(inputList))
startTime = time.time_ns()
heapSort(inputList)
length = len(inputList)
endTime = time.time_ns()
timeTaken = endTime - startTime
print("Time taken to complete heapSort(num5000):")
print(str(timeTaken)+" nanoseconds")
#print("\nResult of heapSort(inputList): "+ str(inputList))
print("\n##########################################\n")

###############################################
print("Performing heapSort(inputList on 50000 numbers...")
print("heapSort(50000.txt)")
inputList = num50000
#print("\nUnsorted inputList: "+str(inputList))
startTime = time.time_ns()
heapSort(inputList)
length = len(inputList)
endTime = time.time_ns()
timeTaken = endTime - startTime
print("Time taken to complete heapSort(num50000):")
print(str(timeTaken)+" nanoseconds")
#print("\nResult of heapSort(inputList): "+ str(inputList))
print("\n##########################################\n")

###############################################
print("Performing heapSort(inputList on 100000 numbers...")
print("heapSort(100000.txt)")
inputList = num100000
#print("\nUnsorted inputList: "+str(inputList))
startTime = time.time_ns()
heapSort(inputList)
length = len(inputList)
endTime = time.time_ns()
timeTaken = endTime - startTime
print("Time taken to complete heapSort(num100000):")
print(str(timeTaken)+" nanoseconds")
#print("\nResult of heapSort(inputList): "+ str(inputList))
print("\n##########################################\n")

###############################################
print("Performing heapSort(inputList on 500000 numbers...")
print("heapSort(500000.txt)")
inputList = num500000
#print("\nUnsorted inputList: "+str(inputList))
startTime = time.time_ns()
heapSort(inputList)
length = len(inputList)
endTime = time.time_ns()
timeTaken = endTime - startTime
print("Time taken to complete heapSort(num500000):")
print(str(timeTaken)+" nanoseconds")
#print("\nResult of heapSort(inputList): "+ str(inputList))
print("\n##########################################\n")