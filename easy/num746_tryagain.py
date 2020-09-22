'''
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
def numPairsDivisibleBy60(time):
    res = 0
    map = {}
    for i in range(0,len(time)):
        if !map[i % 60] :
            map[i % 60] = i
    return res


time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time))
'''