'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
'''

def replaceSpace(s):
    return s.replace(' ','%20')


s = "We are happy."
print(replaceSpace(s))