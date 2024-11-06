# isValidSubsequence Explanation

This explanation is based on the problem: *Is Valid Subsequence*.

## Approach

The function `isValidSubsequence` checks whether a given sequence is a subsequence of a larger array. A subsequence appears in the same relative order but does not need to be consecutive.

1. **Initialize a Sequence Index**: We initialize an index `seqIdx` to track our position in the `sequence`. This helps us check each character in the sequence in the correct order.

2. **Loop through the Array**: For each element in the `array`, we:
   - Check if `seqIdx` equals the length of `sequence`. If so, we stop early since all elements of `sequence` have been matched.
   - If the current element in `array` matches the current element in `sequence[seqIdx]`, we increment `seqIdx` to move to the next element in `sequence`.

3. **Return the Result**: At the end of the loop, if `seqIdx` equals the length of `sequence`, it means every element of `sequence` was found in `array` in the correct order. In this case, we return `True`. If not, we return `False`.

## Complexity Analysis

- **Time Complexity**: O(n), where `n` is the number of elements in `array`. The function processes each element in `array` at most once.
- **Space Complexity**: O(1), as the function only uses a fixed amount of extra space.

## Code

```python
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
