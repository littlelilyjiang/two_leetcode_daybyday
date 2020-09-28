'''
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def nextGreaterElement(nums1, nums2):
    res = []
    for i in nums1:
        for j in range(nums2.index(i)+1,len(nums2)):
            if nums2[j] > i:
                res.append(nums2[j])
                break
        if len(res) <= nums1.index(i):
            res.append(-1)
    return res



nums1 = [4,1,2]
nums2 = [1,3,2,4]
print(nextGreaterElement(nums1,nums2))
