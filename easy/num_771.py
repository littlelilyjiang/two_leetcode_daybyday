'''
给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jewels-and-stones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def numJewelsInStones(J, S):
    sum =0
    for j in J:
        sum = sum + S.count(j)
    return sum

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J, S))

'''
解题思路就是
遍历 再求和
'''