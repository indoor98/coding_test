#풀이 1) heapq모듈 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n) #파이썬 heap모듈은 최소힙이기 때문에 -n 으로 집어넣는다.
            
        for _ in range(k - 1):
            heapq.heappop(heap)
            
        return -heapq.heappop(heap)
      
#풀이 2) heapq모듈의 heapify 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
      
#풀이 3) heapq모듈의 nlargest 이용
class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]

#풀이 4) 정렬을 이용한 풀이
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
