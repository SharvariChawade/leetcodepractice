# Last updated: 06/01/2026, 08:41:32
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        m = max(nums)
4        s = sum(nums)
5        a = (m*(m+1))//2
6        if(a-s != 0):
7            return a-s
8        else:
9            if (0 in nums):
10                return m+1
11            else:
12                return 0