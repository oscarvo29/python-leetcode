

def twoSum(nums: list[int], target: int):
    for idx, number in enumerate(nums):
        for i, num in enumerate(nums):
            if idx != i:
                if number + num == target:
                    return [idx, i]




# def twoSum(nums: list[int], target: int):
#     for i, number in enumerate(nums):
#         bt = nums[0:i] + nums[i + 1:]
#         for j, numb in enumerate(bt):
#             if number + numb == target:
#                return [nums.index(number), nums.index(numb)]


nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

nums = [3, 3]
target = 6
print(twoSum(nums, target))

nums = [3, 2, 3]
target = 6
print(twoSum(nums, target))

nums = [2, 7, 10, 13, 14, 5]
target = 9
print(twoSum(nums, target))
