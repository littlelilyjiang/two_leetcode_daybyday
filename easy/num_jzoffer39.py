'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。



你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
def majorityElement(nums):
    numset = set(nums)
    for i in numset:
        count = nums.count(i)
        if count > int(len(nums)/2):
            return i

nums=[1, 2, 3, 2, 2, 2, 5, 4, 2]
print(majorityElement(nums))
