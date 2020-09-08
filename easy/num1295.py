'''
给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
'''

def findNumbers(nums):
    sum = 0
    for num in nums:
        if len(str(num))%2 == 0:
            sum =sum+1
    return sum

nums = [12,345,2,6,7896]
print(findNumbers(nums))