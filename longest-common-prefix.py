

def longestCommonPrefix(strs: list[str]) -> str:
    counter = 1
    while True:
        prefix = strs[0][:counter]

        for word in strs:
            if len(word) <= 0:
                return ""
            if counter >= len(word) and counter != 1:
                return prefix

            if word[:counter] != prefix:
                if counter == 1:
                    return ""
                return prefix[:-1]
        counter += 1
    
        
l = ["flower","flow","flight"]
print(longestCommonPrefix(l))
l = ["a", "b"]


print(longestCommonPrefix(l))
