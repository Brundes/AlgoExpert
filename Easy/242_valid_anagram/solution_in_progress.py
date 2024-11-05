class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count_map = {}
        for char in s:
            if char in count_map:
                count_map[char] += 1
            else:
                count_map[char] = 1

        for char in t:
            if char in count_map:
                count_map[char] -= 1

                if count_map[char] < 0:
                    return False
            else:
                return False

        return True

# Create an instance of Solution
solution = Solution()

# Test the function
s = "anagram"
t = "nagaram"
boolean = solution.isAnagram(s, t)

print("It is " + str(boolean) + " that " + s + " and " + t + " are anagrams of each other.")
