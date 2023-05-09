class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        post = []
        pre = []
        po = 1
        pr = 1
        for i in range(len(nums)):
            po = po * nums[i]
            post.append(po)
        for i in range(len(nums)):
            pr = pr * nums[len(nums)-1-i]
            pre.insert(0,pr)
        
        for i in range(len(nums)):
            if (i == 0):
                result.append(1*pre[i+1])
            elif(i == len(nums)-1):
                result.append(1*post[i-1])
            else:
                result.append(pre[i+1]*post[i-1])
        print(pre, post)
        return result