'''
有一个courses 表 ，有: student (学生) 和 class (课程)。

请列出所有超过或等于5名学生的课。

例如，表：

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
应该输出:

+---------+
| class   |
+---------+
| Math    |
+---------+

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/classes-more-than-5-students
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Write your MySQL query statement below
# select class from(select count(class) as count_class,class from (
#     select count(class) as class_count,class from courses group by class,student
#     ) a group by a.class ) b where b.count_class>=5