'''
给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证 text 至少包含一个单词 。

请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。

返回 重新排列空格后的字符串 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rearrange-spaces-between-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def reorderSpaces(text):
    space_count = text.count(' ')
    if space_count ==0:
        return text
    text_list = text.split(' ')
    real_list =[]
    for i in text_list:
        if i != '':
            real_list.append(i)
    if len(real_list) == 1:
        return real_list[0] + space_count*' '
    real_space=int(space_count/(len(real_list)-1))
    left_space = space_count%(len(real_list)-1)
    res = ''
    for j in real_list:
        res = res+j+' '*real_space
    return res[0:len(res)-real_space]+' '*left_space

text = "  hello"
print(reorderSpaces(text))