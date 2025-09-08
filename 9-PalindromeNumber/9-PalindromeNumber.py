# Last updated: 09/09/2025, 00:43:35
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        return str(x) == str(x)[::-1]