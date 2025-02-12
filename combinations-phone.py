keyboard = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}

def letterCombinations(digits: str) -> list[str]:
    if digits == "" or digits == "1":
        return []
    output = []
    size = len(digits)
    if size == 1:
        for c in keyboard[digits]:
            output.append(c)
        return output

    def closure(current: str, digits: str, debth: int):
        if debth == size - 1:
            for c in keyboard[digits]:
                output.append(current + c)
            return
        
        digit = digits[0]
        for c in keyboard[digit]:
            new_digits = digits[1:]
            closure(current + c, new_digits, debth + 1)

    closure("", digits, 0)
    return output

digits = "23"
output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
o = letterCombinations(digits)
print(o)

digits = ""
output = []
o = letterCombinations(digits)
print(o)

digits = "2"
output = ["a", "b", "c"]
o = letterCombinations(digits)
print(o)
