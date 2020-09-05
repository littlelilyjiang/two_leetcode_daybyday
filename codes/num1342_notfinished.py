'''

给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。


'''

def step(num,times):
    while(num != 0):
        times = times + 1
        # 下面进行递归
        if num % 2 == 1:
            num = num - 1
        else:
            num = num / 2
        step(num, times)
    return times


def numberOfSteps (num):
    return step(num,0)

print(numberOfSteps(14))

'''
不带参数的递归
还需要多思考
'''