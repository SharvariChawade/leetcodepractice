# Last updated: 09/09/2025, 00:43:39
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[nums[i]]=i
        return