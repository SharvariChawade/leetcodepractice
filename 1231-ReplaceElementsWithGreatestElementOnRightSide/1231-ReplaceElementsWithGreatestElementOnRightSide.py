# Last updated: 09/09/2025, 00:42:54
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #approach 1
        # n = len(arr)
        # rm = -1
        # for i in range(n - 1, -1, -1):
        #     current = arr[i]
        #     arr[i] = rm
        #     rm = max(rm, current)
        # return arr

        #approach 2
        n = len(arr)
        s,l = n-2,n-1
        rm = arr[l]
        while(s>=0):
            temp = arr[s]
            arr[s] = rm
            rm = max(temp, rm)
            s -= 1
        arr[n-1] = -1
        return arr 
        
        #approach 3
        # for i in range(len(arr)):
        #     if i == len(arr)-1:
        #         arr[i] = -1
        #     else:
        #         arr[i] = int(max(arr[i+1 : ]))
        # return arr