res_list = []
def binaryTreePaths(root):
    if root.left == None and root.right == None:
        #这个时候走到了叶子节点 可以开始返回了
        return root
    else:
        binaryTreePaths(root)