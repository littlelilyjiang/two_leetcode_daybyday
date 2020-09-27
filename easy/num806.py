'''
我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。

现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-lines-to-write-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def numberOfLines(widths, S):
    if len(S) == 0:
        return [0,0]
    map = {}
    init = 97
    for i in widths:
        map[chr(init)]=i
        init =init+1
    sum = 0
    res1 = 1
    for i in S[0:len(S)]:
        sum =sum+map[i]
        if sum>100:
            res1 = res1 +1
            sum = map[i]
    return [res1,sum]



widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"


print(numberOfLines(widths,S))

