# Last updated: 06/01/2026, 08:55:27
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        a = 0
5        while a in num_set:
6            a += 1
7        return a