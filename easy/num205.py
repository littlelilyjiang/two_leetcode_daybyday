'''
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def isIsomorphic(s, t):
    s_str = getString(s)
    t_str = getString(t)
    if s_str == t_str:
        return True
    return False

def getString(s):
    map = {}
    res = ''
    tmp = 0
    for i in s:
        if i in map:
            res = res+ str(map[i])
        else:
            tmp = tmp +1
            map[i] = tmp
            res = res + str(tmp)
    return res

print(isIsomorphic('aba','baa'))