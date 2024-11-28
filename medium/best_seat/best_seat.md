# Best Seat Problem

This function determines the best seat in a row of seats, represented as a list, where:
- `1` represents an occupied seat.
- `0` represents an empty seat.

The goal is to identify the index of the seat that is farthest away from any occupied seat.

---

## Approach

1. **Initialization**:
   - `maxSpace`: Tracks the largest segment of empty seats found so far.
   - `bestSeat`: Stores the index of the "best seat" in terms of maximum distance from any occupied seat.
   - `left` and `right`: Pointers used to explore segments of consecutive empty seats (`0s`).

2. **Iterate Over the Seats**:
   - Start with `left` pointing to the current position and use `right` to explore the segment of empty seats.
   - While `right` encounters empty seats (`0`), keep expanding the segment by incrementing `right`.

3. **Calculate the Number of Empty Seats**:
   - Compute the number of empty seats in the current segment as `count = right - left - 1`.

4. **Check for Maximum Space**:
   - If the `count` of the current segment exceeds `maxSpace`, update:
     - `maxSpace` to this new count.
     - `bestSeat` to the index of the seat in the middle of the segment: `(right + left) // 2`.

5. **Advance to the Next Segment**:
   - Move `left` to the `right` pointer, which now points to the next seat after the current segment.

6. **Return the Best Seat**:
   - After examining all segments, return the value of `bestSeat`, which holds the index of the best seat.

---

## Complexity Analysis

- **Time Complexity**: **O(n)**  
   - The function iterates over the array of seats once, processing each seat only once.
- **Space Complexity**: **O(1)**  
   - The solution uses a constant amount of extra space.

---

## Code

```python
def bestSeat(seats):  
    # Initialize variables to track the maximum space, the best seat index, and counters.
    maxSpace = 0
    bestSeat = -1
    left = 0

    # Iterate over the seats to find segments of consecutive empty seats (0s).
    while left < len(seats):
        right = left + 1
        
        # Expand the right pointer to find the end of the current segment of empty seats.
        while right < len(seats) and seats[right] == 0:
            right += 1

        # Calculate the number of empty seats in the segment.
        count = right - left - 1
        
        # If the current segment has more empty seats than previously recorded,
        # update the best seat index and the maximum space.
        if count > maxSpace:
            bestSeat = (right + left) // 2
            maxSpace = count
            
        # Move the left pointer to the next segment.
        left = right
    
    return bestSeat

# Example input
seats = [1, 0, 1, 0, 0, 0, 1]

# Run the function and print the result
result = bestSeat(seats)
print("Best seat index:", result)
