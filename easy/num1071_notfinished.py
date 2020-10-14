'''
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def gcdOfStrings(str1, str2):
    tmp = ''
    if len(str1) < len(str2):
        for i in str1:
            tmp = tmp +i
            if tmp*int(len(str1)/len(tmp))== str1 and tmp*int(len(str2)/len(tmp))== str2:
                return tmp
        return ''
    else:
        for i in str2:
            tmp = tmp +i
            if tmp*int(len(str1)/len(tmp))== str1 and tmp*int(len(str2)/len(tmp))== str2:
                return tmp
        return ''


str1 = "ABABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1,str2))