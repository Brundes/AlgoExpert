def twoNumberSum(array, targetSum):
    #Solution O(n)

    # [4, 6, 1] --- target = 5
    # Result = target - x
    # Result = 5 - 4  => result = 1
    # Stores 4 in Hash && check if there is "1" in Hash

    # Result = 5 - 6
    # Result = -1
    # Stores 6 in Hash && check if there is "-1" in Hash

    # result = 5 - 1
    # result = 4
    # Stores 1 in Hash && check if there is "4" in Hash

    map = {}
    for num in array:
        result = targetSum - num
        
        if result in map:
            return result,num
            
        else:
            map[num] = True
    
    return []


# Test the function
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))