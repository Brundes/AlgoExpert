def threeNumberSum(array, targetSum):
    # Take the first number with a for loop
    # Implement a two-pointer to discover which sum is the ideal

    finalSum = []
    array.sort()  # Sort the array to use two-pointer approach

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            currSum = array[i] + array[left] + array[right]
            if currSum == targetSum:
                finalSum.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currSum < targetSum:
                left += 1
            else:
                right -= 1
                
    return finalSum

# Example usage
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print(threeNumberSum(array, targetSum))
