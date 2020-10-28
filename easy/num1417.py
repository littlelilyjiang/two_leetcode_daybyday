'''
给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。

请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reformat-the-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def reformat(s):
    res_num = []
    res_dc=[]
    res=''
    for i in s:
        if ord(i)>=97 and ord(i)< 123:
            res_dc.append(i)
        else:
            res_num.append(i)
    if abs(len(res_dc)-len(res_num)) > 1:
        return ''
    else:
        if len(res_dc) > len(res_num):
            for t in range(len(res_num)):
                res = res + res_num[t]
                res = res + res_dc[t]
            res = res + res_num[-1]
            return res
        elif len(res_dc) < len(res_num):
            for t in range(len(res_dc)):
                res = res + res_dc[t]
                res = res + res_num[t]
            res = res + res_dc[-1]
            return res
        else:
            for t in range(len(res_dc)):
                res = res + res_dc[t]
                res = res + res_num[t]
            return res

s = "leetcode"
print(reformat(s))