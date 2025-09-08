# Last updated: 09/09/2025, 00:43:02
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_strings = {}
        
        for index, s in enumerate(list1):
            if s not in dict_strings:
                dict_strings[s] = [index]
            else:
                dict_strings[s].append(index)

        for index, s in enumerate(list2):
            if s not in dict_strings:
                dict_strings[s] = [index]
            else:
                dict_strings[s].append(index)

        def get_index_sum(l):
            max = 3000
            if (len(l) == 2):
                return sum(l)
            else:
                return max


        r = list(map(get_index_sum,dict_strings.values()))
        r = r[:len(list1)]
        min_indices = [index for index, value in enumerate(r) if value == min(r)]
        result = []
        if min_indices != []:
            for i in min_indices:
                result.append(list1[i])
        
        return result