'''
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def relativeSortArray(arr1, arr2):
    res = []
    tmp_arr1 = arr1[:]
    left = []
    for j in arr1:
        if j not in arr2:
            left.append(j)
    left.sort(reverse=False)
    for i in arr2:
        if i in arr1:
            for t in range(0, tmp_arr1.count(i)):
                res.append(i)
    return res + left


arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
arr2 = [2, 42, 38, 0, 43, 21]
print(relativeSortArray(arr1, arr2))
