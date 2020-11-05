'''
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。
'''
def isUgly(num):
    if num == 0:
        return False
    while(num != 1):
        if num%2 == 0:
            num = num/2
            continue
        if num%3 == 0:
            num = num/3
            continue
        if num%5 == 0:
            num = num/5
            continue
        if num%2 != 0 and num%3 != 0 and num%5 != 0:
            return False
    return True

print(isUgly(14))