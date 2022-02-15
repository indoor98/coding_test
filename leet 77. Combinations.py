#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(elements, start:int, k: int): # elements = n개의 수 배열, 
            if k == 0 : #elements에 k개의 수가 찼을 경우 result에 추가
                result.append(elements[:])
            
            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
                
        dfs([], 1, k)
        return result
    
