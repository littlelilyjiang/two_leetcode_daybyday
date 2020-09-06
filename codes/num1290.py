'''
给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def getDecimalValue(head):
    head_list = []
    head_list.append(head.val)
    while (head.next != None):
        head_list.append(head.next.val)
        head = head.next
    # 把所有的head的值放到一个list中去 然后通过这个list遍历来求十进制
    sum = 0
    for i in range(0, len(head_list)):
        t = 2 ** i
        sum = sum + head_list[len(head_list) - i - 1] * t
    return sum

'''
新存的list其实也还是链表的顺序，所以再计算的时候 不要把顺序搞反了
'''