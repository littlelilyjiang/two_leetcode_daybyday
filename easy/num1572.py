'''
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
'''

def diagonalSum(mat):
    length = len(mat)
    res = 0
    for i in range(0,length):
        if length%2 != 0 and int(length/2) == i:
            # 如果是奇数行且在正中的话
            res = res + mat[i][i]
        else:
            res = res + mat[i][i]+mat[i][-1-i]
    return res

mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]

print(diagonalSum(mat))