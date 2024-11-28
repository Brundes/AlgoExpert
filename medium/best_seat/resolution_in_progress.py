def bestSeat(seats):  
    # Initialize variables to track the maximum space, the best seat index, and counters.
    maxSpace = 0
    bestSeat = -1
    count = 0
    left = 0

    # Iterate over the seats to find segments of consecutive empty seats (0s).
    while left < len(seats):
        right = left + 1
        
        # Expand the right pointer to find the end of the current segment of empty seats.
        while right < len(seats) and seats[right] == 0:
            right += 1

        # Calculate the number of empty seats in the segment.
        count = right - left - 1
        #print("Valor de count: ", count)
        
        # If the current segment has more empty seats than previously recorded,
        # update the best seat index and the maximum space.
        if count > maxSpace:
            bestSeat = (right + left) // 2
            #print("Valor de bestSeat", bestSeat)
            maxSpace = count
            
        # Move the left pointer to the next segment.
        left = right
    
    #print("último valor", bestSeat)
    return bestSeat

# Example input
seats = [1, 0, 1, 0, 0, 0, 1]

# Run the function and print the result
result = bestSeat(seats)
print("Best seat index:", result)
