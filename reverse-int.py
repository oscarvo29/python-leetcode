



def reverse(x: int) -> int:
    output = str(x)[::-1]
    if x < 0:
        output = "-" + output[:-1]
    n = int(output)
    return n if n > -2147483647 and n < 2147483647 else 0

x = 123 # output = 321
print(reverse(x))

x = -123 # output = -321
print(reverse(x))

x = -120 # output = 21
print(reverse(x))
x = 1534236469 # output = 0
print(reverse(x))