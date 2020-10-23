'''
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def findLengthOfLCIS(nums):
    lenth = len(nums)
    if lenth == 0:
        return 0
    tmp = nums[0]
    res =1
    tmp_res = 0
    for i in nums[1:lenth]:
        if i <= tmp :
            if tmp_res < res:
                tmp_res = res
            res = 1
            tmp = i
            continue
        res = res + 1
        tmp = i
    return max(tmp_res,res)

nums = [1,3,5,4,2,3,4,5]
print(findLengthOfLCIS(nums))