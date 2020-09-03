'''
实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

'''
去掉链表中的一个数据，就相当于用他的下一个数据来替代它
所以用下一个的值来取代这个的值 用下一个的指针来取代这一个的指针 那么这个链表的这个数据就被去掉了
'''