from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    freq = 0
    l = len(nums)
    for i in range(l):
        if nums[i] == x :
            freq = freq+1
    return freq




# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
