class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #중첩함수로 dfs함수 작성
        def dfs(index, path):
            # 끝까지 탐색하면 백 트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
                    
        #예외 처리
        if not digits:
            return []
        
        dic = {"2": "abc", "3":"def", "4":"ghi", "5":'jkl', '6':'mno',
               '7': 'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        dfs(0, "")
        
        return result
