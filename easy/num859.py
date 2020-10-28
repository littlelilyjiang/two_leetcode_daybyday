'''
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/buddy-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def buddyStrings(A, B):
    list_a = list(A)
    list_b = list(B)
    if A == B and A == '':
        return False
    if len(list_a) != len(list_b):
        return False
    tmp1 = 0
    tmp2 = 0
    time = 0
    for i in range(len(list_a)):
        if list_a[i] != list_b[i]:
            if tmp1 == 0:
                tmp1 = i
            else:
                tmp2 = i
            time = time + 1
    if time > 2:
        return False

    if time == 0 and int(len(list_a) / len(set(list_a))) < 2:
        return False
    if list_a[tmp1] == list_b[tmp2] and list_a[tmp2] == list_b[tmp1]:
        return True
    return False


A='ab'
B='ab'
print(buddyStrings(A,B))




