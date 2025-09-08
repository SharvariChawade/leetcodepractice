# Last updated: 09/09/2025, 00:43:28
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i = 0
        n = len(nums)-1
        
        while(i <= n):
            mid = (i+n)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                i = mid + 1
            else:
                n = mid-1
            
        return i
        