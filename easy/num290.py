'''
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def wordPattern(pattern, s):
    s_list = s.split(' ')
    i_list = list(pattern)
    if len(s_list) != len(i_list):
        return  False
    res_map_1 = {}
    res_map_2 ={}
    for i in range(len(i_list)):
        if i_list[i] in res_map_1.keys():
            if res_map_1[i_list[i]] != s_list[i]:
                return False
        if s_list[i] in res_map_2.keys():
            if res_map_2[s_list[i]] != i_list[i]:
                return False
        else:
            res_map_1[i_list[i]] = s_list[i]
            res_map_2[s_list[i]] = i_list[i]
    return True

pattern='aaa'
s ='aa aa aa aa'
print(wordPattern(pattern,s))