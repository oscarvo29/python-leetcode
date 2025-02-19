
"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.
"""


def myAtoi(s: str) -> int:
    INT32_MIN = -2_147_483_648  # -2^31
    INT32_MAX = 2_147_483_647   # 2^31 - 1
    if s == "":
        return 0
      
    number = ""
    is_negative = ""
    s = s.strip()
    
    for i, c in enumerate(s):
        if i == 0:
            if c == '-':
                is_negative = c
                continue
            if c == '+':
                continue
        char_value = ord(c)
        if char_value <= 57 and char_value >= 48:
            number += c
        else:
            break

    if number != "":
        value = int(is_negative+number)
        return max(INT32_MIN, min(value, INT32_MAX))
    return 0 


s = "42"
expected = 42
result = myAtoi(s)
print(f"got: {result} is correct: {result == expected}")

s = "   -042"
expected = -42
result = myAtoi(s)
print(f"got: {result} is correct: {result == expected}")

s = "1337c0d3"
expected = 1337
result = myAtoi(s)
print(f"got: {result} is correct: {result == expected}")

s = "0-1"
expected = 0
result = myAtoi(s)
print(f"got: {result} is correct: {result == expected}")

s = "words and 987"
expected = 0
result = myAtoi(s)
print(f"got: {result} is correct: {result == expected}")

s = "-91283472332"
expected = -2147483648
result = myAtoi(s)
print(f"got: {result} is correct: {result == expected}")