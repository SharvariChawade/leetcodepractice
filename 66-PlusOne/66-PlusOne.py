# Last updated: 09/09/2025, 00:43:22
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits) - 1
        
        while(n>=0):
            num = digits[n]
            if digits[n] is 9:
                digits[n] = 0
                n -= 1
            else:
                digits[n] = num + 1
                break
                
        if(n == -1):
            digits = digits[::-1]
            digits.append(1)
            digits = digits[::-1]
        
        return digits
        