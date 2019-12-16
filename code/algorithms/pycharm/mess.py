

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """

    for _ in range(k):
        nums = [nums[-1]] + nums[:-1]

    return nums

print(rotate([1,2,3,4,5,6,7], 3))