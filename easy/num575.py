'''
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-candies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def distributeCandies(candies):
    candies_set = set(candies)
    l1 = len(candies_set)
    l2 = len(candies)/2

    if l1 > l2:
        candies_set = list(candies_set)[0:int(l2)]
        return len(set(candies_set))
    return l1

candies = [1,1,2,3]
print(distributeCandies(candies))

