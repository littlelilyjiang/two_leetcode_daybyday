'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def containsNearbyDuplicate(nums, k):
    # 用字典查找
    # 元素存入key,索引存入value
    dic = {}
    # 遍历nums
    for i in range(len(nums)):
        # 如果有相同元素，匹配成功
        if nums[i] in dic:
            # 判断索引差
            # 小于k符合条件
            if i - dic[nums[i]] <= k:
                return True
            # 不小于k则将索引更新为更接近未来匹配的那一个
            else:
                dic[nums[i]] = i
        else:
            dic[nums[i]] = i

    return False


nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums,k))