'''
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:
'''

'''
A&0xFFFFFFFF，B&0xFFFFFFFF将A,B转化为无符号数
'''

def convertInteger(A, B):
    x = A & 0xFFFFFFFF ^ B & 0xFFFFFFFF
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count


A = 826966453
B = -729934991
print(convertInteger(A,B))