'''
如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/toeplitz-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def isToeplitzMatrix(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True


matrix = [[11,74,0,93],[40,11,74,7]]

print(isToeplitzMatrix(matrix))