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
