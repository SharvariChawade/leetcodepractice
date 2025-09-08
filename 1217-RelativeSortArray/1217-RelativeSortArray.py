# Last updated: 09/09/2025, 00:42:56
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output = []
        for i in arr2:
            n = arr1.count(i)
            for x in range(n):
                output.append(i)
                arr1.remove(i)
        arr1.sort()
        for i in arr1:
            output.append(i)
        
        return output
        