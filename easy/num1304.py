'''
给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。
'''

def sumZero(n):
    if n == 1:
        return [0]
    res =[]
    for i in range(0,int(n/2)):
        res.append(i+1)
        res.append(-i-1)
    if n % 2 != 0:
        res.append(0)
    return res

print(sumZero(5))

