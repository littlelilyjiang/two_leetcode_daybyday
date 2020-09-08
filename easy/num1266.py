'''
平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。

你可以按照下面的规则在平面上移动：

每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
必须按照数组中出现的顺序来访问这些点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-time-visiting-all-points
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def minTimeToVisitAllPoints(points):
    minTime = 0
    for i in range(0,len(points)-1):
        # 因为走斜线是最近的,先找出横着或者竖着最少的数，然后按照这个数字来斜着走，最后的都直着走就可以了
        if abs(points[i+1][0]-points[i][0]) > abs(points[i+1][1]-points[i][1]):
            # 如果纵坐标更小，那么就先斜着走纵坐标那么远
            time = abs(points[i+1][0]-points[i][0])
        else:
            #否则横坐标更小或者二者一样小的时候  就先斜着走横坐标那么远
            time = abs(points[i + 1][1] - points[i][1] )
        minTime = minTime + time
    return minTime

points = [[3,2],[-2,2]]
print(minTimeToVisitAllPoints(points))

'''
最开始以为要先遍历找出 最近的两点 然后慢慢找到每次最近的点来走

后来才发现其实每次只要走的是最短的路线 相对于整个结果来说就是最短的路线了
最后通过推算发现 这种走法相当于要用的最大时间就是横纵坐标的最大值
所以就用python的内置函数直接来求
'''