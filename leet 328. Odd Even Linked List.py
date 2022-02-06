#공간복잡도 O(1), 시간복잡도 O(n)이라는 제한 조건이 있다.
#따라서 리스트로 변환 후 파이썬 내장함수를 이용한 풀이의 사용이 제한된다.

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #예외 처리
        if head == None:
            return None
        
        
        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head
