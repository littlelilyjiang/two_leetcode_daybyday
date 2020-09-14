'''
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。

请你统计并返回 grid 中 负数 的数目。
'''

def countNegatives(grid):
    sum = 0
    for i in grid:
        len_i = len(i)
        for j in range(0,len_i):
            if i[j] < 0 :
                sum = sum + len_i-j
                break
    return sum

grid = [[1,-1],[-1,-1]]
print(countNegatives(grid))