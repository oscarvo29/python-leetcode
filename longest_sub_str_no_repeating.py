


def lenthOfLongestSubString(s: str) -> int:
    first_unique = 0
    max_length = 0
    used_letters = set()
    for index in range(len(s)):
        current = s[index]
        while current in used_letters:
            used_letters.remove(s[first_unique])
            first_unique += 1

        used_letters.add(current)
        max_length = max_length if max_length > index - first_unique + 1 else index - first_unique + 1
    return max_length

        
# print(out[output], out[sub])
# letters = dict()

# letters['a'] = 1
# letters['b'] = 1
# letters['c'] = 1
# letters['d'] = 1

# if letters.get('v') == None:
#     letters['v'] = 1

# print(letters)
# print(letters['v'])

lenthOfLongestSubString("abcabcbb")
lenthOfLongestSubString("bbbbb")
lenthOfLongestSubString(" ")
lenthOfLongestSubString("pwwkew")
lenthOfLongestSubString("aab")