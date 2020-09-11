'''
给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。

完成所有替换操作后，请你返回这个数组。
'''

def replaceElements(arr):
    if len(arr) == 1:
        return  arr
    if arr[0] < max(arr[1:len(arr)]):
        arr.remove(arr[0])
    for i in range(0,len(arr)-1):
        arr[i] = max(arr[i:len(arr)])
    arr.append(-1)
    return arr

arr =  [400]
print(replaceElements(arr))