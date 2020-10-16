'''
在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足属性 1 和属性 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-town-judge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def findJudge(N, trust):
    if N==1 and len(trust) == 0:
        return 1
    peoel_list = []
    # 这里面保存相信别人的人的序号
    tmp=[]
    # 这里面key是每个出现的人，value是相信它的人的list
    tmp_map_2={}
    for i in trust:
        tmp_list=[]
        tmp.append(i[0])
        peoel_list.append(i[0])
        peoel_list.append(i[1])
        if i[1] in tmp_map_2.keys():
            tmp_list = tmp_map_2[i[1]]
            tmp_list.append(i[0])
            tmp_map_2[i[1]]=tmp_list
        else:
            tmp_list.append(i[0])
            tmp_map_2[i[1]] = tmp_list
    res = []
    for k,v in tmp_map_2.items():
        v_set = set(v)
        if len(v_set) == N-1 and k not in tmp:
            res.append(k)
            if len(res) > 1:
                return -1
    if len(res) == 1:
        return res[0]
    return -1

    print('11111')

N = 1
trust = []
print(findJudge(N,trust))



