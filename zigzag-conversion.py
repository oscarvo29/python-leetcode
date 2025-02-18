

def convert(s: str, numRows: int) -> str:
    if len(s) == 1 or numRows == 1:
        return s

    zigzag: list[list[str]] = []
    for i in range(numRows):
        zigzag.append("")

    flag = 0
    idx = 0 
    while idx < len(s):
        if flag == 0:
            while flag < numRows:
                if idx == len(s):
                    break
                zigzag[flag] += s[idx]
                flag += 1
                idx += 1
            
            flag = numRows - 2
        else:
            zigzag[flag] += s[idx]
            flag -= 1
            idx += 1

    output = ""
    for row in zigzag:
        output += row
    return output



s = "PAYPALISHIRING"
numRows = 3
res = convert(s, numRows)
exp = "PAHNAPLSIIGYIR"
print(f"expexted: {exp}, got: {res}")
print(f"Is correct: {exp == res}")


s = "PAYPALISHIRING"
numRows = 4
res = convert(s, numRows)
exp = "PINALSIGYAHRPI"
print(f"expexted: {exp}, got: {res}")
print(f"Is correct: {exp == res}")

s = "A"
numRows = 1
res = convert(s, numRows)
exp = "A"
print(f"expexted: {exp}, got: {res}")
print(f"Is correct: {exp == res}")