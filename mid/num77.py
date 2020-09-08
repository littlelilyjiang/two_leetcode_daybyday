'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
'''
def combine(n,k):
    res = []
    each_res = []
    for i in range(0,k):
        if i in range(1,n+1):
            each_res
    return res

n=4
k=1
print(combine(n,k))


'''
用递归来做，递归到最后只存在一位数的时候 那么就只需要遍历n次，然后不需要这个数本体参与
'''