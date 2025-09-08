# Last updated: 09/09/2025, 00:43:29
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for i in s:
            
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
                
            elif i == ')':
                if stack and stack[-1] is  '(':
                    stack.pop()
                else:
                    return False
            
            elif i == ']':
                if stack and stack[-1] is  '[':
                    stack.pop()
                else:
                    return False
            
            elif i == '}':
                if stack and stack[-1] is  '{':
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0