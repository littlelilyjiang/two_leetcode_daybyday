
'''
给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。

更正式地，检查是否存在两个下标 i 和 j 满足：

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-n-and-its-double-exist
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def checkIfExist(arr):
    for i in range(len(arr)):
        if 2* arr[i] in arr and i != arr.index(2*arr[i]):
            return True
    return False


arr=[0]
print(checkIfExist(arr))