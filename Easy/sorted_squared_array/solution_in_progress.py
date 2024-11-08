def sortedSquaredArray(array):
    squareArray = []
    for num in array:
        square = num * num
        squareArray.append(square)
    squareArray.sort()
    return squareArray

# Test cases
print(sortedSquaredArray([-7, -3, 1, 9, 2]))    # Expected output: [1, 4, 9, 49, 81]
print(sortedSquaredArray([1, 2, 3, 4, 5]))      # Expected output: [1, 4, 9, 16, 25]
print(sortedSquaredArray([-5, -4, -3, -2, -1])) # Expected output: [1, 4, 9, 16, 25]
print(sortedSquaredArray([-3, -1, 0, 2, 4]))    # Expected output: [0, 1, 4, 9, 16]
print(sortedSquaredArray([]))                   # Expected output: []
