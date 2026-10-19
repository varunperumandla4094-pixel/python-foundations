
# Day 6 - LeetCode 217: Contains Duplicate

def contains_duplicate(nums):
    unique_nums = set(nums)

    if len(nums) != len(unique_nums):
        return True
    else:
        return False


# Test cases
print(contains_duplicate([10, 20, 30, 20]))
print(contains_duplicate([5, 6, 7, 8]))
print(contains_duplicate([]))
