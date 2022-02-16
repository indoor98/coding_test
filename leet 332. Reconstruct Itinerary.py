class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
       #그래프 구성 단계
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
   
        route = []
        
        #dfs함수 작성
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        
        
        dfs('JFK')
        return route[::-1]
      
#pop(0)을 pop()으로 개선한 코드
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets, reverse=True): # reverse=True로 설정하여 애초에 역순으로 그래프에 들어가도록 함
            graph[a].append(b)
            
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            
        dfs('JFK')
        return route[::-1]
