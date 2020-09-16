'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

'''


def reverseWords(s):
    if ' ' not in s:
        return ''.join(reversed(s))
    new_arrs = s.split(' ')
    res = ''
    for arr in new_arrs:
        res = res + ''.join(reversed(arr)) +' '
    return res[0:len(res)-1]


s ="Let's take LeetCode contest"
print(reverseWords(s))