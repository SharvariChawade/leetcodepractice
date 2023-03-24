#include<unordered_set>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int band = 0;
        int len = 0;    
        unordered_set<int> s;
        for (int x:nums){
            s.insert(x);
        }
        
        for(int x:nums){
            band = 0;
            if (s.find(x-1)==s.end() ){
                band++;
                while(s.find(x+1) != s.end()){
                    x++;
                    band++;
                }
                if(band>len) {
                    len = band;
                }
            }
        }
        return len;
    }
};