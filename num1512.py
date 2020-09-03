'''
题目：
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-good-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

def numIdenticalPairs(nums):
    num_index_map ={}
    index = 0
    for num in nums:
        indexs = []
        if num in num_index_map.keys():
            # 如果这个num在num_index_map里面的话 说明他出现过
            indexs = num_index_map.get(num)
            indexs.append(index)
            num_index_map[num] = indexs
        else:
            indexs.append(index)
            num_index_map[num] = indexs
        index = index+1

    # 现在这个map里面存了所有的数字和数字对应的坐标了
    print(num_index_map)
    res = 0
    for num_index in num_index_map:
        if len(num_index_map[num_index]) > 1:
            res = res+ (len(num_index_map[num_index])-1)*len(num_index_map[num_index])/2
    return int(res)

nums = [1,2,3,1,1,3]

print(numIdenticalPairs(nums))
'''
解题思路：
把这个数组通过一个map记录下来
map里面的key是这个数组里的每一个数字，value是一个数组 数组里面是这个数字出现的位置
最后遍历一次这个map，这个map中的value大于1的 通过一个等差数列来求和就可以了


PS：这个时间复杂度很高 应该在第一次遍历的时候 可以通过一种巧妙的方式直接计算出最终的结果
但是现在的程度不管怎么思考都会感觉在第一次遍历就求结果会有漏掉的情况 希望以后回过头来看 能想到时间复杂度更低的方法
'''