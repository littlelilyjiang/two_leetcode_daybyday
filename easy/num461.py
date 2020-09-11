'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def hammingDistance(x, y):
    s_x = str(bin(x)).replace('0b','')
    s_y = str(bin(y)).replace('0b', '')
    res = 0
    min_len = min(len(s_x),len(s_y))
    for i in range(1,min_len+1):
        if s_x[-i] != s_y[-i]:
            res = res + 1
    if len(s_x) > min_len:
        #如果x的位数比较多，那么就取x中1的数量
        return res + s_x[0:len(s_x)-min_len].count('1')
    elif len(s_y) > min_len:
        #如果x的位数比较多，那么就取x中1的数量
        return res + s_y[0:len(s_y)-min_len].count('1')
    return res



x=93
y=73
print(hammingDistance(x,y))