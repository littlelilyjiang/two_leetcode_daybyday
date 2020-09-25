'''
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
'''

def CheckPermutation(s1, s2):
    list_s1= list(s1)
    list_s2 = list(s2)
    for i in list_s1:
        if i in list_s2:
            list_s2.remove(i)
    if len(list_s2) == 0:
        return True
    else:
        return False

s1 = "abc"
s2 = "bca"
print(CheckPermutation(s1,s2))