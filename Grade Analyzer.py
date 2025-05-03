sName = input("What is your name")
iTest1 = int(input("Enter Test1 Score: "))
iTest2 = int(input("Enter Test2 Score: "))
iTest3 = int(input("Enter Test3 Score: "))
iTest4 = int(input("Enter Test4 Score: "))
sDrop = input("Drop Lowest Grade('Y' for yes and 'N' for no): ")

if iTest1 <0 or iTest2 <0 or iTest3 <0 or iTest4 <0:
    print("Test score great than 0")
    exit()

if sDrop == "Y" or sDrop == "y":
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        iLowest = iTest1
    elif iTest2 <= iTest3 and iTest2 <= iTest4:
        iLowest = iTest2
    elif iTest3 <= iTest4:
        iLowest = iTest3
    else:
        iLowest = iTest4
    iNumber0fTests = 3
elif sDrop == "N" or sDrop == "n":
        iLowest = 0
        iNumber0fTests = 4
else:
    print("Enter Y or N")
    exit()

fAverage = (iTest1 + iTest2 + iTest3 + iTest4 - iLowest) / iNumber0fTests

if fAverage>= 97.0:
    sLetter = "A+"
elif fAverage>= 94.0:
    sLetter = "A"
elif fAverage>= 90.0:
    sLetter = "A-"
elif fAverage>= 87.0:
    sLetter = "B+"
elif fAverage>= 84.0:
    sLetter = "B"
elif fAverage>= 80.0:
    sLetter = "B-"
elif fAverage>= 77.0:
    sLetter = "C+"
elif fAverage>= 74.0:
    sLetter = "C"
elif fAverage>= 70.0:
    sLetter = "C-"
elif fAverage>= 67.0:
    sLetter = "D+"
elif fAverage>= 64.0:
    sLetter = "D"
elif fAverage>= 60.0: 
    sLetter = "D-"
else:
    sLetter = "F"
    
print(sName, "'s test avarage is ",format(fAverage,".1f"))

print("Letter Grade For The Test Is", sLetter)




      


    

        
              
