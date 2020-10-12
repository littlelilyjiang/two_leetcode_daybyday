'''
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。


'''


def findKthPositive(arr, k):
    res = []
    tmp = max(len(arr),max(arr))
    for i in range(1,tmp):
        if i not in arr:
           res.append(i)

    if k <= len(res):
        return res[k-1]
    else:
        return len(arr)+k

arr = [2]
k = 1
print(findKthPositive(arr,k))
