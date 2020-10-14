'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def twoSum(numbers, target):
    res = []
    new_set = set(numbers)
    for i in new_set:
        if target - i in numbers:
            if target - i != i:
                res.append(numbers.index(i) + 1)
                res.append(numbers.index(target - i) + 1)
            else:
                res.append(numbers.index(i) + 1)
                res.append(numbers.index(i, numbers.index(i) + 1, len(numbers)) + 1)
            res.sort()
            return res
numbers = [-1,0]
target = -1
print(twoSum(numbers,target))