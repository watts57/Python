def palindrome(stringList, index, fileInput):


    if index == -1: # if stringList is not yet populated (this is first recursion)
        with open(fileInput, "r") as source: # source represents fileInput being read in as a file
            for line in source: # for each line in fileInput
                stringAdded = line
                #print(stringAdded)
                stringList.append(stringAdded.strip("\n",)) #add to list but remove newline (\n) first
            source.close # close text file
        return palindrome(stringList, index + 1, fileInput) # return with index incremented by one and stringList populated




    while index < len(stringList): # while within length of stringList
        stringChecked = stringList[index]
        stringReversed = stringChecked[::-1] # reverse using slicing
        #print(stringChecked)# print current string being checked
        #print(stringReversed) # print reversed version of string being checked
        if stringChecked == stringReversed:
            print(str(stringChecked) + " is a palindrome")
        else:
            print(stringChecked + " is NOT a palindrome")



        return palindrome(stringList, index+1, fileInput) # return and do recursion again, increment index by one

    print("done")
    return# end program after all conditions met

stringList = [] # holds strings
index = -1 # initialize to -1 so that program knows to populate stringList
fileInput = "strings.txt" # holds fileName -- Note to TA-- I just find this easier to keep track of
palindrome(stringList, index,fileInput) # call function recursively