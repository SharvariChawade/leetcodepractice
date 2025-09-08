# Last updated: 09/09/2025, 00:42:53
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for n,i in enumerate(sentence.split(" ")):
            if(len(i)>=len(searchWord)):
                if(i[:len(searchWord)] == searchWord[:]):
                    return n+1
        return -1