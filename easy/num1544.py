'''
给你一个由大小写英文字母组成的字符串 s 。

一个整理好的字符串中，两个相邻字符 s[i] 和 s[i+1]，其中 0<= i <= s.length-2 ，要满足如下条件:

若 s[i] 是小写字符，则 s[i+1] 不可以是相同的大写字符。
若 s[i] 是大写字符，则 s[i+1] 不可以是相同的小写字符。
请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 两个相邻 字符并删除，直到字符串整理好为止。

请返回整理好的 字符串 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。

注意：空字符串也属于整理好的字符串，尽管其中没有任何字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/make-the-string-great
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def makeGood(s):
    if len(s) == 1:
        return s

    for i in range(len(s) - 1):
        if s[i] != s[i + 1] and s[i].upper() == s[i + 1].upper():
            s = s[:i] + s[i + 1:]
            s = s[:i] + s[i + 1:]
            return makeGood(s)
    return s

s = "leEeetcode"

print(makeGood(s))