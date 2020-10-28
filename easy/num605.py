'''
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def canPlaceFlowers(flowerbed, n):
    tmp = [0] + flowerbed + [0]
    for i in range(1, len(tmp) - 1):
        if tmp[i - 1] == 0 and tmp[i] == 0 and tmp[i + 1] == 0:
            tmp[i] = 1  # 在 i 处栽上花
            n -= 1
    return n <= 0  # n 小于等于 0 ，表示可以栽完花





flowerbed = [1,0,1,0,0,1,0]
n = 2
print(canPlaceFlowers(flowerbed,n))