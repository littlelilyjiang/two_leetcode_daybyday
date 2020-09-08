'''
给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/destination-city
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#因为只求终点，所以不要关系list[0]的去向，关注list[1]是否被抵消

def destCity (paths):
    if len(paths) == 0:
        return []
    start = []
    end =[]
    for i in paths:
        if i[0] in end:
            end.remove(i[0])
        else:
            start.append(i[0])
        if i[1] in start:
            start.remove(i[1])
        else:
            end.append(i[1])
    return end[0]

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))

