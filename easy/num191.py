'''
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
'''

def hammingWeight(n):
    return str(bin(n)).replace('0b','').count('1')

n=5
print(hammingWeight(n))