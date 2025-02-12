

def intToRoman(num: int) -> str:
    if num < 1:
        return ""
    weigths = (("I","V"), ("X","L"), ("C","D"), ("M"))     

    str_value = str(num)
    output = ""
    for decimal, str_number in enumerate(str_value[::-1]):
        number = int(str_number)
        placeholder = ""
        if number > 5:
            if number == 9:
                placeholder = weigths[decimal][0] + weigths[decimal + 1][0]
            else:
                difference = number - 5
                number -= 5
                placeholder = weigths[decimal][1] +  weigths[decimal][0] * difference
        elif number == 5:
            placeholder = weigths[decimal][1]
        else:
            if number == 4:
                placeholder = weigths[decimal][0] + weigths[decimal][1]
            else:
                placeholder = weigths[decimal][0] * number
        output = placeholder + output
    return output



num = 3749
o = "MMMDCCXLIX"
val = intToRoman(num)
print(f"val: {val}, expected: {o} is equal: {val == o}")

num = 58
o = "LVIII"
val = intToRoman(num)
print(f"val: {val}, expected: {o} is equal: {val == o}")

num = 1994
o = "MCMXCIV"
val = intToRoman(num)
print(f"val: {val}, expected: {o} is equal: {val == o}")
