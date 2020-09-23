'''
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
'''

def shortestToChar(S, C):
    res =[]
    index=[]
    for i in range(0,len(C)):
        if C[i] == S:
            index.append(i)

    for t in range(0,len(C)):
        tmp = abs(t - index[0])
        for i in index:
            if abs(i-t) < tmp:
                tmp=abs(i-t)
        res.append(tmp)
    return res

S = "loveleetcode"
C = 'e'

print(shortestToChar(C,S))