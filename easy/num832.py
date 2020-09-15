'''
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flipping-an-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



def flipAndInvertImage(A):
    res = []
    for j in A:
        j.reverse()
        tmp = str(j)
        new_tmp = tmp.replace('0','2').replace('1','0').replace('2','1')
        res.append(eval(new_tmp))
    return res

A= [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(A))