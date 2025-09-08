# Last updated: 09/09/2025, 00:43:23
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        l = list(s.split(" "))
        
        for i in l[::-1]:
            if i is not '':
                return len(i)

            