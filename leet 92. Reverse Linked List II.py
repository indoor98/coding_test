# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #예외처리
        if not head or left == right:
            return head
        
        root = start = ListNode(None)
        root.next = head #최종 반환값
        for _ in range(left -1):
            start = start.next
        end = start.next
        
        for _ in range(right-left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next
