// Last updated: 09/09/2025, 00:43:14
#include <unordered_map>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> freq;
        for (int ele : nums)
        {
            freq[ele]++;
            if(freq[ele]>int(nums.size()/2))
            {
                return ele;
            }
        }
        return 0;
    }
};