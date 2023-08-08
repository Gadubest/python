class Solution:
    def isPalindrome(self, x: int) -> bool:
        txt = str(x)
        for i in range(txt.__len__()):
            if(txt[i] != txt[txt.__len__()-1-i]):
                return False
        return True

#https://leetcode.com/problems/palindrome-number/