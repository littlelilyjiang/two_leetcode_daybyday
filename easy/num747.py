'''
在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def dominantIndex(nums):
    max_num = max(nums)
    index = nums.index(max_num)
    for i in nums:
        if max_num < 2*i and max_num!=i:
            return -1
    return index

nums = [3, 6,6, 1, 0]
print(dominantIndex(nums))