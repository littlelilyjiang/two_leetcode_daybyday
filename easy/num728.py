'''
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/self-dividing-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def selfDividingNumbers(left, right):
    res = []
    for i in range(left,right+1):
        tmp = 0
        for t in str(i):
            if int(t) == 0:
                break
            elif i % int(t) == 0:
                tmp = tmp+1
        if tmp == len(str(i)):
            res.append(i)
    return res


left=1
right=22
print(selfDividingNumbers(left,right))