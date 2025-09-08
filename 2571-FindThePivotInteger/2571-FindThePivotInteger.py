# Last updated: 09/09/2025, 00:42:47
class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = list(range(1,n+1))
        l = 0
        r = n-1
        sl = arr[l]
        sr = arr[r]
        while(l<r):
            if(sr>sl):
                l = l+1
                sl = sl+arr[l]
            else:
                r = r-1
                sr = sr+arr[r]
        if(sl == sr):
            return l+1
        else:
            return -1