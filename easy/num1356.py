'''
给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。

如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。

请你返回排序后的数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def sortByBits(arr):
    map ={}
    res =[]
    for i in arr:
        tmp = str(bin(i).replace('0b','')).count('1')
        if tmp not in map.keys():
            map[tmp] = [i]
        else:
            tmp_list = map[tmp]
            tmp_list.append(i)
            tmp_list.sort()
            map[tmp] = tmp_list
    for item in map.values():
        res = res+item
    return res

arr=[2,3,5,7,11,13,17,19]
print(sortByBits(arr))