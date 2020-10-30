'''
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diving-board-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def divingBoard(shorter, longer, k):
    if not k:
        return []
    # 这个if里面的判断 可以节约很多时间
    if shorter == longer:
        return [shorter * k]
    res = [0] * (k + 1)
    for i in range(k + 1):
        res[i] = shorter * (k - i) + longer * i
    return res



shorter = 2
longer = 1118596
k = 979
print(divingBoard(shorter,longer,k))