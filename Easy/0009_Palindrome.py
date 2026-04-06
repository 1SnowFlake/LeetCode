class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        return str(x)[::-1]==str(x) 