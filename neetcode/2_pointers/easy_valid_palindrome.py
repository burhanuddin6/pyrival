# https://leetcode.com/problems/valid-palindrome/
# beats 70%
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        a = []
        for i in s:
            if i.isalnum():
                a.append(i)
        s = ''.join(a)
        print(s)
        p1 = len(s) - 1
        p2 = 0
        while(p2 <= p1):
            if s[p1] != s[p2]:
                return False
            p1 -= 1
            p2 += 1
        return True
        