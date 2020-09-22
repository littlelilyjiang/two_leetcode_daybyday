'''
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
'''

def findWords(words):
    list1='qwertyuiopQWERTYUIOP'
    list2='asdfghjklASDFGHJKL'
    list3='zxcvbnmZXCVBNM'
    res = []
    for word in words:
        tmp = ''
        for t in word:
            if t in list1:
                tmp = tmp+'1'
            elif t in list2:
                tmp = tmp+'2'
            elif t in list3:
                tmp = tmp+'3'
        tmp = set(tmp)
        if len(tmp) == 1:
            res.append(word)
    return res


words=["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))

