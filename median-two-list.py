


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    return

def merge(l1: list[int], l2: list[int], output = []) -> list[int]:
    if len(l1) == 0 and len(l2) == 0:
        return output
    


l = [1, 4, 2, 5, 3, 6, 9, 7]

def sorting(l1: list[int], output: list[int] = []) -> list[int]:
    left = 0
    right = len(l1) - 1
    
    if len(l1) == 1:
        print(l1)
        return l1[0]
    
    pivot_point = l1[-1]
    for item in l1:
        if item <= pivot_point:
            left.append(item)
        else:
            right.append(item)

    subarr_1 = sorting(left)
    subarr_2 = sorting(right)
    print(f"subarr 1: {subarr_1}")
    print(f"subarr 1: {subarr_2}")

# sorting(l)

for i in 121:
    print(i)

# n1 = [1, 3]
# n2 = [2]

# print(len(n2) // 2)


# findMedianSortedArrays(n1, n2)

# n1 = [1, 2]
# n2 = [3, 4]

# findMedianSortedArrays(n1, n2)


