#인덴트 조심하자
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        
        for char in s:
            if char not in table.keys():
                stack.append(char)
            
            elif (not stack) or table[char] != stack.pop():
                return False
            
            
        return len(stack)==0
                
