# Last updated: 09/09/2025, 00:43:04
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(word.isupper()):
            return True
        elif(word.islower()):
            return True
        elif(word[0].isupper() == True):
            i = 1
            while(i<len(word)):
                if(word[i].isupper() == True):
                    return False
                i = i+1
            return True
        else:
            return False