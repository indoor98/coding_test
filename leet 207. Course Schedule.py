# dfs이용 풀이(time out발생)
 def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #그래프 만들기
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        
        def dfs(i):
            #순환 구조이면 False
            if i in traced:
                return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            #탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            
            return True
        
        #순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
      
# 가지치기를 이용한 최적화
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        visited = set()
        
        def dfs(i):
            if i in traced:
                return False
            
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
                
            traced.remove(i)
            visited.add(i)
            
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True  
