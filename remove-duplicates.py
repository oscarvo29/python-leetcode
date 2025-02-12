
expectedNums = []
def removeDuplicates(nums: list[int]) -> int:
    duplicates = set()
    size = 0
    for idx, num in enumerate(nums):
        if num in duplicates:
            continue
        duplicates.add(num)
        expectedNums.append(num)
        size += 1
    return size


nums = [1,1,2]
expected = 2 #[1, 2]
o = removeDuplicates(nums)
print(o)

nums = [0,0,1,1,1,2,2,3,3,4]
expected = 5 #[0,1,2,3,4,_,_,_,_,_]
o = removeDuplicates(nums)
print(o)
