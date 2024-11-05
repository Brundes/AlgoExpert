class Solution(object):
    def isAnagram(s, t):
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

s = "anagram"
t = "nagaram"
boolean = str(Solution.isAnagram(s,t))

print("It is " + boolean + " that " + s + " and " + t + " are anagrams of each other.")