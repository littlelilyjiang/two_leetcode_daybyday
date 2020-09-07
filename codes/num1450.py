'''
给你两个整数数组 startTime（开始时间）和 endTime（结束时间），并指定一个整数 queryTime 作为查询时间。

已知，第 i 名学生在 startTime[i] 时开始写作业并于 endTime[i] 时完成作业。

请返回在查询时间 queryTime 时正在做作业的学生人数。形式上，返回能够使 queryTime 处于区间 [startTime[i], endTime[i]]（含）的学生人数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def busyStudent(startTime,endTime,queryTime):
    sum = 0
    for i in range(0,len(startTime)):
        if queryTime >= startTime[i] and queryTime <= endTime[i]:
            sum = sum +1
    return sum

startTime = [1,1,1,1]
endTime = [1,3,2,4]
queryTime = 7

print(busyStudent(startTime,endTime,queryTime))