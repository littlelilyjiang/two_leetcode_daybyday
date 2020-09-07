'''
给你一个字符串 s 和一个 长度相同 的整数数组 indices 。

请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。

返回重新排列后的字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def restoreString(s,indices):
    tmp_map = {}
    res = ''
    for i in range(0,len(indices)):
        tmp_map[indices[i]] = s[i]
    arr_lis = list(tmp_map.keys())
    arr_lis.sort()
    for j in arr_lis:
        res = res+str(tmp_map.get(j))
    return res

s = "aiohn"
indices = [3,1,4,2,0]
print(restoreString(s,indices))

'''
使用了一个map来存位置和字母的关系
然后把位置进行一次排序 依次取出这个位置的字母拼成最后需要的单词
时间复杂度 o(2n)
'''