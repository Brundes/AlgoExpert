def twoNumberSum(array, targetSum):
    # Solution O(n^2)
    for i in range(len(array)):
        x = array[i]
        
        for j in range(i + 1, len(array)):
            y = array[j]
            result = x + y
            
            if result == targetSum:
                return x, y
    return []

# Test the function
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))