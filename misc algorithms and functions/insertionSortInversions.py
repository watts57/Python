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

def insertionSortInversions(inputList):
    inversions = 0 #init as 0
    for i in range(1, len(inputList)): #while in range of inputList indices
        key = inputList[i] # value compared is key, which is inputList[i]
        j = i - 1 # j is one less than i

        while j >= 0 and key < inputList[j]: # while j is more than 0 and the key is less than index j
            inputList[j + 1] = inputList[j] # index to right of j becomes j
            j -= 1 # j moved left
            inversions += 1 #inversion has occurred; number has been moved


        inputList[j + 1] = key # key moves right
    print("Number of Inversions = " +str(inversions)) # print number of inversions when done





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
insertionSortInversions(inputList)
##print("10 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime

print("--------")
print("\n Time to sort 10 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####50 numbers#######")

getInputs(fileInput50, numbers50)
inputList =  numbers50
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("50 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 50 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####100 numbers#######")

getInputs(fileInput100, numbers100)
inputList = numbers100
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("00 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 100 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####150 numbers#######")

getInputs(fileInput150, numbers150)
inputList = numbers150
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("150 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 150 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####200 numbers#######")

getInputs(fileInput200, numbers200)
inputList = numbers200
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("200 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 200 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####250 numbers#######")

getInputs(fileInput250, numbers250)
inputList = numbers250
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("250 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 250 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####300 numbers#######")

getInputs(fileInput300, numbers300)
inputList = numbers300
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("300 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 300 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####350 numbers#######")

getInputs(fileInput350, numbers350)
inputList = numbers350
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("350 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 350 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####400 numbers#######")

getInputs(fileInput400, numbers400)
inputList = numbers400
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("400 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 400 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####450 numbers#######")

getInputs(fileInput450, numbers450)
inputList = numbers450
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("450 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 450 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####500 numbers#######")

getInputs(fileInput500, numbers500)
inputList = numbers500
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("500 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 500 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####1000 numbers#######")

getInputs(fileInput1000, numbers1000)
inputList = numbers1000
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("1000 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 1000 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####5000 numbers#######")

getInputs(fileInput5000, numbers5000)
inputList = numbers5000
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("5000 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 5,000 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########

print("####10000 numbers#######")

getInputs(fileInput10000, numbers10000)
inputList = numbers10000
startTime = float(time.time_ns())
totalInversionCount = []
insertionSortInversions(inputList)
##print("10000 numbers (from lab 4): " + str(inputList))
endTime = float(time.time_ns())
timeTaken = endTime - startTime
print("--------")
print("\n Time to sort 10,000 numbers with insertion sort (in nanoseconds): " + str(+timeTaken) + "\n")

print("--------")
#########