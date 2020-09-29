'''
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？
'''

def missingNumber(nums):
    max_num = len(nums)+1
    for i in range(0,max_num+1):
        if i not in nums:
            return i



nums=[9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))