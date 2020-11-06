'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
'''

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    for i in range(len(nums)):
        if nums[i]>target:
            return i
    return len(nums)

nums=[1,3,5,6]
target=0
print(searchInsert(nums,target))