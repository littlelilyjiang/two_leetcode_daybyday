'''
给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。

「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def findTheDistanceValue(arr1, arr2, d):
    res = 0
    for i in arr1:
        for j in arr2:
            if abs(i-j) <= d:
                res = res-1
                break
        res = res+1
    return res

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3

print(findTheDistanceValue(arr1,arr2,d))
