# Last updated: 09/09/2025, 00:42:51
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i,j = 0,1
        max_diff = -1

        while(j<len(nums)):
            if(nums[i]<nums[j]):
                max_diff = max(max_diff, nums[j]-nums[i])
            else:
                i=j
            j += 1
        
        return max_diff