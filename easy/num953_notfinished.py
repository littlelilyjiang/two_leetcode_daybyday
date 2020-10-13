'''
种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verifying-an-alien-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def isAlienSorted(words, order):
    flag = True
    for i in range(len(words)-1):
        min_num = min(len(words[i]), len(words[i + 1]))
        if words[i+1] in words[i] and words[i+1] != words[i]:
            return False
        for t in range(min_num):
            word_1= words[i][t]
            word_2= words[i+1][t]
            if order.index(word_1)> order.index(word_2):
                return False
            elif order.index(word_1)< order.index(word_2):
                return True
    return flag


words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
order = "zkgwaverfimqxbnctdplsjyohu"
# order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words,order))