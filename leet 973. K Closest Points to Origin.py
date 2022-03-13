class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points: #points 의 원소들이 [x, y]꼴이므로 (x, y)꼴로 받아냄 [x, y]꼴로 받아내도 가능
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))
        
        result = []
        for i in range(0, k):
            result.append(heapq.heappop(heap)[1:])
            
        return result
        
        
