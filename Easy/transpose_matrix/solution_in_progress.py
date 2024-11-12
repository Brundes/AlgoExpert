def transposeMatrix(matrix):
    matrixTransposed = []
    for col in range(len(matrix[0])):
        rowCreated = []
        
        for row in range(len(matrix)):
            rowCreated.append(matrix[row][col])
            
        matrixTransposed.append(rowCreated)
        
    return matrixTransposed

# Example input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the function and print the result
transposed = transposeMatrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)
print("\nTransposed Matrix:")
for row in transposed:
    print(row)
