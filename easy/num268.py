'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
'''

def missingNumber(nums):
    for i in range(len(nums)+1):
        if i  not in nums:
            return i