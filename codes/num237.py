'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

 

现有一个链表 -- head = [4,5,1,9]，它可以表示为:



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

head =[]

def deleteNode(node):
    for i in head:
        if i.val == node:
            i.val = i.next.val
            i.next = i.next.next
    return head


'''
这道题太奇怪了  传入的是一个参数啊
我回过头来在看了一遍题目 还是不知道怎么样才能通过检查
'''
