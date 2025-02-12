


def romanToInt(s: str) -> int:
    weigths = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    prev = None
    for roman in s[::-1]:
        current = weigths[roman]
        if prev == None:
            prev = current
            sum += current
            continue

        if current < prev:
            sum -= current
            prev = current
        elif current == prev:
            sum +=  current
            prev = current
        else:
            sum += current
            prev = current
    return sum


s = "III"
o = 3
romanToInt(s)

s = "LVIII"
o = 58
romanToInt(s)

s = "MCMXCIV" 
o = 1994
romanToInt(s)

"""
    tjek char + tjek char der er efter følgene
    så
    og tjek heiraki
    C før M 
"""


"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000



        MCMXCIV

        1000    sum 1000
        100     c < prev -> sub 900
        1000    c > prev -> add 1900
        10      c < prev -> sub 1890
        100     c > prev -> add 1990
        1       c < prev -> sub 1989
        5       c > prev -> add 1994
"""