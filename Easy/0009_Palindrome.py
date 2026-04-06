class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
	string = str(x)
        return string[::-1]==string 