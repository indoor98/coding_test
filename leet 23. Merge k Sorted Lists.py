# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i])) 
                # heap변수에 (lists[i].val, i, lists[i])를 lists[i].val을 기준으로 최소 힙을 만족시키며 삽입한다.
                # 자세한 내용은 파이썬 heap모듈 확인
                
        while heap:
            node = heapq.heappop(heap) #현재 heap에 저장된 값 중 val값이 가장 작은 값을 할당
            idx = node[1] #인덱스 할당
            #result에 node변수에 저장된 연결리스트의 헤드노드를 연결시킴
            result.next = node[2]
            
            #헤드노드를 이후 노드들을 다시 최소 heap성질을 만족시키며 heap변수에 저장함.
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
                
        return root.next        
                
