# Last updated: 23/11/2025, 18:31:31
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while(original in nums):
            original*=2
        return original