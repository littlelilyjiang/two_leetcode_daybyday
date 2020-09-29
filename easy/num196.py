'''
编写一个 SQL 查询，来删除 Person 表中所有重复的电子邮箱，重复的邮箱里只保留 Id 最小 的那个。
'''

'''
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

作者：LeetCode
链接：https://leetcode-cn.com/problems/delete-duplicate-emails/solution/shan-chu-zhong-fu-de-dian-zi-you-xiang-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''