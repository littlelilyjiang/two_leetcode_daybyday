'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


'''

def firstUniqChar(s):
    for i in range(len(s)) :
        if s.count(s[i]) == 1:
            return i
    return -1
s = "loveleetcode"
print(firstUniqChar(s))
