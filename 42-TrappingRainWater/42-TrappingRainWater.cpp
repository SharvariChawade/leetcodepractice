// Last updated: 09/09/2025, 00:43:26
class Solution {
public:
    int trap(vector<int>& height) {
        
        int n = height.size();
        vector<int> l1(n,0), r1(n,0);
        int ans=0;
        l1[0] = height[0];
        r1[n-1] = height[n-1];
        
        for(int i=1;i<height.size();i++){
            l1[i] = max(l1[i-1],height[i]);
            r1[n-i-1] = max(r1[n-i],height[n-i-1]);
        }
        
        for(int i = 0; i<height.size();i++){
            ans = ans + (min(l1[i],r1[i]) -height[i]);
        }
        
        return ans;
    }
};