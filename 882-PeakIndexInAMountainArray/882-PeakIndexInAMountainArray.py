# Last updated: 09/09/2025, 00:43:00
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # flag = 0
        # ind = 0

        # while(flag == 0 and ind<len(arr)):
        #     if(arr[ind] < arr[ind+1]):
        #         ind = ind + 1
        #     else:
        #         flag = 1
        m = max(arr)
        ind = arr.index(m)
        return ind