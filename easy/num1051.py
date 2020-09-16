'''
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。

请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。

注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/height-checker
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



def heightChecker(heights):
    o_heights = heights
    heights = sorted(heights)
    count = 0
    for i in range(len(o_heights)):
        if o_heights[i] != heights[i]:
            count += 1
    return count

heights=[5,1,2,3,4]
print(heightChecker(heights))