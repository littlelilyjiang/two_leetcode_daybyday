'''
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
'''
def subtractProductAndSum(n):
    sum = 0
    ji = 1
    for i in str(n):
        sum = sum +int(i)
        ji = ji*int(i)
    return ji-sum

print(subtractProductAndSum(4421))

'''
把这个数字遍历一遍 按照数学方法求出来对应的结果
'''