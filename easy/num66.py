'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def plusOne(digits):
    tmp_str=''
    for i in digits:
        tmp_str = tmp_str+str(i)
    num = int(tmp_str)+1
    tmp = str(num)
    res=[]
    for i in tmp:
        res.append(int(i))
    return res

digits=[1,2,3]
print(plusOne(digits))