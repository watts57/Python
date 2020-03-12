# selection sort algorithm based on example pseudocode and prior assignment given to us in CS 330 Lab for similar problem

import time


def insertionSort():
    # first let's load all the input files up
    ########100########
    for line in open(fileInput100, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                numbers100.append(int(i)) # add the integer to list

    #print()
    #print(100)
    #print(numbers100)
    ########1000########
    for line in open(fileInput1000, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                numbers1000.append(int(i))  # add the integer to list
    #print()
    #print(1000)
    #print(numbers1000)
    ##########5000########
    for line in open(fileInput5000, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                numbers5000.append(int(i)) # add the integer to list
    #print()
    #print(5000)
    #print(numbers5000)
    ########50000########
    for line in open(fileInput50000, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                numbers50000.append(int(i)) # add the integer to list
    #print()
    #print(50000)
    #print(numbers50000)
    ##########100000##########
    for line in open(fileInput100000, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                numbers100000.append(int(i)) # add the integer to list
    #print()
    #print(100000)
    #print(numbers100000)
    ########500000########
    for line in open(fileInput500000, 'r'):  # read input file
        numString = line

        for i in numString.split():  # use spaces to separate integers
            if i.isdigit():  # if integer found
                numbers500000.append(int(i))  # add the integer to list
    #print()
    #print(500000)
    #print(numbers500000)

    ##########




    ####SELECTION SORT -- based on Dr. Unan's example pseudocode and my work for CS 330 assignment similar to this one -- see other project if lost

#######SORT 100
    print("at line 78")
    start100 = float(time.time_ns())
    for i in range(1, len(numbers100)):
        key = numbers100[i]
        j = i - 1
        while j >= 0 and key < numbers100[j]:
            numbers100[j + 1] = numbers100[j]
            j -= 1
        numbers100[j + 1] = key
        print("SORT 100...key = " + str(key) + "  i = " + str(i) + "  j = " + str(j))
        ################
    end100 = float(time.time_ns())
    time100 = end100 - start100
    print("\n Time to sort 100 numbers with insertion sort (in nanoseconds): " + str(+time100)+"\n")


#######SORT 1000
    print("at line 93")
    start1000 = float(time.time_ns())
    for i in range(1, len(numbers1000)):
        key = numbers1000[i]
        j = i - 1
        while j >= 0 and key < numbers1000[j]:
            numbers1000[j + 1] = numbers1000[j]
            j -= 1
        numbers1000[j + 1] = key
        print("SORT1000...key = " + str(key) + "  i = " + str(i) + "  j = " + str(j))
        ################
    end1000 = float(time.time_ns())
    time1000 = end1000 - start1000
    print("\n Time to sort 1000 numbers with insertion sort (in nanoseconds): " + str(+time1000) + "\n")
#######SORT 5000
    print("at line 108")
    start5000 = float(time.time_ns())
    for i in range(1, len(numbers5000)):
        key = numbers5000[i]
        j = i - 1
        while j >= 0 and key < numbers5000[j]:
            numbers5000[j + 1] = numbers5000[j]
            j -= 1
        numbers5000[j + 1] = key
        print("SORT 5,000...key = " + str(key) + "  i = " + str(i) + "  j = " + str(j))
        ################
    end5000 = float(time.time_ns())
    time5000 = end5000 - start5000
    print("\n Time to sort 5000 numbers with insertion sort (in nanoseconds): " + str(+time5000) + "\n")
#######SORT 50000
    print("at line 122...50k numbers")
    start50000 = float(time.time_ns())
    for i in range(1, len(numbers50000)):
        key = numbers50000[i]
        j = i - 1
        while j >= 0 and key < numbers50000[j]:
            numbers50000[j + 1] = numbers50000[j]
            j -= 1
        numbers50000[j + 1] = key
        print("SORT 50,0000...key = " + str(key) + "  i = " + str(i) + "  j = " + str(j))
        ################
    end50000 = float(time.time_ns())
    time50000 = end50000 - start50000
    print("\n Time to sort 50000 numbers with insertion sort (in nanoseconds): " + str(+time50000) + "\n")
#######SORT 100000
    print("at line 136....100k numbers")
    start100000 = float(time.time_ns())
    for i in range(1, len(numbers100000)):
        key = numbers100000[i]
        j = i - 1
        while j >= 0 and key < numbers100000[j]:
            numbers100000[j + 1] = numbers100000[j]
            j -= 1
        numbers100000[j + 1] = key
        print("SORT 100,000...key = " + str(key) + "  i = " + str(i) + "  j = " + str(j))
        ################
    end100000 = float(time.time_ns())
    time100000 = end100000 - start100000
    print("\n Time to sort 100000 numbers with insertion sort (in nanoseconds): " + str(+time100000) + "\n")
#######SORT 500000
    print("at line 150....500k numbers")
    start500000 = float(time.time_ns())
    for i in range(1, len(numbers500000)):
        key = numbers500000[i]
        j = i - 1
        while j >= 0 and key < numbers500000[j]:
            numbers500000[j + 1] = numbers500000[j]
            j -= 1
        numbers500000[j + 1] = key
        print("SORT 500,000...key = "+ str(key) + "  i = " + str(i) + "  j = "+str(j))
        ################
    end500000 = float(time.time_ns())
    time500000 = end500000 - start500000
    print("\n Time to sort 500000 numbers with insertion sort (in nanoseconds): " + str(+time500000) + "\n")
    return

numbers100 = []
numbers1000 = []
numbers5000 = []
numbers50000 = []
numbers100000 = []
numbers500000 = []

listOfInputs = [numbers100, numbers1000, numbers5000, numbers50000, numbers100000, numbers500000]

fileInput100 = "100.txt"
fileInput1000 = "1000.txt"
fileInput5000 = "5000.txt"
fileInput50000 = "50000.txt"
fileInput100000 = "100000.txt"
fileInput500000 = "500000.txt"

insertionSort()
