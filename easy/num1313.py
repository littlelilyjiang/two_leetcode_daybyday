'''
给你一个以行程长度编码压缩的整数列表 nums 。

考虑每对相邻的两个元素 [freq, val] = [nums[2*i], nums[2*i+1]] （其中 i >= 0 ），每一对都表示解压后子列表中有 freq 个值为 val 的元素，你需要从左到右连接所有子列表以生成解压后的列表。

请你返回解压后的列表。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decompress-run-length-encoded-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def decompressRLElist(nums):
    res = []
    for i in range(0,len(nums)):
        if i%2 == 0:
            #偶数位才做处理
            for j in range(0,nums[i]):
                res.append(nums[i+1])
    return res

nums = [1,1,2,3]
print(decompressRLElist(nums))

'''
这个解法的时间复杂度很高
n^2的时间复杂度
'''

