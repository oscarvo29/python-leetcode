
def maxArea(height: list[int]) -> int:
    area = 0
    left = 0
    right = len(height) - 1
    lowest_tower = 0

    while left < right:
        t1 = height[left]
        t2 = height[right]
        lowest_tower = t1 if t1 < t2 else t2
        current_area = lowest_tower * (right - left)
        if area <  current_area:
            area = current_area

        if t1 < t2:
            left += 1
        else:
            right -= 1

    return area


height = [1,8,6,2,5,4,8,3,7]
maxArea(height)

height = [1,1]
maxArea(height)

height = [1, 132, 1, 5, 7, 1, 5, 134523, 2, 4, 1, 6, 13, 5, 70]
maxArea(height)



"""

print(f"left: {left_side}")
    print(f"right: {right_side}")
    print(f"pivot point: {pivot_point}")
    print(f"item at pivot point: {height[pivot_point]}")
    print(f"height lsit: {height}")
    print(f"height len: {len(height)}")
    print(f"height tuple: {tuple(height)}")


"""