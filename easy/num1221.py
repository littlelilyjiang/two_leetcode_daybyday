'''
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-a-string-in-balanced-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def balancedStringSplit(s):
    tmp_l = 0
    tmp_r = 0
    res = []
    for i in s:
        if i == 'L':
            tmp_l = tmp_l +1
            if tmp_l == tmp_r:
              res.append(tmp_l)
        if i == 'R':
            tmp_r = tmp_r + 1
            if tmp_l == tmp_r:
                res.append(tmp_l)
    return len(set(res))

s = "RLLLLRRRLR"
print(balancedStringSplit(s))