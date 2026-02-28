# Last updated: 28/02/2026, 11:32:43
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l = 0
4        r = len(s)-1
5        s = s.lower()
6        while(r>l):
7            while l<r and s[r] not in 'qwertyuiopasdfghjklzxcvbnm1234567890':
8                r -= 1
9            while l<r and s[l] not in 'qwertyuiopasdfghjklzxcvbnm1234567890':
10                l+=1
11            if(s[r]==s[l]):
12                r-=1
13                l+=1
14            else:
15                return False
16        return True