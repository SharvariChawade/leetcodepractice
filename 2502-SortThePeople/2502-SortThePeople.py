# Last updated: 09/09/2025, 00:42:46
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def quicksort(arr, names, low, high):
            if low < high:
                pivot_index = partition(arr, names, low, high)
                quicksort(arr, names, low, pivot_index - 1)
                quicksort(arr, names, pivot_index + 1, high)

        def partition(arr, names, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] > pivot:  # Change comparison to sort in descending order
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    names[i], names[j] = names[j], names[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            names[i + 1], names[high] = names[high], names[i + 1]
            return i + 1
        
        n = len(heights)
        quicksort(heights, names, 0, n-1)
        return names