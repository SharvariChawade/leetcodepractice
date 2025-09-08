// Last updated: 09/09/2025, 00:43:08

class Solution {
public:
    bool isPowerOfTwo(int n) {
        int x = 0;
        int prod = 1;
        while(x < 30){
            if (prod == n){
                return true;
            }
            prod = 2*prod;
            x = x+1;  
        }
        if(n == pow(2,30)){
            return true;
        }
        // for (int i = 0;i<=30;i++){
        //     int ans = pow(2,i);
        //     if(ans == n){
        //         return true;
        //     }
        // }
        return false;
    }
};