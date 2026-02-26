# Last updated: 27/02/2026, 01:38:53
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        l = 0
7        r = 1
8        
9        while(r<len(nums)):
10            if(nums[l]==0 and nums[r]!=0):
11                temp = nums[l]
12                nums[l] = nums[r]
13                nums[r] = temp
14                l += 1
15                r += 1
16            elif (nums[l]==0 and nums[r]==0):
17                r += 1
18            elif(nums[l]!=0 and nums[r]==0):
19                r +=1
20                l += 1
21            elif(nums[l]!=0 and nums[r]!=0):
22                r+=1
23                l+=1