'''
给定两个数组，编写一个函数来计算它们的交集。


'''
def intersection(nums1, nums2):
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
            nums2.remove(i)
    return set(res)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))