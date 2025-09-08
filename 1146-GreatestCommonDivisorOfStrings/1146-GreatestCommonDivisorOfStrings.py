# Last updated: 09/09/2025, 00:42:57
import math
class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 == str1[0]*(len(str1)) and str2 == str2[0]*(len(str2))):
            l = math.gcd(len(str1),len(str2))
            if(str1[0] == str2[0]):
                sol = str1[1]*l
                return sol
            else:
                return ''
        elif len(str1) < len(str2):
            if (str2 == str1*int(len(str2)/len(str1))):
                return str1
            else:
                sol = ''
                for i in range(len(str1)):
                    sol += str1[i]
                    if(str1 == sol*int(len(str1)/len(sol))):
                        if(str2 == sol*int(len(str2)/len(sol))):
                            i = int(len(str1)/len(sol))
                            while(i>0):
                                soldash = ''
                                soldash = sol *i
                                if(str1 == soldash*int(len(str1)/len(soldash)) and str2 == soldash*int(len(str2)/len(soldash))):
                                    return soldash
                                else:
                                    i -= 1
                                
                            if (i == 0):
                                return sol
                                
                        else:
                            return ''
        elif len(str1) > len(str2):
            if (str1 == str2*int(len(str1)/len(str2))):
                return str2
            else:
                sol = ''
                for i in range(len(str2)):
                    sol += str2[i]
                    if(str2 == sol*int(len(str2)/len(sol))):
                        if(str1 == sol*int(len(str1)/len(sol))):
                            i = int(len(str2)/len(sol))
                            while(i>0):
                                soldash = ''
                                soldash = sol *i
                                if(str1 == soldash*int(len(str1)/len(soldash)) and str2 == soldash*int(len(str2)/len(soldash))):
                                    return soldash
                                else:
                                    i -= 1
                                
                            if (i == 0):
                                return sol
                        else:
                            return ''

        elif len(str1) == len(str2):
            sol = ''
            if str1 == str2:
                return str1
                # for i in range(len(str2)):
                #     sol += str2[i]
                #     if(str2 == sol*int(len(str2)/len(sol))):
                #         return sol
            else:
                return ''
                  

