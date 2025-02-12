
def findSubstring(s: str, words: list[str]) -> list[int]:
    output = []
    step = len(words[0])
    words_size = len(words)

    if len(s) == step:
        if s in words and not len(s) < words_size:
            return [0]
        else:
            return []

    def closure(s: str, words: list[str], is_recurssive: bool = False):
        if len(s) == step:
            if s in words and words_size == 1 and is_recurssive:                
                return True
            else:
                return False
        
        idx = 0
        while idx <= len(s) - step:
            word = s[idx: idx + step]
            if words_size == 1:
                if word in words:
                    output.append(idx)
            else:
                if word in words:
                    if len(words) == 1 and is_recurssive:
                        return True

                    sub_words = words[0:]
                    sub_words.remove(word)
                    sub_str = s[idx + step:]
                    is_valid = closure(sub_str, sub_words, is_recurssive=True)
                    if is_valid:
                        if not is_recurssive:
                            output.append(idx)
                        else:
                            return True
                    if is_recurssive:
                        return False
                else:
                    if is_recurssive:
                        return False
            idx += 1
    closure(s, words)
    return output


# s = "barfoothefoobarman"
# words = ["foo","bar"]
# output = [0,9]
# o = findSubstring(s, words)
# print(o)

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# output = []
# o = findSubstring(s, words)
# print(o)

# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]
# output = [6,9,12]
# o = findSubstring(s, words)
# print(o)

# s = "a"
# words = ["a","a"]
# output = [0]
# o = findSubstring(s, words)
# print(o)


s = "bcabbcaabbccacacbabccacaababcbb"
words = ["c","b","a","c","a","a","a","b","c"]
output = [6,16,17,18,19,20]
o = findSubstring(s, words)
print(f"expected: {output}, got: {o}, is correct: {o == output}")

s = "mississippi"
words = ["is"]
output = [1, 4]
o = findSubstring(s, words)
print(f"expected: {output}, got: {o}, is correct: {o == output}")

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
output = [8]
o = findSubstring(s, words)
print(f"expected: {output}, got: {o}, is correct: {o == output}")




