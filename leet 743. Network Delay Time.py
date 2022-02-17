class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 인접 리스트 구성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # 큐 변수 : [(소요시간, 정점)] 시작점부터 현재위치까지의 소요시간을 나타낸다
        Q = [(0, k)] 
        dist = collections.defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q) #time은 시간, node는 정점
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        if len(dist) == n :
            return max(dist.values())
        return -1
