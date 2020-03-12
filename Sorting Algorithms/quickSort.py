
import time

#This "automates" loading text files and saves a lot of lines of manual coding
def getInputs(sourceText, targetArray):

    # first let's load all the input files up
    ########100########
    for line in open(sourceText, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                targetArray.append(int(i))  # add the integer to list



'''
PARTITIONING:

HIGH LEVEL OVERVIEW FROM LECTURE

partition (A, low, high)
pivotitem = A [low]
i = low + 1 for j = low +1 to high      
do if A [ j ] < pivotitem       
exchange A [ j ] and A [ i ]        
then i = i + 1
exchange A[low] and A[i - 1] 
--------
in my code....

....I had trouble getting the other way to work, but it's probably just because I've been awake for 2 days straight...crazy work schedule this week.

inputList is A
pivotItem is just called pivot


I had an easier time figuring out this high level algorithm instead


if inputList[j] <= pivot, then i = i+1, 
THEN...

if j is greater or equal to pivot
swap inputList[i] and inputList[j], 

written like this--> inputList[i], inputList[j] = inputList[j], inputList[i]

OTHERWISE

inputList[i+1] and inputList[high] swap with each other
-----

MY FUNCTION IS BELOW:
'''



def partition(inputList, low, high):
    i = (low - 1)  # this is the index of the small element
    pivot = inputList[high]  # set up the pivot index

    for j in range(low, high): #iterate in j from low to high index


        # if index j is equal to or less than pivot
        if inputList[j] <= pivot:
            # add 1 to lesser element
            i = i + 1
            inputList[i], inputList[j] = inputList[j], inputList[i] #swap index i and j of inputList

    inputList[i + 1], inputList[high] = inputList[high], inputList[i + 1] #swap i+1 and high of inputList
    return (i + 1)


def quickSort(inputList):
    #just calls quickSortRecursive
    quickSortRecursive(inputList, 0, len(inputList)-1) # params are... quickSortRecursive(inputList, low, high)....low is 1st index....high is set to last index
        #inputList param specified in function call below
        #inputList values are the arrays/lists at the bottom called numbers at the bottom
        # example...numbers100 has the values from 100.txt stored in it.
        #values in array comes from the getInputs(sourceText, targetArray) function at the top of this file

def quickSortRecursive(inputList,low,high):
    #if low  is less than high
    if low < high:
        part = partition(inputList,low,high) #partition the inputList...'part' refers to this....now do partitioning and recursive calls
        quickSortRecursive(inputList,low,part-1)
        quickSortRecursive(inputList,part+1, high)

    

def findPivot(inputList,low,high):
    #fairly self explanatory. This function sets the pivot
    #pivotIndex is the location (index) of pivot in array
    #pivotValue is the value stored at that index
    pivotIndex = findPivot(inputList,low,high)
    pivotValue = inputList[pivotIndex]
    inputList[pivotIndex], inputList[low] = inputList[low], inputList[pivotIndex]
    boundary = low #stopping point of partitioning

    for i in range(low, high+1): #from low to high + 1m check if index i is less than value of pivot
        if inputList[i] < pivotValue: # if so...
            boundary += 1 #increment value of boundary
            inputList[i], inputList[boundary] = inputList[boundary], inputList[i] # in this syntax scheme, values are assigned in order of appearance  ...example:  X, Y = 1, 2..... then X = 1, Y = 2
    inputList[low], inputList[boundary] = inputList[boundary], inputList[low]

    return boundary

def findMedian(inputList):
    inputSize = len(inputList)-1

    if inputSize % 2 == 0: # if inputList has even length
        median = inputList[inputSize / 2]
    else:
        median =  inputList[(inputSize+1)//2]
    return median








#now call the functions and execute the methods

print("\n************************************Beginning of Program*************************************************\n")
print("\nWilliam Watts || BlazerID: watts57@uab.edu || B Number: B01026111 \n")
print("\nCS 303....Lab5....Problem Number 1....\n")
print("\nquickSort\n")


print("The arrays are only set to print on the first 2 (smallest) inputs....but all of these can be set up to print")
print("NOTE TO USER: when examining code....")
print("You can remove '#' from in front of print command for 'print(numbers[insert amount of numbers])' to see the sorted array \n...printing large arrays cluttered console window\n")


############100.txt

# Numbers to sort.....these are read from text files provided....
#NOT INCLUDED IN RUNNING TIME PER INSTRUCTIONS... THIS IS FILE INPUT... INSTRUCTIONS SAY DO NOT INCLUDE FILE I/O TIME
print("\n................[100 Numbers].....................\n")
print("getting inputs...")
numbers100 = []
fileInput100 =  "100.txt"
getInputs(fileInput100, numbers100)

#QUICKSORT NOW THAT EVERYTHING IS SET UP


print("Began quickSort of 100.txt...which is stored in numbers100 (subsequent calls work the same way)...TIMER STARTED")

startTime = time.time_ns()
quickSort(numbers100)
endTime = time.time_ns()
resultTime = endTime - startTime

print(numbers100)
print("Time taken to perform quickSort on 100 numbers: "+ str(resultTime))
print("\nCompleted quickSort of 100 numbers\n")

############1000.txt

print("\n................[1000 Numbers].....................\n")
numbers1000 = []
fileInput1000 = "1000.txt"
getInputs(fileInput1000, numbers1000)

startTime = time.time_ns()
quickSort(numbers1000)
endTime = time.time_ns()
resultTime = endTime - startTime
print(numbers1000)
print("Time taken to perform quickSort on 1,000 numbers: "+ str(resultTime))
print("\nCompleted quickSort of 1000 numbers\n")

############5000.txt
print("\n................[5000 Numbers].....................\n")
numbers5000 = []
fileInput5000 = "5000.txt"
getInputs(fileInput5000, numbers5000)

startTime = time.time_ns()
quickSort(numbers5000)
endTime = time.time_ns()
resultTime = endTime - startTime


#print(numbers5000)
print("Time taken to perform quickSort on 5,000 numbers: "+ str(resultTime))

print("\nCompleted quickSort of 5000 numbers\n")

############50000.txt
print("\n................[50000 Numbers].....................\n")
numbers50000 = []
fileInput50000 = "50000.txt"
getInputs(fileInput50000, numbers50000)

startTime = time.time_ns()
quickSort(numbers50000)
endTime = time.time_ns()
resultTime = endTime - startTime
#print(numbers50000)
print("Time taken to perform quickSort on this many numbers: "+ str(resultTime))


print("\nCompleted quickSort of 50000 numbers\n")

############100000.txt
print("\n................[100000 Numbers].....................\n")
numbers100000 = []
fileInput100000 = "100000.txt"
getInputs(fileInput100000, numbers100000)

startTime = time.time_ns()
quickSort(numbers100000)
endTime = time.time_ns()
resultTime = endTime - startTime

#print(numbers100000)
print("Time taken to perform quickSort on 100,000 numbers: "+ str(resultTime))


print("\nCompleted quickSort of 100000 numbers\n")

############500000.txt
print("\n................[500000 Numbers].....................\n")
numbers500000 = []
fileInput500000 = "500000.txt"
getInputs(fileInput500000, numbers500000)

startTime = time.time_ns()
quickSort(numbers500000)
endTime = time.time_ns()
resultTime = endTime - startTime
#print(numbers500000)
print("Time taken to perform quickSort on 500,000 numbers: "+ str(resultTime))


print("\nCompleted quickSort of 500000 numbers\n")
########NUMBER TWO

#seems to make the most sense to have this piggyback off of the quickSort since our arrays are already sorted now

print("\nNumber 2: Find the median of an array....use same files as previous question \n")

print("\nMedians of these arrays:\n")

print("\nThe median of numbers100 (array from 100.txt) is : "+ str(findMedian(numbers100)))
#print("\nCheck: Index of median value is: "+ str(numbers100.index(findMedian(numbers100))))
#print("Check: array[index of median] = : " + str(numbers100[(numbers100.index(findMedian(numbers100)))]))
print("\nThe median of numbers1000 (array from 1000.txt) is : "+ str(findMedian(numbers1000)))
print("\nThe median of numbers5000 (array from 5000.txt) is : "+ str(findMedian(numbers5000)))
print("\nThe median of numbers50000 (array from 50000.txt) is : "+ str(findMedian(numbers50000)))
print("\nThe median of numbers10000 (array from 100000.txt) is : "+ str(findMedian(numbers100000)))
print("\nThe median of numbers500000 (array from 500000.txt) is : "+ str(findMedian(numbers500000)))

print("\n###############\nEnd of Program.")
print("\n-------------------------------")
#####END OF PROJECT