# Anagram Check Explanation

This explanation is based on the LeetCode problem: [Valid Anagram](https://leetcode.com/problems/valid-anagram/solutions/3687854/3-method-s-c-java-python-beginner-friendly/).

## Approach

We create a dictionary called `count_map` to store the frequency of each character. The keys represent characters, and the values represent their frequencies in the strings.

1. **Check Lengths**: First, we check if the lengths of the strings `s` and `t` are different. If they are, they cannot be anagrams, so we return `False` immediately.

2. **Count Frequencies in `s`**: We iterate over each character in `s`...

## Complexity Analysis

The time complexity of this solution is **O(n)**, where `n` is the total number of characters in both strings. 

## Code

```python
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
