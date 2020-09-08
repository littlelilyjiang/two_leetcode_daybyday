'''

编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。
'''
# select Email from (select count(*) as nums,Email from Person group by Email ) a where a.nums>1
