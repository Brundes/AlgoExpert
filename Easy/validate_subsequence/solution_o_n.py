def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

# Example input where the output should be True
array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, 10]
print("First example: ", isValidSubsequence(array1, sequence1))  # Expected output: True

# Example input where the output should be False
array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [1, 6, 10, -1]
print("Second example: ", isValidSubsequence(array2, sequence2))  # Expected output: False