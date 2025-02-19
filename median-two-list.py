
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    max_size = len(nums1) + len(nums2)
    merged = []
    while len(merged) <= max_size:
        if len(nums1) == 0 and len(nums2) > 0:
            merged += nums2
            break
        if len(nums2) == 0 and len(nums1) > 0:
            merged += nums1
            break

        if nums1[0] < nums2[0]:
            merged.append(nums1.pop(0))
        else:
            merged.append(nums2.pop(0))
            
    mid = len(merged)//2
    if len(merged) % 2 == 1:
        return float(merged[mid])
    else:
        return (merged[mid] + merged[mid - 1]) / 2




n1 = [1, 3]
n2 = [2]

o = findMedianSortedArrays(n1, n2)
expected = 2.0
print(f"got: {o}, is correct: {o == expected}")


n1 = [1, 2]
n2 = [3, 4]
o = findMedianSortedArrays(n1, n2)
expected = 2.5
print(f"got: {o}, is correct: {o == expected}")


