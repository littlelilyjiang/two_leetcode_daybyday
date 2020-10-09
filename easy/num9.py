'''

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''

def isPalindrome(x):
    tmp_str = str(x)
    for i in range(int(len(tmp_str)/2)):
        if tmp_str[i] != tmp_str[-i-1]:
            return False
    return True


print(isPalindrome(-111011))

