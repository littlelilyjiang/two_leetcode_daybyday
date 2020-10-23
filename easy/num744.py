'''
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：

如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def nextGreatestLetter(letters, target):
    letters_set = set(letters)
    letters= list(letters_set)
    letters.sort(reverse=True)
    letters.reverse()
    for i in letters:
        if i> target:
            return i
    return letters[0]

letters = ["c","f","j"]
target='c'
print(nextGreatestLetter(letters,target))
