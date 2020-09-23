'''
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

'''

def addDigits(num):
    while(len(str(num)) > 1):
        res = 0
        for i in str(num):
            res = res + int(i)
        num =res
    return num

print(addDigits(38))
