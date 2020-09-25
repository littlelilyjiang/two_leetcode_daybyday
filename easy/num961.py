'''
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。
'''

def repeatedNTimes(A):
    for t in A:
        if A.count(t) == len(A)/2:
            return t