"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""



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


