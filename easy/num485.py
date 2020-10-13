'''
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:
'''

def findMaxConsecutiveOnes(nums):
    str_num = str(nums)
    new_list=str_num.split('0')
    tmp = 0
    for i in new_list:
        if i.count('1')> tmp:
            tmp = i.count('1')
    return tmp

nums=[1,1,0,1,1,1,0]
print(findMaxConsecutiveOnes(nums))