def minCount(coins):
    sum = 0
    for i in coins:
        if i%2 == 1:
            sum = sum + int(i/2) +1
        else:
            sum = sum +i/2
    return int(sum)

coins =[2,3,10]
print(minCount(coins))