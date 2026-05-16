"""
Given a list of integers and a target, return the indices
of the two numbers that add up to the target.

nums = [2, 7, 11, 15], target = 9
→ Output: [0, 1]
"""

def find_sum(nums: list[int], target: int):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    


nums = [2, 7, 11, 15]
target = 9
print(find_sum(nums, target))

nums = [3, 7, 3, 15]
target = 6
print(find_sum(nums, target))