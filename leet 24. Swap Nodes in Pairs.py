#각 노드의 val만 바꾸는 풀이, 면접에서 질문이 들어올 경우 "빠르게 풀기"위하여 선택한 풀이임을 강조해야한다.
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next :
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
            
        return head


#풀이 2) 반복을 이용한 풀이
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next :
            b = head.next
            head.next = b.next
            b.next = head
            prev.next = b
            head = head.next
            prev = b.next
        return root.next
      
      
      
#풀이3) 재귀 구조로 스왑
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p=head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
            
