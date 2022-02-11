#개별 체이닝을 활용할 예정이다. 따라서 ListNode class를 따로 정의한다.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        
        
class MyHashMap:

    def __init__(self):
        self.size = 1000 #사이즈를 1000으로 적당히 설정
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        #인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None: #table을 defaultdict(ListNode)로 할당하였기 때문에 value값을 확인해야한다.
            self.table[index] = ListNode(key, value)
            return 
        
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None: #만일 처리하지 않을시 while문 다음 코드에서 p=None이 되어 에러가 발생함.
                break
            p = p.next
        p.next = ListNode(key, value)
        
        
    def get(self, key: int) -> int:
        index = key % self.size
        # 해당 인덱스에 노드가 없는 경우
        if self.table[index].value is None:
            return -1
        
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p=p.next
        return -1
    

        
    def remove(self, key: int) -> None:
        index = key % self.size 
        #해당 인덱스에 노드가 존재하지 않는 경우
        if self.table[index].value is None:
            return
        
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return 
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
            
            
        
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
