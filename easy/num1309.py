'''
给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：

字符（'a' - 'i'）分别用（'1' - '9'）表示。
字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
返回映射之后形成的新字符串。

题目数据保证映射始终唯一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def freqAlphabets(s):
    return s.replace('10#','j').replace('11#','k').replace('12#','l').replace('13#','m').replace('14#','n').replace('15#','o').replace('16#','p').replace('17#','q').replace('18#','r').replace('19#','s').\
        replace('20#','t').replace('21#','u').replace('22#','v').replace('23#','w').replace('24#','x').replace('25#','y').replace('26#','z').replace('1','a').replace('2','b').replace('3','c').replace('4','d').replace('5','e').replace('6','f').replace('7','g').replace('8','h').replace('9','i')

s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"

print(freqAlphabets(s))