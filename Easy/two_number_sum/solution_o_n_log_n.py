def twoNumberSum(array, targetSum):
    #Solution O(n*log(n))
    
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        result = array[left] + array[right]
        if result == targetSum:
            return [array[left], array[right]]
        elif result < targetSum:
            left += 1
        elif result > targetSum:
            right -= 1

    return []

# Test the function
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))