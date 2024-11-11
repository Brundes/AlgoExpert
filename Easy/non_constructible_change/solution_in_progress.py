def nonConstructibleChange(coins):
    coins.sort()
    
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    
    return currentChangeCreated + 1

# Example test cases
print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))  # Expected output: 20
print(nonConstructibleChange([1, 1, 1, 1, 1]))        # Expected output: 6
print(nonConstructibleChange([1, 2, 5]))              # Expected output: 4
print(nonConstructibleChange([]))                     # Expected output: 1
print(nonConstructibleChange([1, 1, 1, 1, 10]))       # Expected output: 5