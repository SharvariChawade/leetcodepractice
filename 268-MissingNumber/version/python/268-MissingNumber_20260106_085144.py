# Last updated: 06/01/2026, 08:51:44
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        a = 0
4        while a in set(nums):
5            a += 1
6        return a