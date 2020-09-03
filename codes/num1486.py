'''
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xor-operation-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def xorOperation(n, start):
    res = 0
    res = res^start
    for i in range(1,n):
        start = start + 2
        res = res^start
    return res


print(xorOperation(10,5))

'''
pyhton求异或，可以使用^直接来求 所以让这道题简化了
其实最开始的想法是从+2入手 每次+2 那么就等于每次加了一个进位 以此为突破口来做
'''