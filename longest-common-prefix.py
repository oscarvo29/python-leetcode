
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs: list[str]) -> str:
    shortest_word = strs[0]
    for word in strs:
        if len(shortest_word) > len(word):
            shortest_word = word
    strs.remove(shortest_word)
    prefix = ""
    for idx, c in enumerate(shortest_word):
        for word in strs:
            if word[idx] != c:
                return prefix
        prefix += c

    return prefix
    
        
l = ["flower","flow","flight"]
output = longestCommonPrefix(l)
ex = "fl"
print(f"got: {output}, is correct = {output == ex}")

l = ["a", "b"]
output = longestCommonPrefix(l)
ex = ""
print(f"got: {output}, is correct = {output == ex}")

l = ["dog", "racecar", "car"]
output = longestCommonPrefix(l)
ex = ""
print(f"got: {output}, is correct = {output == ex}")
