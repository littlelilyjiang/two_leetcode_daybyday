'''
给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def kidsWithCandies(candies, extraCandies):
    max = 0
    for i in candies:
        if i > max:
            max = i
    #这里选出了最大的max数字是什么
    res = []
    for i in candies:
        if i+extraCandies >= max:
            # 这里因为要求的输出是 [true,true,false]这样的 没有引号 所以采用这种方式来输出true和false
            res.append(1==1)
        else:
            res.append(1!=1)
    return res

candies = [12,1,12]
extraCandies = 10
print(kidsWithCandies(candies,extraCandies))

'''
解题思路：
遍历一次先选出最大的max的那个数字（python感觉应该有方法可以直接求到数组的最大数字）
第二次遍历 数字都+extra 如果加上之后和max一样大或者超过max的大小，则输出true
因为结果想要的是[true,true,false]这样的结果
所以append的时候  是1==1 这种形式的  但是在编译器 这个输出的True 在leetcode客户端输出的是true

'''