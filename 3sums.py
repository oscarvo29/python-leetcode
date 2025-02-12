
def threeSum(nums: list[int]) -> list[list[int]]:
    """
        return as many lists, with size of 3 (triplets)
        containing unique numbers, which adds up to 0.
        else return an empty list
    """
    triplets = []
    index = 0
    sorted_nums = sorted(nums)
    counter = len(sorted_nums)
    triplets_set = set()

    while index < counter:
        left = index + 1
        point = sorted_nums[index]
        right = len(sorted_nums) -1
        
        while left < right:    
            sum = point + sorted_nums[left] + sorted_nums[right]

            if sum == 0:
                triplet = tuple([point, sorted_nums[left], sorted_nums[right]])
                if triplet not in triplets_set:
                    triplets_set.add(triplet)
                left += 1
                right -= 1
            elif sum < 0:
                left += 1 
            else:
                right -= 1
        index += 1

    for triplet in triplets_set:
        triplets.append(list(triplet))

    return triplets



n = [-1,0,1,2,-1,-4]
t = threeSum(n)
print(f"Expected: [[-1, 0, 1], [-1, -1, 2]]\nGot: {t}\n\n")

n = [0,1,1]
t = threeSum(n)
print(f"Expected: []\nGot: {t}\n\n")

n = [0,0,0]
t = threeSum(n)
print(f"Expected: [0, 0, 0]\nGot: {t}\n\n")

n = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
t = threeSum(n)
print(f"Expected: [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]\nGot: {t}\n\n")

n = [3,0,-2,-1,1,2]
t = threeSum(n)
print(f"Expected: [[-2,-1,3],[-2,0,2],[-1,0,1]]\nGot: {t}\n\n")

n = [3,-2,1,0]
t = threeSum(n)
print(f"Expected: []\nGot: {t}\n\n")


n = [2,4,1,0,-3,-1]
t = threeSum(n)
print(f"Expected: [[[-3,-1,4],[-3,1,2],[-1,0,1]]]\nGot: {t}\n\n")

# n = [8,5,12,3,-2,-13,-8,-9,-8,10,-10,-10,-14,-5,-1,-8,-7,-12,4,4,10,-8,0,-3,4,11,-9,-2,-7,-2,3,-14,-12,1,-4,-6,3,3,0,2,-9,-2,7,-8,0,14,-1,8,-13,10,-11,4,-13,-4,-14,-1,-8,-7,12,-8,6,0,-15,2,8,-4,11,-4,-15,-12,5,-9,1,-2,-10,-14,-11,4,1,13,-1,-3,3,-7,9,-4,7,8,4,4,8,-12,12,8,5,5,12,-7,9,4,-12,-1,2,5,4,7,-2,8,-12,-15,-1,2,-11]
# t = threeSum(n)
# print(f"Got: {t}\n\n")

n = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
t = threeSum(n)
print(f"Expected: [[-5,1,4],[-3,-1,4],[-3,0,3],[-2,-1,3],[-2,1,1],[-1,0,1],[0,0,0]]\nGot: {t}\n\n")




"""
    triplets = []
    index = 0
    sorted_nums = sorted(nums)
    counter = len(sorted_nums)
    

    while index < counter:
        if index > 0 and sorted_nums[index] == sorted_nums[index - 1]:
            index += 1
            continue
        left = index + 1
        point = sorted_nums[index]
        right = len(sorted_nums) -1
        
        while left < right:    
            sum = point + sorted_nums[left] + sorted_nums[right]

            if sorted_nums[left] == sorted_nums[left - 1]:
                left += 1
                continue

            if right < counter - 2 and sorted_nums[right] == sorted_nums[right +1]:
                right -= 1
                continue

            if sum == 0:
                triplets.append([point, sorted_nums[left], sorted_nums[right]])
                left += 1
                right -= 1
            elif sum < 0:
                left += 1 
            else:
                right -= 1
        index += 1

    return triplets

"""
