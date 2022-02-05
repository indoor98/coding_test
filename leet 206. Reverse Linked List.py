#재귀 함수를 이용한 풀이
#prev는 None부터 시작해서 head를 따라 이동한다.
#node는 head부터 시작해서 이동한다.

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)
    

#반복을 이용한 풀이
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node :
            node.next, node, prev = prev, node.next, node
        
        return prev
