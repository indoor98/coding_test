#풀이1) 리스트 변환을 이용한 풀이
class Solution:
    #연결리스트를 역순으로 변환하는 함수
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
        
    
    # 연결 리스트를 파이썬 리스트로 변환하는 함수
    def toList(self, head : ListNode) -> List:
        node = head
        pythonlist = []
        while node:
            pythonlist.append(node.val)
            node = node.next
        
        return pythonlist
            
    
    
    # 파이썬 리스트를 연결리스트로 변환하는 함수
    def toReversedLinkedList(self, pythonlist : List) -> ListNode:
        prev: ListNode = None
        
        for r in pythonlist:
            node = ListNode(r)
            node.next, prev = prev, node
        
        return node
        
            
        
    
    
    #두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        
        return self.toReversedLinkedList(str(resultStr))
        
        
#풀이2) 전가산기를 이용한 풀이
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next
        
