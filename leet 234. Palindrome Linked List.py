# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#풀이1) 리스트 변환 풀이
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head
        a: List = []
        while tmp != None:
            a.append(tmp.val)
            tmp=tmp.next
        
        return a == a[::-1]
      

#풀이 2) 덱을 활용, 위 풀이1은 파이썬의 리스트 인덱싱을 사용하였기 때문에 더 빠르게 나옴.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q : Deque = collections.deque()
        
        if not head : #head가 비어있을 경우 예외처리
            return True
        
        node = head
        while node != None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
              
#풀이 3) 러너(투 포인터 변형)을 활
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        rev = None
        
        while fast and fast.next :
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next
                
        while rev and rev.val == slow.val:
            rev,slow = rev.next, slow.next
        
        return not rev
    
