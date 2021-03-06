'''
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-the-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def shuffle(nums, n):
    res = []
    if len(nums) >= 2:
        num_1 = nums[0:n]
        num_2 = nums[n:2*n]
        index = 0
        for i in num_1:
            res.append(i)
            res.append(num_2[index])
            index = index+1
        return res
    else:
        return res

nums = [1,1,2,2]
n = 2
print(shuffle(nums,n))

#解题思路：主要的来说 就是用到了python的切片来做