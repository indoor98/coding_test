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

#반복을 이용한 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route, stack = [], ['JFK']
        while stack:
            #반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
            
        return route[::-1]
