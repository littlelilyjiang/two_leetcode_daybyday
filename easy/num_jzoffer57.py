'''
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

'''

def twoSum(nums, target):
    res = {}
    for j in nums:
        if j in res:
            return [j,res[j]]
        else:
            res[target-j] = j


nums = [10,26,30,31,47,60]
target = 40
print(twoSum(nums,target))