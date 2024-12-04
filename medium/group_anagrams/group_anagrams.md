# Group Anagrams Problem

This function groups strings into collections of anagrams. An **anagram** is a word formed by rearranging the letters of another, such as `"listen"` and `"silent"`. The function organizes words into groups where each group contains words that are anagrams of each other.

---

## Approach

1. **Initialize a Map**:
   - Use a dictionary `map` to group words based on their sorted character sequences.
   - The key represents the sorted version of a word, and the value is a list of words that match that sorted order.

2. **Iterate Through the Words**:
   - For each word in the input list:
     - **Sort the Characters**: Rearrange the word's characters in alphabetical order to create a unique identifier for all anagrams of the word.
     - **Update the Map**:
       - If the sorted word is already in the map, append the current word to the list of anagrams.
       - If the sorted word is not in the map, create a new key-value pair with the sorted word as the key and a list containing the current word as the value.

3. **Return the Groups**:
   - Extract the values from the dictionary (each value is a list of anagrams) and return them as a list of lists.

---

## Complexity Analysis

- **Time Complexity**: **O(n \* k \* log(k))**
   - `n`: Number of words in the input list.
   - `k`: Average length of each word.
   - Sorting each word takes `O(k \* log(k))`, and this is done for all `n` words.
- **Space Complexity**: **O(n \* k)**
   - Space is used to store the dictionary and the grouped words.

---

## Code

```python
def groupAnagrams(words):
    map = {} 
    
    for string in words:
        # Sort each string and use it as a key
        stringSorted = "".join(sorted(string))
        if stringSorted in map:
            map[stringSorted].append(string)
        else:
            map[stringSorted] = [string]
    return list(map.values())

# Predefined input
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Run the function with the predefined input
result = groupAnagrams(words)
print("Grouped Anagrams:", result)

