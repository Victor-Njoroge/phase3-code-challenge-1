def numbers():
    threeNumbers=[]
    negCount = 0
    posCount = 0
    for i in range (3):
        number=int(input("Enter your three numbers: "))
        threeNumbers.append(number)
        if number > 0:
            posCount +=1
        elif number < 0:
            negCount +=1
            
    print(threeNumbers)
    if posCount == 2 and negCount == 1:
        print(True)
    else :
        print(False)
   
numbers()