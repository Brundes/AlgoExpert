# Anagram Check Explanation

This explanation is based on the LeetCode problem: [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/).

## Approach

We create a dictionary called `count_map` to store the frequency of each character. The keys represent characters, and the values represent their frequencies in the strings.

1. **Check Lengths**: First, we check if the lengths of the strings `s` and `t` are different. If they are, they cannot be anagrams, so we return `False` immediately.

2. **Count Frequencies in `s`**: We iterate over each character in `s`. For each character, we update `count_map`:
   - If the character already exists as a key in `count_map`, we increment its count.
   - If it doesn’t exist, we add it to `count_map` with an initial count of 1.

3. **Adjust Frequencies with `t`**: We then iterate over each character in `t`. For each character:
   - If it exists in `count_map`, we decrement its count by 1.
   - If it does not exist in `count_map`, it means `t` has a character not found in `s`, so we return `False` immediately.

4. **Verify Counts**: After adjusting counts with both strings, we check each value in `count_map`. If any frequency is non-zero, it means there’s an imbalance between the occurrences of that character in `s` and `t`, indicating they’re not anagrams. We return `False` in this case.

5. **Return True if All Counts are Zero**: If we reach this point without returning `False`, all character counts have canceled out, meaning `s` and `t` have the same characters with the same frequencies. Thus, we return `True`, confirming they are anagrams.

This approach efficiently compares character frequencies between the two strings by counting in one pass and adjusting in another, ensuring that all frequencies cancel to zero if they are true anagrams.

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
