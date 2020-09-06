'''
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def smallerNumbersThanCurrent(nums):
    res = []
    for i in range(0, len(nums)):
        num = 0
        for j in nums:
            if nums[i] > j:
                num = num+1
        res.append(num)
    return res

nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))

'''
这样做的时间复杂度是n^2
但是应该有什么办法可以做到n的复杂度
'''