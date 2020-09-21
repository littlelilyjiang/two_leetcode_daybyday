'''
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
'''

def uniqueOccurrences(arr):
    res_map = {}
    for j in arr:
        count = arr.count(j)
        if count in res_map.keys() and res_map[count] != j:
            return False
        else:
            res_map[count] = j
    return True

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))