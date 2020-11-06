'''
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True
    x1, y1 = coordinates[0][0], coordinates[0][1]
    x2, y2 = coordinates[1][0], coordinates[1][1]
    for i in range(2, len(coordinates)):
        x3, y3 = coordinates[i][0], coordinates[i][1]
        if (y3 - y2) * (x2 - x1) != (y2 - y1) * (x3 - x2):
            return False
    return True

coordinates = [[2,1],[4,2],[6,3]]
print(checkStraightLine(coordinates))