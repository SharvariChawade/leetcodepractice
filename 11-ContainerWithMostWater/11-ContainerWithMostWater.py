# Last updated: 09/09/2025, 00:43:34
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while(l < r):
            area = min(height[l],height[r]) * (r-l)
            max_area = max(area,max_area)
            if(height[l]<height[r]):
                l += 1
            else:
                r -= 1
        return max_area