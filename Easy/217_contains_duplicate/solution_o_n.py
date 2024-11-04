class Solution(object):
    def containsDuplicate(self, nums):
        # Create HashMap to store values of "nums"
        # Check if it exists in set, insert it in negative case
        # True -> if the value is duplicate
        # False -> if it reaches the entire list without duplicates

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

# Test cases
solution = Solution()
nums_with_duplicates = [1, 2, 3, 4, 5, 2]
nums_without_duplicates = [1, 2, 3, 4, 5]

print(solution.containsDuplicate(nums_with_duplicates))  # Expected output: True
print(solution.containsDuplicate(nums_without_duplicates))  # Expected output: False