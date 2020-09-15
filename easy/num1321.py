'''
给你一个仅由数字 6 和 9 组成的正整数 num。

你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。

请返回你可以得到的最大数字。
'''

def maximum69Number (num):
    num = str(num)
    for i in range(0,len(num)):
        if num[-i] == '6':
            res = num.replace('6','9',1)
            return res
    return num

num=9996
print(maximum69Number(num))