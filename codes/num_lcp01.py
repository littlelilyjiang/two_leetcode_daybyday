'''

小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？



输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。
'''

def game(guess, answer):
    res = 0
    for i in range(0,3):
        if guess[i] == answer[i]:
            res =res+1
    return res

guess = [1,2,3]
answer = [1,2,1]
print(game(guess, answer))

'''
第一次想的是如果求两个数组的交集有多少个 但是后来发现还和数字的出场顺序有关系
所以能想到的办法就是一个一个拿出来比 因为刚好也只有3个
'''