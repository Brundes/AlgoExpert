def smallestDifference(arrayOne, arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()
    minDifPair = []
    
    minimumDif = float("inf")
    
    indexOne = 0
    indexTwo = 0
    
    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        integerOne = arrayOne[indexOne]
        integerTwo = arrayTwo[indexTwo]
        
        if integerOne < integerTwo:
            currentDif = integerTwo - integerOne
            indexOne += 1
        elif integerOne > integerTwo:
            currentDif = integerOne - integerTwo
            indexTwo += 1
        else:
            return [integerOne, integerTwo]

        if minimumDif > currentDif:
            minimumDif = currentDif
            minDifPair = [integerOne, integerTwo]
            
    return minDifPair

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

result = smallestDifference(arrayOne, arrayTwo)
print(f"The pair with the smallest difference is: {result}")