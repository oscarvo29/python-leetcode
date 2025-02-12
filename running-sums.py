def closure(n: list[int]):
    if len(n) == 1:
        output.append(n[0])
        return n[0]
    item = n.pop()
    value = item + closure(n)
    output.append(value)
    return value


output = []
nums = [1, 2, 3, 4]
closure(nums)
print(f"nums: {nums} \n output: {output}\n\n")

output = []
nums = [1, 1, 1, 1, 1]
closure(nums)
print(f"nums: {nums} \n output: {output}\n\n")

output = []
nums = [3, 1, 2, 10, 1]
closure(nums)
print(f"nums: {nums} \n output: {output}\n\n")


# x = nums.pop()
# print(x)