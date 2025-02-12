
def strStr(haystack: str, needle: str) -> int:
    needle_size = len(needle)
    max = len(haystack) - needle_size
    left = 0
    while left <= max:
        if haystack[left: left + needle_size] == needle:
            return left
        
        left += 1
    return -1

# haystack = "sadbutsad"
# needle = "sad"
# expected = 0
# o = strStr(haystack, needle)
# print(o)

# haystack = "leetcode"
# needle = "leeto"
# expected = -1
# o = strStr(haystack, needle)
# print(o)

haystack = "hello"
needle = "ll"
expected = 2
o = strStr(haystack, needle)
print(o)
