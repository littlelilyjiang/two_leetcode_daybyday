'''
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。


'''

def countOdds(low, high):
    if low%2 == 0 and high%2 ==0:
        return int((high-low)/2)
    else:
        return int((high-low)/2)+1

low = 4
high = 10
print(countOdds(low,high))
