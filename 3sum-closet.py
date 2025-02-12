
def threeSumClosest(nums: list[int], target: int) -> int:
    if len(nums) < 3:
        return 0 
    
    if len(nums) == 3:
        return nums[0] + nums[1] + nums[2] 

    sorted_numbers = tuple(sorted(nums))
    output = 0
    distance = 0
    for idx, n in enumerate(sorted_numbers):
        if idx == len(sorted_numbers) -1:
             return output
        
        left = idx + 1
        right = len(sorted_numbers) - 1

        if idx == 0:
            output = n + sorted_numbers[left] + sorted_numbers[right]
            distance = target - output 

        while left < right:
            left_number = sorted_numbers[left]
            right_number = sorted_numbers[right]
            placeholder = n + left_number + right_number
            difference = target - placeholder 
            if placeholder == target:
                 return placeholder
            if abs(difference) < abs(distance):
                 output = placeholder
                 distance = difference
            
            if placeholder < target:
                 left += 1
            else:
                 right -= 1
    return output


nums = [-1,2,1,-4] 
target = 1
output = threeSumClosest(nums, target)
print(f"output: {output}, target: {target}")


nums = [0,0,0] 
target = 1
output = threeSumClosest(nums, target)
print(f"output: {output}, target: {target}")


nums = [1,5,20, 0, 3, -5,-1, 10, 2, -5] 
target = 10
output = threeSumClosest(nums, target)
print(f"output: {output}, target: {target}")

nums = [1,1,0, -1, -2] 
target = 3
output = threeSumClosest(nums, target)
print(f"output: {output}, target: {target}")