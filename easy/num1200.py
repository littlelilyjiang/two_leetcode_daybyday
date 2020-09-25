'''
给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
'''

# 先sort 再两两相减 得到最小 这样来算

def minimumAbsDifference(arr):
    arr.sort()

    small = []
    smallkey = 99999

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < smallkey:
            smallkey = arr[i] - arr[i - 1]
            small = [[arr[i - 1], arr[i]]]
        elif arr[i] - arr[i - 1] == smallkey:
            small.append([arr[i - 1], arr[i]])

    return small


arr = [4,2,1,3]
print(minimumAbsDifference(arr))