# Last updated: 23/11/2025, 17:58:52
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min = 0
        for i in nums:
            if(i%3 != 0):
                min+=1
        
        return min