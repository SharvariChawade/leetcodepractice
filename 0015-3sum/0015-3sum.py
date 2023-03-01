class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        sol = []
        length = len(nums)
        
        for i in range(length-2):
            
            if (i>0) and nums[i]==nums[i-1]:
                continue
            
            l = i+1
            r = length - 1
            
            while(l < r):
                s = nums[i]+nums[l]+nums[r]
                
                if(s>0):
                    r = r-1
                elif(s < 0):
                    l = l+1
                    
                else:
                    sol.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l = l+1
                    while l<r and nums[r] == nums[r-1]:
                        r = r-1
                    l = l+1
                    r = r-1
                    
        return sol