
# Day 6 - LeetCode 349: Intersection of Two Arrays

def intersection(nums1, nums2):
    unique1 = set(nums1)
    unique2 = set(nums2)

    common = unique1.intersection(unique2)

    new_list = list(common)
    return new_list


# Test cases
print(intersection([1, 2, 2, 3], [2, 3, 3, 5]))
print(intersection([10, 20], [30, 40]))
print(intersection([1, 1, 2], [1, 1, 3]))
