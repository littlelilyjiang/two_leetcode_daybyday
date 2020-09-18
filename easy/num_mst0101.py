'''
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
'''


def isUnique(astr):
    for i in astr:
        if astr.count(i) > 1:
            return False
    return True


print(isUnique("leetcode"))