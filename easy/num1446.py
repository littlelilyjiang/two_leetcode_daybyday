'''
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串的能量。


'''

def maxPower(s):
    if len(s) < 2:
        return len(s)
    tmp = 1
    max=1
    for i in range(len(s)-1) :
        if s[i] == s[i+1]:
            tmp = tmp +1
            if tmp > max:
                max = tmp
        else:
            tmp = 1
    return max

s = "j"
print(maxPower(s))