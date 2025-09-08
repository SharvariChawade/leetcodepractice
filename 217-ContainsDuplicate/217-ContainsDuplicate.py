# Last updated: 09/09/2025, 00:43:09
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False